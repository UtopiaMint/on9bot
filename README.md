# On9 Bot

A [Telegram](https://telegram.org) [bot](https://core.telegram.org/bots) providing simple utilities.
You may find it [here](https://t.me/On9Bot).

(Moved repository here so no one can see my stupid commits, heh)

## Commands (in alphabetical order)

Some commands require/allow you to reply to a message.\
Required: `[in reply to message]`\
Optional: `(in reply to message)`

### /feedback
Send feedback to the creator.

Usage: `/feedback@On9Bot <text>`

### /file_id
Gives you the file id of the file you replied to.
You must reply to a file.
Note that the file id may be different for other bots.

Usage: `[in reply to message] /file_id@On9Bot`

### /id
Tells you your user id.
If used in group, chat id will also be given.
If you reply to another message, user id of replied message's sender will be given instead.
User id of original message's sender will be given instead if replied message is forwarded.

Usage: `(in reply to message) /id@On9Bot`

### /link
Gives you a link of the message the message you replied to in the format `t.me/username/message_id`.
You must use this in groups and reply to a message.
If not used in public (super)groups, message id of the message you replied to is provided.

Usage: `[in reply to message] /link@On9Bot`

### /ping
Replies if bot is alive.

Usage: `/ping@On9Bot`

### /pinned
Replies to the pinned message.
You must use this in groups.
If the pinned message is sent by another bot, an inline button to that message is provided instead.
If the pinned message is sent by another bot and the (super)group is not private,
message id of the pinned message is provided.

Usage: `/pinned@On9Bot`

### /r
Repeats text, then deletes your message with "/r" if the bot has the admin right to do so.
Simply says repeats "hi" if your message on "/r hi".
If you reply to a message, the bot replies to that message as well.
However, if you reply to a message and your message does not have any arguments,
the bot repeats the replied message exactly how it was formatted.*

*This only works with plain text messages. Captions are not supported.

Usage: `(in reply to message) /r@On9Bot <text>` or `[in reply to plain text message] /r@On9Bot`

### /remove_keyboard
Replaces existing reply keyboard markup and removes it.

Usage: `/remove_keyboard@On9Bot`

### /user_info
Gives you your name, user id, name, username* and language code*.
Tells you your status (creator, member, banned, etc) and rights** as well if used in groups or supergroups.
If you reply to another message, user information of the replied message's sender will be given instead.

*Only given if you have them.
**Only applicable to administrators and restricted users.

Usage: `(in reply to message) /user_info@On9Bot`

## Message replies (in reply priority)

### Service messages
Replies on bot join (including itself) and leaving member.

### "Hello" from bot owner
Greets owner.

### "no u" in text
Counts the amount of linked "no"s before a "u" (as shown below).
```Python
no_count = max([p.count("no") for p in [s.strip() for s in update.message.text.lower().split("u") if "no" in s]])
```
Then replies with ("no" count + 1) "no"s followed by a "u" if "no" count is less than 100.
Else, replies with the "infinity no u" sticker.