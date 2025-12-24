import subprocess
from utils.notifier import send_report_to_telegram
from utils.notifier import send_report_to_discord
from utils.notifier import send_report_to_telegram_or_discord

def run_pytest_automation():
    subprocess.run(["pytest", "-s", "-v", "tests/test_sauce_demo.py", "--alluredir=allure-results"])

def generate_report_allure():
    subprocess.run(["allure", "generate", "--single-file", "allure-results", "-o", "allure-report"])

def generate_report_allure_to_zip():
    subprocess.run(["zip", "-r", "allure-report.zip", "allure-report"])


run_pytest_automation()
generate_report_allure()
generate_report_allure_to_zip()
# send_report_to_telegram()
# send_report_to_discord()
send_report_to_telegram_or_discord()
