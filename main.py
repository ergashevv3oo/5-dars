from telebot import TeleBot
import asyncio
import aiohttp

TOKEN = "8346514878:AAFk2uFDOhW7zuDm1FR1J4vJbLftj6y536A"
API = "75ba2f52bbe1e2b8b1b5e94b96030d59"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Shahar nomini yozing")

@bot.message_handler(func=lambda x: True)
def get_weather(message):
    asyncio.run(weather(message))

async def weather(message):
    city = message.text
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                bot.send_message(message.chat.id, "Shahar topilmadi")
                return

            data = await response.json()
            temp = data['main']['temp']
            bot.send_message(
                message.chat.id,
                f" {city} harorati: {temp}"
            )

if __name__ == "__main__":
    bot.infinity_polling()
