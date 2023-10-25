import os

env = os.getenv("env", "development")


if env == "test":
    base_url = os.getenv("BASE_URL", "http://localhost:8000/api")

    
elif env == "production":
    base_url = os.getenv("BASE_URL", "https://api.plugin.webbot.chat/api")



elif env == "development":
    base_url = os.getenv("BASE_URL", "https://api.plugindev.webbot.chat/api")








