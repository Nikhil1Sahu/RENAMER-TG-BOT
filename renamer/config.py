import os
import logging
logger = logging.getLogger(__name__)

class Config:
    API_ID = 18466881
    API_HASH = "8c8ca14ad8e416ce4e6ea717db7ec6af"
    OWNER_ID = 5565120414
    AUTH_USERS = [8190474898, 1918675169, OWNER_ID]
    BANNED_USERS = []
    BOT_TOKEN = "8483246378:AAFACrQv9a9rSfLjejyIAClK2b8iokIeARo"
    BOT_PASSWORD = None
    CUSTOM_CAPTION = None
    FORCE_SUB = "network_of_kingdom"
    DATABASE_URL = "mongodb+srv://nikhilsahu7j:dTQKfvo0jABOYKOu@cluster0.n2csgvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    try:
        TIME_GAP = None
    except:
        TIME_GAP = None
        logger.warning("Give the timegap in seconds. Dont use letters 😑")
    TIME_GAP_STORE = {}
    try:
        TRACE_CHANNEL = -1002731391701
    except:
        TRACE_CHANNEL = None
        logger.warning("Trace channel id was invalid")
