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

import java.io.File;
import java.util.Properties;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class MRWorld {

    private Integer id;
    private String name;
    private boolean copy;
    private boolean withProps;
    private File copyFile;
    private Properties props;

    public MRWorld(Integer id) {
        this.id = id;
        copy = false;
    }

    public MRWorld(Integer id, File copyFile) {
        this.id = id;
        copy = true;
        this.copyFile = copyFile;
    }

    public MRWorld(Integer id, File copyFile, Properties props) {
        this.id = id;
        copy = true;
        withProps = true;
        this.copyFile = copyFile;
        this.props = props;
    }

    public String getName() {
        return name;
    }

    public void load() {

    }

    public void archive() {

    }

    public void unload() {

    }

}
