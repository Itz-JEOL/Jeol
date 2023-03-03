from os import path, getenv
import time
import re
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('ADMINS', '').split()]
    
var = Config()
