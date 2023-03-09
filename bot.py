# TOKEN FOR BOT = '6131361529:AAGykrRlK5ujAxBELMSqv72lVzRVejYcFFM'

from aiogram import Bot, Dispatcher, executor, types
from driver_class import driver_detection
import os
import sys


bot = Bot(token='5689474523:AAFRW7UTMOnl9tgYPwqzWmLisR5j_ZhRwNg')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Пришлите мне фото или видео, и я попробую определить, спит водитель или нет.'
    
    await message.reply(text)

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    user_id = message.from_user.id
    ph_name='yolov5/runs/detect/'+str(user_id)+'/'+str(user_id)+'.jpg'
    
    await message.photo[-1].download(ph_name)
    


    
    text = driver_detection(ph_name)
    with open(ph_name, 'rb') as f:
        # await bot.send_photo(chat_id=message.chat.id, photo=f)  #Доработать на будущее вывод фото с bbox
        await bot.send_message(user_id, text)




@dp.message_handler(content_types=['video'])
async def handle_docs_video(message):
    user_id = message.from_user.id
    video_name=str(user_id)+'.mp4'

    await message.video.download(video_name)
    
    os.system(f'python yolov5/detect.py --source {video_name} --name {user_id}')
    
    with open('yolov5/runs/detect/'+str(user_id)+'/'+str(video_name), 'rb') as video:

        video_file = types.InputFile(video)
        await bot.send_video(chat_id=message.chat.id, video=video_file)






if __name__ == '__main__':
    executor.start_polling(dp)


