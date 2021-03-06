import re

from telegram import User, Chat, Message
from telegram.error import TelegramError
from telegram.ext import BaseFilter

from config import BOT, OWNER, OWNER_USERNAME

# Constants


POKER_CARDS = [f"{f}{c}" for f in ("♦️", "♣️", "♥️", "♠️") for c in (*"A23456789", "10", *"JQK")]
GITHUB_SOURCE_CODE_LINK = "https://github.com/Tr-Jono/on9bot"
RAND_FUNC_POST_LINK = ""
MARKDOWN_ERROR_TEXT = r'''Markdown error occurred: {}.
Parse mode = Markdown. Use a backslash ("\") before a markdown character to escape it, like this:
"\_", "\*", "\`"'''


# Functions


def yn_processor(xpr: bool) -> str:
    return "Yes" if xpr else "No"


def del_msg(msg: Message) -> None:
    try:
        msg.delete()
    except TelegramError:
        pass


def kick_member(chat: Chat, user_id: int) -> None:
    try:
        chat.kick_member(user_id)
    except TelegramError:
        pass


def echo_owner_check(text: str) -> None:
    text = text.lower()
    assert OWNER_USERNAME.lower() not in text
    assert not ("[" in text and f"](tg://user?id={OWNER.id})" in text)


def check_number_man(user: User) -> bool:
    return bool(re.match(r"(\d{8}) \1", user.full_name))


# Filters


class CheckNumberMan(BaseFilter):
    name = 'CheckNumberMan'

    def filter(self, message: Message) -> bool:
        return check_number_man(message.from_user)


class BotIsAdmin(BaseFilter):
    name = 'BotIsAdmin'

    def filter(self, message: Message) -> bool:
        return BOT.id in [admin.id for admin in message.chat.get_administrators()]


check_number_man_filter: CheckNumberMan = CheckNumberMan()
bot_is_admin_filter: BotIsAdmin = BotIsAdmin()
