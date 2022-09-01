import pandas as pd
from selenium import webdriver
import json
import os

# Global Variables    
PDF_savepath = './Downloads' # Edit here to change save directory
webdriver_path = './chromedriver' # Edit this to the chrome webdriver location. Visit https://chromedriver.chromium.org/downloads and https://www.google.com/chrome/ to download webdriver and chrome browser.
reference = pd.read_csv('reference.csv') # List of pages to be archived

# Download function
def download(url,name,PDF_savepath = PDF_savepath,webdriver_path = webdriver_path):
    '''
    Download the webpage and save as PDF to PDF_savepath.

    url:                    URL format string. The link to the page.
    name:                   String. Name of the downloaded file.
    PDF_savepath:           Directory format string. Where to store the downloaded file. Default to be specified in Global Variables.
    webdriver_saverpath:    Directory format string. Path to the webdriver. Default to be specified in Global Variables.
    '''
    # Specify download preferences
    chrome_options = webdriver.ChromeOptions()
    appState = {
        'recentDestinations': [
            {
                'id': 'Save as PDF',
                'origin': 'local',
                'account': ''
            }
        ],
        'selectedDestinationId': 'Save as PDF',
        'version': 2
    }
    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState), 
        'savefile.default_directory': PDF_savepath,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--kiosk-printing')
    # chrome_options.add_argument('-headless') # I don't know why headless mode doesn't work...
    # Start running the browser
    driver = webdriver.Chrome(webdriver_path, options=chrome_options) 
    driver.implicitly_wait(10)
    driver.get(url)
    driver.execute_script('window.print();')
    driver.close()
    # Rename
    os.chdir(PDF_savepath)
    files = filter(os.path.isfile, os.listdir(PDF_savepath))
    files = [os.path.join(PDF_savepath, f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))
    newest_file = files[-1]
    os.rename(newest_file, name +".pdf")

# Parse the list, feel free to modify to cope with desired category format
for i in range(len(reference)):
    url = reference.iloc[i]['url']
    name = reference.iloc[i]['name']
    download(url, name)
    print(name + ' downloaded')