import requests

BOT_TOKEN = "8282453071:AAEHHv2wwL5aEUnLzCeFrGJN3XRjj4yWyWQ"
CHAT_ID = "-1003284337293"
FILE_PATH = "/Users/izarhairulanam/Documents/Izar/project_selenium/allure-report.zip"  # file dari automation kamu
WEBHOOK_URL_DISCORD = "https://discord.com/api/webhooks/1442783839758844006/db_A-kAkWS16kR05oKazGMdslUgYUzTHJnn9dhMItyfb70BCbWVWkYyunGXotlC-A2_f"
URL_TELEGRAM = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

def send_report_to_telegram():
    try:
        with open(FILE_PATH, "rb") as file:
            response = requests.post(
                url=URL_TELEGRAM,
                data={"chat_id": CHAT_ID},
                files={"document": file}
            )
        print("\nProses Send To Telegram......")
        print("=====Response Code=====")
        print("Status:", response.status_code)
        print("\n=====Log=====")
        print("Log:", response.text)
        return response.status_code
    except Exception as e:
        print(e)
        return False


def send_report_to_discord():
    try:
        with open(FILE_PATH, "rb") as file:
            response = requests.post(
                url=WEBHOOK_URL_DISCORD,
                files={"document": file},
                data={"content": "📦 Automation Report - Allure"}
            )
        print("\nProcess Send To Discord......")
        print("=====Response Code=====")
        print(f"Response Code: {response.status_code}")
        print("\n=====Log=====")
        print(f"Log: {response.text}")
        return response.status_code
    
    except Exception as e:
        print(e)
        return False


def send_report_to_telegram_or_discord():
   if send_report_to_telegram():
       print("Berhasil Kirim Ke Telegram")
   else:
       print("Gagal Kirim ke Telegram")
       print("Kirim Report ke Discord")
       send_report_to_discord()