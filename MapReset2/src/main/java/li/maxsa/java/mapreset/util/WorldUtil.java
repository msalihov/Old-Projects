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
package li.maxsa.java.mapreset.util;

import org.bukkit.ChatColor;
import org.bukkit.World;
import org.bukkit.WorldType;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class WorldUtil {

    public static String getEnvironmentString(World world) {
        return ChatColor.GOLD + "Environment: " + (world.getEnvironment() == World.Environment.NORMAL ? ChatColor
                .GREEN + "NORMAL" : ChatColor.YELLOW + world.getEnvironment().name());
    }

    public static String getWorldTypeString(World world) {
        return ChatColor.GOLD + "Type: " + (world.getWorldType() == WorldType.NORMAL ? ChatColor.GREEN + "NORMAL" :
                ChatColor.YELLOW + world.getWorldType().name());
    }
}
