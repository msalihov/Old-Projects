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
package li.maxsa.java.mapreset.world;

import org.bukkit.World;
import org.bukkit.entity.Player;

import java.util.HashMap;
import java.util.Map;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class WorldManager {

    private static Map<Integer, MRWorld> worlds;
    private static Map<World, Integer> worldsToIdMap;

    public static void init() {
        worlds = new HashMap<>();
        worldsToIdMap = new HashMap<>();
    }

    public static void newWorld() {

    }

    public static MRWorld getMRWorld(Integer id) {
        return worlds.get(id);
    }

    public static MRWorld getMRWorld(World world) {
        return worlds.get(worldsToIdMap.get(world));
    }

    public static MRWorld getMRWorld(Player player) {
        return worlds.get(worldsToIdMap.get(player.getWorld()));
    }

}
