from aiogram.filters.command import Command
from aiogram import types
from aiogram import Router
from sqlalchemy.exc import IntegrityError
from utils.root_me import scribe_root_me
from database.db import get_db
from database.user_dao import UserDAO
from states.user_states import UserRegisteryForm
common_router = Router()
from aiogram.fsm.context import FSMContext


# Хэндлер на команду /start
@common_router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Отправь мне свое ФИО.")
    await state.set_state(UserRegisteryForm.full_name)
    
    
@common_router.message(UserRegisteryForm.full_name)
async def get_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(full_name=fullname)
    await message.reply("Скиньте ссылку вашего профиля в https://www.root-me.org/")
    await state.set_state(UserRegisteryForm.root_me_nickname)


@common_router.message(UserRegisteryForm.root_me_nickname)
async def save_user(message: types.Message, state: FSMContext):
    root_me_link = message.text
    root_me_nickname = scribe_root_me(root_me_link)
    user_form_data = await state.get_data()
    try:
        with get_db() as db:
            user_dao = UserDAO(db)
            fullname = user_form_data.get("full_name")
            print(fullname)
            username = message.from_user.username
            user_dao.create_user(username, fullname, root_me_nickname)
            await message.reply('Запись пользователя в БД сохранена!')
    except IntegrityError:
        await message.reply("Ошибка сохранения пользователя в БД")