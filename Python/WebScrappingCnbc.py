from bs4 import BeautifulSoup
import requests, re
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

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

d = {'Date': [], 'Headline': [], '1st Paragraph': [], 'Link': []}
tb = pd.DataFrame(data=d)

counter = 1

while True:
    try:
        html_text = requests.get('https://www.cnbc.com/real-estate/').text
        break
    except:
        pass
soup = BeautifulSoup(html_text, 'lxml')

for div in soup.find_all('div', class_='Card-card'):
    try:
        date = div.find('span', class_='Card-time').text
    except:
        date = 'No Data'
    try:
        headline = div.find('div', class_='Card-eyebrowContainer').text
    except:
        headline = 'No Data'
    try:
        paragraph = div.find('a', class_="Card-title").text
    except:
        paragraph = 'No Data'
    try:
        link = div.find('a', class_='Card-title')['href']
    except:
        pass
    if 'ago' in date:
        date = str(datetime.now()).split()[0]
    try:
        date = '/'.join(
            date.split(',')[1].replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').split())
    except:
        pass

    tb.loc[counter, 'Date'] = date
    tb.loc[counter, 'Headline'] = headline
    tb.loc[counter, '1st Paragraph'] = paragraph
    tb.loc[counter, 'Link'] = link
    counter += 1
tb = tb.fillna('No Data')

result = sheet.values().get(spreadsheetId=sheetID, range='CNBC!D:D').execute()
gsheet = result.get('values', [])
gsheet = pd.DataFrame(data=gsheet)
last = 'CNBC!A' + str(len(gsheet) + 1)
for i in range(1, len(tb)):
    a = tb.loc[i]['Link']
    if a in gsheet.values:
        tb = tb.drop(i, axis=0)
tb = tb.drop_duplicates(subset=['Link'])
sheet.values().update(spreadsheetId=sheetID,
                      range=last,
                      valueInputOption='USER_ENTERED',
                      body=dict(majorDimension='ROWS',
                                values=tb.values.tolist())).execute()
print('CNBC done in: ' + str(datetime.now() - startTime))