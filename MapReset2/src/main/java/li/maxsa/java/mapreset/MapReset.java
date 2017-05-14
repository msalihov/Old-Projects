/*
 * Copyright 2013 Maxim Salikhov.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package li.maxsa.java.mapreset;

import com.sk89q.bukkit.util.CommandsManagerRegistration;
import com.sk89q.minecraft.util.commands.CommandException;
import com.sk89q.minecraft.util.commands.CommandPermissionsException;
import com.sk89q.minecraft.util.commands.CommandUsageException;
import com.sk89q.minecraft.util.commands.CommandsManager;
import com.sk89q.minecraft.util.commands.MissingNestedCommandException;
import com.sk89q.minecraft.util.commands.WrappedCommandException;
import li.maxsa.java.mapreset.commands.MapResetCommands;
import li.maxsa.java.mapreset.listeners.PlayerConnectionListener;
import li.maxsa.java.mapreset.world.WorldManager;
import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.command.ConsoleCommandSender;
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.plugin.PluginManager;
import org.bukkit.plugin.java.JavaPlugin;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class MapReset extends JavaPlugin {

    private static MapReset instance;
    private CommandsManager<CommandSender> commandsManager;

    @Override
    public void onEnable() {
        instance = this;
        MRLogger.log("MapReset " + getVersion() + " loading...");
        saveDefaultConfig();
        registerCommands();
        registerListeners();
        WorldManager.init();
        MRLogger.log("MapReset " + getVersion() + " loaded!");
    }

    @Override
    public void onDisable() {

    }

    public static MapReset get() {
        return instance;
    }

    public static void saveConf() {
        instance.saveConfig();
    }

    public static FileConfiguration getConf() {
        return instance.getConfig();
    }

    public static String getVersion() {
        return instance.getDescription().getVersion();
    }

    private void registerCommands() {
        commandsManager = new CommandsManager<CommandSender>() {
            @Override
            public boolean hasPermission(CommandSender commandSender, String s) {
                return commandSender instanceof ConsoleCommandSender || commandSender.hasPermission(s);
            }
        };
        CommandsManagerRegistration cmdRegister = new CommandsManagerRegistration(instance, commandsManager);
        cmdRegister.register(MapResetCommands.ParentMapResetCommand.class);
    }

    private void registerListeners() {
        PluginManager pluginManager = Bukkit.getPluginManager();
        pluginManager.registerEvents(new PlayerConnectionListener(), instance);
    }

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String commandLabel, String[] args) {
        try {
            commandsManager.execute(cmd.getName(), args, sender, sender);
        } catch (CommandPermissionsException e) {
            sender.sendMessage(ChatColor.RED + "You don't have permission.");
        } catch (MissingNestedCommandException e) {
            sender.sendMessage(ChatColor.RED + e.getUsage());
        } catch (CommandUsageException e) {
            sender.sendMessage(ChatColor.RED + e.getMessage());
            sender.sendMessage(ChatColor.RED + e.getUsage());
        } catch (WrappedCommandException e) {
            if (e.getCause() instanceof NumberFormatException) {
                sender.sendMessage(ChatColor.RED + "Number expected, string received instead.");
            } else {
                sender.sendMessage(ChatColor.RED + "An error has occurred. See console.");
                e.printStackTrace();
            }
        } catch (CommandException e) {
            sender.sendMessage(ChatColor.RED + e.getMessage());
        }
        return true;
    }

}
