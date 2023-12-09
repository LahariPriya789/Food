import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://recipes.timesofindia.com/'
response = requests.get(url)
# print(response)

page_source = response.content
jsoup = BeautifulSoup(page_source)

body = jsoup.find('div',attrs = {'class':'musttrysec clearfix'})
result = body.find_all('div', attrs= {'class':'mustTry_left recipemainli'})

# print(result)
final_result = []
for div in result:
    dummy = dict()
    result_div = div.find('div', attrs={'class': 'caption clearfix'})
    if result_div:
        a = result_div.find('a')
        span_time = result_div.find('span',attrs = {'class':'duration'})
        # print(span_time)
        span_type = result_div.find('span',attrs = {'class':'vegnonveg'})
        child = span_type.find('span')['class'][0] if span_type else None
        # print(span_type)

        name = a.text
        link = a['href']
        time = span_time.text if span_time else None
        type = child

        dummy['Name'] = name
        dummy['Link'] = link
        dummy['Duration'] = time
        dummy['Veg or Nonveg'] = type

        final_result.append(dummy)
print(final_result)

df = pd.DataFrame(final_result)
# df.to_csv('D:\\$PYTHON\\Food .csv', index=False)
