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
package li.maxsa.java.mapreset.commands;

import com.sk89q.minecraft.util.commands.Command;
import com.sk89q.minecraft.util.commands.CommandContext;
import com.sk89q.minecraft.util.commands.CommandException;
import com.sk89q.minecraft.util.commands.CommandPermissions;
import com.sk89q.minecraft.util.commands.NestedCommand;
import li.maxsa.java.mapreset.MapReset;
import li.maxsa.java.mapreset.util.MessageBuilder;
import li.maxsa.java.mapreset.util.MultilineMessageBuilder;
import li.maxsa.java.mapreset.util.Presets;
import li.maxsa.java.mapreset.util.WorldUtil;
import li.maxsa.java.mapreset.world.MRWorld;
import li.maxsa.java.mapreset.world.WorldManager;
import org.bukkit.ChatColor;
import org.bukkit.World;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class MapResetCommands {

    public static class ParentMapResetCommand {
        @Command(aliases = {"mapreset", "mapr", "mreset", "mr"}, desc = "All MapReset commands", usage = "<command>",
                min = 0,
                max = -1)
        @NestedCommand(MapResetCommands.class)
        public static void cmd(final CommandContext args, CommandSender sender) throws CommandException {
        }
    }

    @Command(aliases = {"version", "v"}, desc = "Returns the version of the plugin currently running", max = 0)
    @CommandPermissions("mapreset.info.version")
    public static void version(final CommandContext args, CommandSender sender) {
        MessageBuilder msgBuilder = new MessageBuilder(sender);
        msgBuilder.append(ChatColor.GOLD);
        msgBuilder.append("Current MapReset version: ");
        msgBuilder.append(ChatColor.GREEN + MapReset.getVersion());
        msgBuilder.send();
    }

    @Command(aliases = {"info", "i"}, desc = "Returns the information about the currently set world", max = 0)
    @CommandPermissions("mapreset.info.info")
    public static void info(final CommandContext args, CommandSender sender) throws CommandException {
        if (sender instanceof Player) {
            Player player = (Player) sender;
            World bWorld = player.getWorld();
            MRWorld world = WorldManager.getMRWorld(bWorld);
            MultilineMessageBuilder msgBuilder = new MultilineMessageBuilder(player);
            msgBuilder.append(Presets.HEADER_TEMPLATE.replaceAll("%var", "World Information"));
            msgBuilder.append(ChatColor.GOLD + "Name: " + ChatColor.GREEN + (world == null ? bWorld.getName() : world
                    .getName()));
            msgBuilder.append(ChatColor.GOLD + "MapReset world: " + (world == null ? ChatColor.RED + "false" :
                    ChatColor.GREEN + "true"));
            if (world == null) {
                msgBuilder.append(WorldUtil.getEnvironmentString(bWorld));
                msgBuilder.append(WorldUtil.getWorldTypeString(bWorld));
            } else {
                msgBuilder.append(WorldUtil.getEnvironmentString(bWorld));
                msgBuilder.append(WorldUtil.getWorldTypeString(bWorld));
            }
            msgBuilder.send();
        } else {
            throw new CommandException("This command may only be used by a player.");
        }
    }
}
