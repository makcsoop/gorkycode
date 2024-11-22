import random

import tracemalloc
from aiogram import*
from aiogram.types import*
from aiogram.filters import Command,CommandStart

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7516736796:AAHyh9iC__5LbJj_QOXlRRFPQYQwm3BfX6Y'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

st:str=F.text
print(st)
url='https://i.pinimg.com/originals/fd/bd/bb/fdbdbbb5fa814d08a45576efc758095d.jpg'

def get_random_number() -> int:
    return random.randint(1, 100)

a:int=5

users={}



@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nДавайте сыграем в игру "Угадай число"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help'
    )
    if message.from_user.id not in users:
        users[message.from_user.id]={'in_game':False,
            'secret_number':None,
            'attempts':None,
            'total_games':0,
            'wins':0,
            'make_diff':0

        }


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        f'Правила игры:\n\nЯ загадываю число от 1 до 100,'
        f'а вам нужно его угадать\nВы имеете базово 5 попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n/diff - изменить сложность\n\nДавай сыграем?\n/secret'
    )
@dp.message(Command(commands='diff'))
async def process_diff_change(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer("Поменять сложность можно только не во время игры!")
    else:
        await message.answer("Выберите сложность:\nEasy🥱\nMedium😏\nHard🤩\nInsane😎\n\nНапиши свой выбор)")
        users[message.from_user.id]['make_diff']+=1
@dp.message(F.text.lower().in_(['easy','medium','hard','insane']))
async def process_change(message: Message):
    global a
    if (users[message.from_user.id]['make_diff']==1):
        if (message.text.lower()=='easy'):
            a+=5
            users[message.from_user.id]['make_diff'] -= 1
            await message.answer("Теперь у вас 10 попыток!")
        if (message.text.lower()=='medium'):
            a+=2
            users[message.from_user.id]['make_diff'] -= 1
            await message.answer("Теперь у вас 7 попыток!")
        if (message.text.lower()=='hard'):
            a+=0
            users[message.from_user.id]['make_diff'] -= 1
            await message.answer("Теперь у вас 5 попыток!")
        if (message.text.lower()=='insane'):
            a-=2
            users[message.from_user.id]['make_diff'] -= 1
            await message.answer("Теперь у вас 3 попытки!")
        if (message.text.lower()!='easy' and message.text.lower()!='medium' and message.text.lower()!='hard' and message.text.lower()!='insane'):
            await message.answer("Че?🙄")
    else:
        await message.answer("В данный момент вы не выбираете сложность!\nПропишите /diff, для выбора сложности")


@dp.message(Command(commands='stat'))
async def process_check_stat(message: Message):
    await message.answer(
        f'Всего игр сыграно: {users[message.from_user.id]['total_games']}\n'
        f'Побед: {users[message.from_user.id]['wins']}\n'
    )
@dp.message(Command(commands='secret'))
async def secret(message: Message):
    await message.answer("https://clck.ru/3EHFv9")
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        await message.answer(
            'Вы вышли из игры😥. Если захотите сыграть '
            'снова - напишите об этом'
        )
    else:
        await message.answer(
            'А мы и так с вами не играем😥. '
            'Может, сыграем разок?'
        )
@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра',
                                'играть', 'хочу играть']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = a
        await message.answer(
            'Ура!\nЯ загадал число от 1 до 100, '
            'попробуй угадать!'
        )
    else:
        await message.answer(
            'Пока мы играем в игру я могу '
            'реагировать только на числа от 1 до 100 '
            'и команды /cancel и /stat'
        )
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer(
            'Жаль😥 :(\n\nЕсли захотите поиграть - просто '
            'напишите об этом'
        )
    else:
        await message.answer(
            'Мы же сейчас с вами играем. Присылайте, '
            'пожалуйста, числа от 1 до 100'
        )
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer(
                'Ура!!!\n✨✨✨✨✨✨✨\nВы угадали число!\n\n'
                'Может, сыграем еще?'
            )
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Мое число меньше')
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Мое число больше')

        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли😥\n\nМое число '
                f'было {users[message.from_user.id]["secret_number"]}\n\nДавайте '
                f'сыграем еще?'
            )
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')
@dp.message()
async def process_other_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100'
        )
    elif users[message.from_user.id]['make_diff']==1:
        await message.answer("Че? Напиши нормально")
    else:
        print(st)
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )


if __name__ == '__main__':
    dp.run_polling(bot)