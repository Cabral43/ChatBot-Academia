from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str=os.getenv("DATABASE_URL")
    TWILIO_ACCOUNT_SID: str=os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN: str=os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER: str=os.getenv("TWILIO_WHATSAPP_NUMBER")

    class Config:
        case_sensitive = True

settings = Settings()