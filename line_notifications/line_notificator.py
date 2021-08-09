from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv
import os


class LineNotificator:
    def __init__(self):
        load_dotenv(verbose=True)
        self.line_channel_access_token = os.environ.get("CHANNEL_ACCESS_TOKEN")
        self.line_bot_api = LineBotApi(self.line_channel_access_token)
        self.user_id = os.environ.get("USER_ID")
    
    def send_message(self, msg):
        messages = TextSendMessage(text=msg)
        self.line_bot_api.push_message(self.user_id, messages=messages)


if __name__=="__main__":
    ln = LineNotificator()
    ln.send_message("test")

