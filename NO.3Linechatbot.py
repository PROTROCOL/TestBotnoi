from linebot import LineBotApi, WebhookHandler # type: ignore
from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, MessageAction, CarouselColumn, CarouselTemplate # type: ignore

# กำหนด Channel Access Token และ Channel Secret
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

def send_text_message(user_id, text):
    line_bot_api.push_message(user_id, TextSendMessage(text=text))

def send_quick_reply(user_id):
    quick_reply = QuickReply(items=[
        QuickReplyButton(action=MessageAction(label="Option 1", text="Option 1")),
        QuickReplyButton(action=MessageAction(label="Option 2", text="Option 2"))
    ])
    line_bot_api.push_message(user_id, TextSendMessage(text='Choose an option', quick_reply=quick_reply))

def send_carousel_message(user_id):
    carousel_template = CarouselTemplate(columns=[
        CarouselColumn(text='Option 1', actions=[MessageAction(label='Select', text='Option 1')]),
        CarouselColumn(text='Option 2', actions=[MessageAction(label='Select', text='Option 2')])
    ])
    line_bot_api.push_message(user_id, template_message) # type: ignore

# ทดสอบฟังก์ชัน
user_id = 'USER_ID'  # ระบุ ID ของผู้ใช้
send_text_message(user_id, 'Hello!')
send_quick_reply(user_id)
send_carousel_message(user_id)
