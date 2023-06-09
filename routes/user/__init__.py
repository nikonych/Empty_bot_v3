from aiogram import Router
from aiogram.filters import CommandStart

from . import start
from .profile import profile_router


user_router = Router()
# user_router.callback_query.register(start.back_to_start_handler)
# # user_router.callback_query.register(start.back_to_start_handler, text='back_in_menu')
# user_router.message.register(start.start_handler)
# user_router.message.register(start.start_handler, text='⬅️ Вернуться в меню')
user_router.message.register(start.start_handler, CommandStart())

# user_router.include_router(purchase_router)
# user_router.include_router(profile_router)
# user_router.include_router(tokens_router)
# user_router.include_router(help_router)
# user_router.include_router(rule_router)
