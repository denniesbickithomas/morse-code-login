# Copy this file to config.py and fill in your own values.
# config.py is gitignored, so your secrets never reach GitHub.

# Telegram bot (alerts when an unknown face is detected)
BOT_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-telegram-chat-id"

# Email alerts (optional, used by attachem.py)
# Use a Gmail App Password, not your normal account password.
EMAIL_USER = "you@example.com"
EMAIL_APP_PASSWORD = "your-app-password"
ALERT_EMAIL_TO = "recipient@example.com"

# Twilio SMS (optional, currently commented out in the code)
TWILIO_ACCOUNT_SID = "your-twilio-sid"
TWILIO_AUTH_TOKEN = "your-twilio-auth-token"
