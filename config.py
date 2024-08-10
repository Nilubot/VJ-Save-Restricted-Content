import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21049692"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b41eec918ed650258ef34a08bed230e7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://is46bfo8on:0gwvyBfm0NeRpaiI@cluster0.6pyctxp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
