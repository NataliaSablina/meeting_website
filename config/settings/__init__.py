import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("BUILD_TYPE") == "DEV":
    from .development import *
elif os.getenv("BUILD_TYPE") == "PROD":
    from .production import *
else:
    print("Unknown settings, develop installed")
    from .development import *
