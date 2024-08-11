ADMIN_ID = 745636044  # Доступ к апи телеграма, для всех ботов один
API_ID = 25483828  # -//-
BOT_TOKEN = '6379786228:AAGJu2K4df2pgCpxaE0Dti6gDnFPuxm2_aE'  # PINbot_Demo
CHANNEL = -1001860127735  # Как работает PINbot https://t.me/+9LcrUmCTHT41NmVk
LIST_ADMINS = [745636044, 1495761126]

BOTUSERNAME = 'PINbot_Demo'
LINKTOPINBOT = 'https://t.me/pinanybot'

LOGNAME = "Logs/PINbot_Demo.log"

# DataBase
DB_HOST = '127.0.0.1'
DB_USER = 'postgres'
DB_PASSWORD = '43288'
DB_DATABASE = 'PINbot_Demo'
DB_TABLE = 'datausers'

NAME_FOR_BASE = 'PINbot_Demo'

# Экспорт из базы в csv
CSV_FILE = 'PINbot_Demo_'
LIST_SUBJECTS = ["id", "user_id", "come_from", "inviter_code", "username", "first_name", "last_name", "date_of_use"]

# ------------
# Получить заголовки из базы
# COPY (SELECT * FROM datausers ORDER BY date_of_use DESC) TO '/home/kofesutra/12345.csv' WITH CSV DELIMITER ';' HEADER
