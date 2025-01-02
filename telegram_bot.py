from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = '7862768565:AAHhyKcHzv4Cjjfs2BgNCc5Zj14nFrX4XCc'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id   
    user_name = update.effective_user.username  
    chat_id = update.effective_chat.id
    chat_title = update.effective_chat.title if update.effective_chat.type == 'group' else None 

    # Gửi tin nhắn trả lời
    await update.message.reply_text(
        f"ID Người Dùng: {user_id}\n"
        f"Tên Người Dùng: {user_name}\n"
        f"ID Nhóm: {chat_id}\n"
        f"Tên Nhóm: {chat_title if chat_title else 'Không có nhóm'}"
    )

def main():
    # Tạo ứng dụng bot
    application = ApplicationBuilder().token(API_TOKEN).build()

    # Thêm handler cho lệnh /start
    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
