from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from serial import Serial
from env import Env

bot = Bot(token=Env.TOKEN)
dp = Dispatcher(bot)
port = Serial(Env.PORT, 9600)


@dp.message_handler(commands='start')
async def _start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(Env.TURN_ON),
           types.KeyboardButton(Env.TURN_OFF))
    await msg.answer("Hi! You can use me to control your Arduino!",
                     reply_markup=kb)


@dp.message_handler(Text(equals=Env.TURN_ON))
async def _turn_on(msg: types.Message):
    kb = types.InlineKeyboardMarkup(resize_keyboard=True)
    for led in Env.LEDS:
        # port.write(bytes(str(Env.LEDS.index(led) + 1), 'utf-8'))
        # if port.read() == b'0':
        #     kb.add(types.InlineKeyboardButton(getattr(Env, led), callback_data='%s1' % led))
        kb.add(types.InlineKeyboardButton(getattr(Env, led), callback_data='%s1' % led))
    await msg.answer(Env.CHOOSE, reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.endswith('1'))
async def _turn_on_callback(c: types.CallbackQuery):
    i = Env.LEDS.index(c.data[0]) + 1
    port.write(bytes('%s1' % i, 'utf-8'))
    await c.message.edit_text(Env.TURNED_ON % getattr(Env, c.data[0]))


@dp.message_handler(Text(equals=Env.TURN_OFF))
async def _turn_off(msg: types.Message):
    kb = types.InlineKeyboardMarkup(resize_keyboard=True)
    for led in Env.LEDS:
        # port.write(bytes(str(Env.LEDS.index(led) + 1), 'utf-8'))
        # if port.read() == b'1':
        #     kb.add(types.InlineKeyboardButton(getattr(Env, led), callback_data='%s0' % led))
        kb.add(types.InlineKeyboardButton(getattr(Env, led), callback_data='%s0' % led))
    await msg.answer(Env.CHOOSE, reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data.endswith('0'))
async def _turn_off_callback(c: types.CallbackQuery):
    i = Env.LEDS.index(c.data[0]) + 1
    port.write(bytes('%s0' % i, 'utf-8'))
    await c.message.edit_text(Env.TURNED_OFF % getattr(Env, c.data[0]))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
