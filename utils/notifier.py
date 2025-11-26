import requests

BOT_TOKEN = "8282453071:AAEHHv2wwL5aEUnLzCeFrGJN3XRjj4yWyWQ"
CHAT_ID = "-1003284337293"
FILE_PATH = "/Users/izarhairulanam/Documents/Izar/project_selenium/allure-report.zip"  # file dari automation kamu
WEBHOOK_URL_DISCORD = "https://discord.com/api/webhooks/1442783839758844006/db_A-kAkWS16kR05oKazGMdslUgYUzTHJnn9dhMItyfb70BCbWVWkYyunGXotlC-A2_f"

def send_report_to_telegram():
    with open(FILE_PATH, "rb") as file:
        response = requests.post(
            url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
            data={"chat_id": CHAT_ID},
            files={"document": file}
        )
    print("\nProses Send To Telegram......")
    print("=====Response Code=====")
    print("Status:", response.status_code)
    print("\n=====Log=====")
    print("Log:", response.text)


def send_report_to_discord():
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
    


