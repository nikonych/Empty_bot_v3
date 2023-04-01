from aiogram import Router
from aiogram.enums import ContentType
from aiogram.filters import Text

from utils.misc.kb_config import profile_btn
from . import profile

profile_router = Router()

profile_router.message.register(profile.profile_handler, Text(text=profile_btn))
profile_router.callback_query.register(profile.profile_handler, Text(text='back_profile'))


