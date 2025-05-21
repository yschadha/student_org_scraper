from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options for headless run
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://sa.ucla.edu/RCO/public/search?q=tech'
driver.get(url)

time.sleep(5)

# Handle iframes
iframes = driver.find_elements(By.TAG_NAME, "iframe")
if iframes:
    driver.switch_to.frame(iframes[0])

# Scroll to bottom to load all dynamic content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Wait for cards to appear
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card') or contains(@class, 'row')]"))
    )
except:
    print("Club elements did not load in time.")
    print(driver.page_source)
    driver.quit()
    exit()

club_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') or contains(@class, 'row')]")

all_clubs_data = []

for club in club_containers:
    try:
        name_tag = club.find_element(By.XPATH, ".//div[starts-with(@class, 'row bold')]")
        club_name = name_tag.text.strip()
    except:
        club_name = None

    try:
        email_tag = club.find_element(By.XPATH, ".//a[starts-with(@href, 'mailto:')]")
        club_email = email_tag.text.strip().split("@")[0]
    except:
        club_email = None

    try:
        insta_tag = club.find_element(By.XPATH, ".//a[contains(@href, 'instagram.com')]")
        club_instagram = insta_tag.get_attribute("href")
    except:
        club_instagram = None

    try:
        signatories = club.find_elements(By.XPATH, ".//div[contains(@class, 'col-md-2')]")
        sigs = []
        for i in range(len(signatories)):
            if "Signatory" in signatories[i].text:
                if i + 1 < len(signatories):
                    sigs.append(signatories[i + 1].text.strip())
        if not sigs:
            sigs = ["None"]
    except:
        sigs = ["None"]

    if club_name or club_email or club_instagram:
        club_data = {
            "name": club_name,
            "email": club_email,
            "instagram": club_instagram,
            "signatories": sigs
        }
        all_clubs_data.append(club_data)

driver.quit()

# Print result
for club in all_clubs_data:
    print(club)
