from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests
import json
import createHtml
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths to the directories
testdata_dir = os.path.join(script_dir, "../testData")
img_dir = os.path.join(script_dir, "../img")

# Ensure both directories exist
os.makedirs(testdata_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

# Define the file paths
json_file_path = os.path.join(testdata_dir, "data.json")
chromedriverFile = os.path.join(testdata_dir, "chromedriver.exe")
img_file_path = os.path.join(img_dir, "image.jpg") 

#Global Variables
#CHROME_DRIVER_PATH = "D:\\projects\\Automation\\Website Automation\\testData\\chromedriver.exe"
CHROME_DRIVER_PATH = chromedriverFile
WEBSITE_URL = "https://variety.com/v/film/news/"  # Example website
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(15)

data = {"title":"","caption":"","ImgUrl":"", "url":""}



def detect_new_articles():
    """
        For Detecting new articles in web page
    """
    driver.get(WEBSITE_URL)
    driver.maximize_window()
    driver.refresh()  
    time.sleep(3)  # Wait for the page to load
    title = driver.find_element(By.XPATH,"//h3[@id='title-of-a-story']").text
    jsonData = loadFromJsonFile()
    #Trigger for new articles
    if str(jsonData['title']) != title:        
        driver.find_element(By.XPATH,"//h3[@id='title-of-a-story']").click()
        data['title'] = title
        time.sleep(3)
        return True,str(jsonData['title']),title
    else:
        return False,str(jsonData['title']),title

def fetch_article_content():
    """
        Fetching all the paragraphs on article
    """
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    paragraphs = soup.find_all('p')
    return " ".join([p.text for p in paragraphs])

# Generate caption from the content
def generate_caption(article_content):
    """
        Generating the caption
    """
    data["caption"] = article_content[:200] + "..." 
    return article_content[:200] + "..."  # Truncate to 200 characters

def getImage():
    """
        Get the image from article and store in img folder
    """
    try:
        image_element = driver.find_element(By.XPATH,"//figure/div/div/img[@class='c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto']")
        # Extract the image URL
        image_url = image_element.get_attribute("srcset")

        # Download the image using requests
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save the image locally
            with open(img_file_path, "wb") as file:
                file.write(response.content)
        else:
            print("Failed to download the image")
    except Exception as error:
        print(error)


def shorten_url():
    """
    Shortens the given URL using the TinyURL API.
    """
    try:
        url = driver.current_url
        # TinyURL API
        api_url = f"http://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data['url'] = response.text
            return response.text
        else:
            print("Failed to shorten URL")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def saveToJsonFile():
    """
        Save the data title caption, url of article to json file for comparing new article and showing in index.html
    """
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)

def loadFromJsonFile():
    """
        Retrieve data from json file to loaded_data variable
    """
    with open(json_file_path, "r") as file:
        loaded_data = json.load(file)
        return loaded_data

def openhtmlFile():
    """
        Open index.html and show image and caption with shorten url
        Close the web page after 10 seconds for checking new article
    """
    jsonData = loadFromJsonFile()
    createHtml.createHtmlFile(jsonData['caption'],jsonData['url'])
    driver.switch_to.new_window('tab')
    #open index.html and paste local link here
    driver.get("file:///D:/projects/Automation/Website%20Sharing/index.html")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(10)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])