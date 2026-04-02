import fear_and_greed
index=fear_and_greed.get().value
index_str=f"{index:.1f}"

!pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv("token_ID.env")
TOKEN=os.getenv("LINE_TOKEN")
user_id=os.getenv("LINE_user_id")

!pip install line-bot-sdk
import linebot
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
line_bot_api=LineBotApi(TOKEN)

from datetime import datetime

T_ext=f"{now}\nF&G:{index_str}"
messages=TextSendMessage(text=T_ext)
line_bot_api.push_message(user_id, messages=messages)
