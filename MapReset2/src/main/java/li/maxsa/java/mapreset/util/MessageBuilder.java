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

import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

/**
 * @author msalihov (Maxim Salikhov)
 */
public class MessageBuilder {

    private StringBuilder parts;
    protected CommandSender sender;

    public MessageBuilder(CommandSender sender) {
        parts = new StringBuilder();
        this.sender = sender;
    }

    public MessageBuilder(Player player) {
        parts = new StringBuilder();
        sender = player;
    }

    public MessageBuilder append(Object obj) {
        parts.append(obj);
        return this;
    }


    public void send() {
        sender.sendMessage(parts.toString());
    }
}
