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

import java.util.logging.Level;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class MRLogger {

    public static void log(String msg) {
        MapReset.get().getLogger().log(Level.INFO, msg);
    }

    public static void log(Level lvl, String msg) {
        MapReset.get().getLogger().log(lvl, msg);
    }

}
