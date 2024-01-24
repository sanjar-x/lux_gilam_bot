from aiogram import Bot, Dispatcher, types


bot = Bot(token="6953507113:AAFICKZN7nEet4pkmpovCt9zqRR3iVOKPH8", parse_mode="HTML")

dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Привет, {user.full_name}!\n"
        f"Вот твои данные:\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username}\n"
        f"Имя: {user.first_name}\n"
        f"Фамилия: {user.last_name}"
    )


# "6953507113:AAFICKZN7nEet4pkmpovCt9zqRR3iVOKPH8"
