from flask import Flask, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/clubs", methods=["GET"])
def scrape():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://sa.ucla.edu/RCO/public/search?category=Greek%20Life%20-%20Fraternities&type=Undergraduate')


    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    club_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'row bold')]")
    emails = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'mailto:')]")
    instas = driver.find_elements(By.XPATH, "//a[contains(@href, 'instagram.com')]")

    data = []
    for i in range(min(len(club_elements), len(emails), len(instas))):
        data.append({
            "name": club_elements[i].text.strip(),
            "email": emails[i].text.strip(),
            "instagram": instas[i].get_attribute("href")
        })

    driver.quit()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)
