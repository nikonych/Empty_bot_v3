from aiogram import Dispatcher, Router, F

from config import Config
from .admin import admin_router
# from .admin import admin_router
from .errors import errors_router
from .user import user_router


def register_all_routes(dp: Dispatcher, config: Config):
    master_router = Router()

    dp.include_router(master_router)
    dp.include_router(errors_router)

    # admin_router.message.filter(F.from_user.id.in_(config.tg_bot.admin_ids))
    # user_router.message.filter(F.chat.id > 0)
    # admin_router.message.filter(F.chat.id > 0)

    master_router.include_router(user_router)
    master_router.include_router(admin_router)
    # master_router.include_router(admin_router)
