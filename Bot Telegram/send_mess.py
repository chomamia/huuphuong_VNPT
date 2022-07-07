import telegram
import random
def send_test_message():
    telegram_notify = telegram.Bot("5547536251:AAGq1De6wC2j_nzjILFYBE-LhslrwNYpRXo")
    message = input()
    
    telegram_notify.send_message(chat_id="-626545711", text=message,
                                parse_mode='Markdown')
send_test_message()