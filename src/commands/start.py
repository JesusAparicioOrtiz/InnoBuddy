import json
import os
from commands.readMesssage import readMessage

def start(update, context):
    mensaje = readMessage("start")
    context.bot.send_message(update.message.chat_id, mensaje, parse_mode='MarkdownV2')
