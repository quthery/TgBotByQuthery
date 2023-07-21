from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
import webbrowser
from kbs import kb_client

token = "6192287978:AAG9X4Fw0K4mqLg5_k7YYJgq8T3rHm4btrI"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer("qq", reply_markup=kb_client)


@dp.message_handler(commands=["cancel"])
async def cmd_canel(msg: types.Message) -> None:
    await msg.answer("poka(", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=["help"])
async def cmd_start(msg: types.Message) -> None:
    help_message = "👋 почти все команды\n\n" \
                   "✨ /start - открыть ReplyKeyboard\n" \
                   "❌ /cancel - KeyboardRemove\n" \
                   "❓ /help - получить информацию о доступных командах\n" \
                   "🎥 /toxis - Кружок Toxis'a \n" \
                   "🌟 /sigma - sigmaface\n" \
                   "🔗 /maryday - Никитосик\n\n" \
                   "🎉 привет вопрос по механике доты...\n\n" \
                   "🚀 узнай file_id своего стикера отправив мне его!"
    await msg.answer(help_message)


@dp.message_handler(commands=["toxis", "toxi$"])
async def toxis(msg: types.Message) -> None:
    videos = ['video1.mp4', 'video2.mp4', 'video3.mp4', 'video.mp4']
    random_videos = random.sample(videos, k=1)

    for video in random_videos:
        video_note = open(video, 'rb')
        await bot.send_video_note(msg.chat.id, video_note)


@dp.message_handler(commands=["sigma", 'sigmaface', 'takesigma'])
async def sigmaface(msg: types.Message) -> None:
    file = open("sigma.gif", 'rb')

    await msg.answer_document(file)
    file.close


@dp.message_handler(commands=["maryday", "pro"])
async def maryday(msg: types.Message) -> None:
    if msg.get_command() == "/maryday":
        url = "https://www.twitch.tv/mary_day"
    elif msg.get_command() == "/pro":
        url = "https://www.twitch.tv/pro"

    webbrowser.open(url)


@dp.message_handler(content_types="sticker")
async def handle_text(msg: types.Message):
    await msg.answer(msg.sticker.file_id)


stickers = ["CAACAgIAAxkBAAICoGS6exg30I6flr95A1gTgwFSDD3YAAI2JwAC7xDJSpYkW3Y1rwfBLwQ",
            "CAACAgIAAxkBAAICnmS6exV5nyLe_fU5oDfytjssxVN5AALcJwAC-qmpSZod2GFAr2_9LwQ",
            "CAACAgIAAxkBAAIComS6ey4WscqOJk8XwV6F4ipt0fEcAAIPIgACr70YSUBK5NQTLTuTLwQ",
            "CAACAgIAAxkBAAICpGS6ezZxuWlhMYiwRX8t1l76eK4qAAKLJQACHnTRSy-XHXirzFGTLwQ"]

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(msg: types.Message):
    random_sticker = random.choice(stickers)
    if "вопрос по механике" in msg.text.lower():
        await msg.answer_sticker(random_sticker)


@dp.message_handler()
async def wordik(msg: types.Message) -> None:
    await msg.answer("че сказал??😡😡😡")


@dp.message_handler(content_types="photo")
async def photo_pikcha(msg: types.Message) -> None:
    await msg.answer("Норм пикча")


if __name__ == "__main__":
    executor.start_polling(dp)
