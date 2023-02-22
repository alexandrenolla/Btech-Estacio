from bs4 import BeautifulSoup
import requests, re
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome)

scope = ['https://www.googleapis.com/auth/spreadsheets']
key = {"type": "service_account", "project_id": "taco-bell-306614",
       "private_key_id": "6f15f7490d00a7c3d6d47bfc20721e8a835367a0",
       "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDD206eJ3an4Uew\n0gVZ56Q1rPUgXqwXDQUkhbbk6rOB7ancApFpSX7yfJnXc1G/A2Q9p0d31MOY2o/h\nyEPExbnVhl2i8Aaz3eG49ZwaZ+QtXDkM1sgVD4dLHihuqKDXoW90Rn43S4MhiBcr\ni+DCGqv7Je9oKzhr4SQEYK8BJHSEBcYc06aRJLgJgA5EjfhMbggDf1xqNkPiQVWy\nrdnUvZK5QEGr253NILPT9F+iUw4SwmEd95bPtsBamVvPAL6d0ejtpC9HTsbkNf9x\n7mjpCko4mcjfFHqUo9iQ2DGZQ3/JTK2Ti8njzus/uoCUbt9ziipyr3/0poQlhBSt\nubJU9n3PAgMBAAECggEAV2cipfyJfLDRu+x1u+HeS5/UQm5NUPob/ej4Lh85HXXw\ntACnYLuOPetyAg5yABKk5MimYake4rNCu2kSKRlt7YaJeeGwtAsEJPTihXwwfTen\nM/4TiyaDY3fhZkS1hpUB9ntQ7x8xNUEUyfehxS1+61TKCowjIS13U8bLwnBA2Pss\nyT2G+Nu8Mh+rBjtEpB67HFLq1EvLKu0e0QbybQyZyMx6VO2PbMWzGwbfQWkHk1g2\n4tPCK6riu7TR3CANsGHEqTfwopsfte4JYPcQBo4d4cus04/+vx1qykFOCcRBrCUS\nhIzSJt3iRmB5+RpOd21UW4+WI3LQL/uabT9YZE4kbQKBgQDiM17pwpEyx0Jr85sW\n/5N79RQUKBL0ItjhOopil+669IOrVEwDB0rzOoeoc6TbfDvEtc5cHvm6bJo4G89L\na71PwsxlvfmRzHMoluCRcth3QrwHsXLNc+P0E1pgOY1XR3/cjSu8jF6kliEWF6Yn\nOTUeKZ1m+T73JljQwi/8vsicbQKBgQDdqJVaun+/ItOnUK3hPWsoC9zm0OfZ+L9j\ns4bOWod4iOSqvf3dh8l0hxz69uuQ+YR1xRwfEyHmbRjG5jHA64sV3YZw2Up5JNuq\nPH66J66Dg03Wiu3N7NZfHc4ib72NAw+Bbl5q+iNY8PUZHxwCjJH2mbJe+x/z8dpV\ni8D65ttlqwKBgDIiCo4qlj231evREPV27XwSpEGXZCQBuSmp7NPPMpTy7l/Bjhs5\nuY3Q0hIul0Ih9akyVisqnlSID2ISH85qcYnE9cIy6aY7tuYvElSKLJm6C6x00qng\nXoxQ4b3j44SNjzQVgbUHM06tC2Y3FZcp4bDurjkNUrw6HoMeFr6glhu9AoGAILgj\n49KnzMUNTSNhp1/zk2O85e1sbAaF6ee0PH2shaRfbLzC3pKOsD7Jjlooh6vtW50O\n+59NX8A26hVMvteGHmIm2D2a+qrwKf7oDf6RiiQ1tzemxsDxG/VAWmD4L/qFrWtn\nUI8/7H8VDvJCpjWtziL963tSSiYnPn10rRSqyiUCgYEAwh56lDCQwNrU7/+eezHj\nUBWYAidcCI16eBWGg/HDW82FYqTg9CsOTFNcPKKKbA06r/AOl3mD7w4M4AqfBKn4\n5bwNtZ+vXFLWl1U5MBF/FosEq/tnzEFuzM0t7fKeaZQAoUh1GcwkXIQAjyr5O1QK\nzDNhKpeQxtIVEZLOKT30IF4=\n-----END PRIVATE KEY-----\n",
       "client_email": "taco-bell@taco-bell-306614.iam.gserviceaccount.com", "client_id": "106206877208872617723",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/taco-bell%40taco-bell-306614.iam.gserviceaccount.com"}

credentials = None
credentials = service_account.Credentials.from_service_account_info(key, scopes=scope)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

startTime = datetime.now()
sheetID = '1LgUVJHHp7soOwp8mb-cXodKappHLr0HOjV9rTEWilj0'

d = {'Date': [], 'Section': [], 'Headline': [], 'Link': [], '1st Paragraph': []}
tb = pd.DataFrame(data=d)

links = []
urls = {'commercial real estate': 'https://www.bizjournals.com/news/commercial-real-estate/',
        'commercial real estate construction': 'https://www.bizjournals.com/news/commercial-real-estate/construction',
        'commercial real estate brokerages': 'https://www.bizjournals.com/news/commercial-real-estate/cre-brokerages',
        'commercial real estate developers': 'https://www.bizjournals.com/news/commercial-real-estate/cre-developers',
        'commercial real estate retail development': 'https://www.bizjournals.com/news/commercial-real-estate/retail-development',
        'commercial real estate leed': 'https://www.bizjournals.com/news/commercial-real-estate/leed',
        }

linha = 0
for url in urls:
    driver.get(urls[url])
    lis = [i for i in driver.find_element(By.XPATH, '//*[@id="NewsRiver"]/div').find_elements(By.TAG_NAME, 'li') if
           i.text != '']
    for li in lis:
        try:
            data = li.find_element(By.TAG_NAME, 'span').text.split(',')
            data = ''.join([' '.join([data[0].split()[0][:3], data[0].split()[1]]), data[1]])
            link = li.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links += [link]
            header = li.find_element(By.TAG_NAME, 'h2').text
        except:
            continue

    tb.loc[linha, 'Date'] = data
    tb.loc[linha, 'Headline'] = header
    tb.loc[linha, 'Section'] = url
    tb.loc[linha, 'Link'] = link
    linha += 1

linha = 0
for link in links:
    driver.get(link)
    paragrafo = driver.find_element(By.XPATH,
                                    '//*[@id="v-article-content"]/div[1]/div/div/div[1]/div[1]/div[5]/div[2]/p[1]').get_attribute(
        "textContent")

    tb.loc[linha, '1st Paragraph'] = paragrafo
    linha += 1

tb = tb.fillna('No Data')

# Grab the column with the links from the news
result = sheet.values().get(spreadsheetId=sheetID, range='Biz Journals!D:D').execute()

# Grab the links from the news and transform into pandas table.
gsheet = result.get('values', [])
gsheet = pd.DataFrame(data=gsheet)

# Grab the total lines of the table with the links + 1 and create a string
last = 'Biz Journals!A' + str(len(gsheet) + 1)  # Editar

# Remove duplicates between pandas and panda's gsheets
for i in range(1, len(tb)):
    a = tb.loc[i]['Link']
    if a in gsheet.values:
        tb = tb.drop(i, axis=0)

# Remove duplicate infos inside pandas table
tb = tb.drop_duplicates(subset=['Link'])

# Update the gsheets with the table collected
sheet.values().update(spreadsheetId=sheetID,
                      range=last,
                      valueInputOption='USER_ENTERED',
                      body=dict(majorDimension='ROWS',
                                values=tb.values.tolist())).execute()

print('Biz Journals done in: ' + str(datetime.now() - startTime))