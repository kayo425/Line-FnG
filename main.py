import os
import fear_and_greed
from datetime import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage

# --- 設定（GitHubの金庫から値を受け取る） ---
TOKEN = os.getenv("LINE_TOKEN")
user_id = os.getenv("LINE_user_id")

# --- データの取得と時間の計算 ---
index = fear_and_greed.get().value
index_str = f"{index:.1f}"
now = datetime.now().strftime("%Y/%m/%d(%a) %H:%M")

# --- LINE送信の実行 ---
T_ext = f"{now}\nF&G:{index_str}"
line_bot_api = LineBotApi(TOKEN)
messages = TextSendMessage(text=T_ext)
line_bot_api.push_message(user_id, messages=messages)
