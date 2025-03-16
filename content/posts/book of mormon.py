#%%

import requests
import json
import pandas as pd  

url = 'https://raw.githubusercontent.com/bcbooks/scriptures-json/refs/heads/master/book-of-mormon.json'
resp = requests.get(url)
data = json.loads(resp.text)

df = pd.json_normalize(data)
df


#%%
df_bom = pd.DataFrame()
book_titles = []
chapter_numbers = []
chapters = []

for i, book in enumerate(data['books'][0:2]):
    book_titles.append(book['book'])
    for chapter in book['chapters']:
        # chapters.append(chapters)
        chapter_numbers.append(chapter['chapter'])
        print(chapter)
        print(chapter['chapter'])



    # chapter_numbers.append(book['chapters'])
    # print(book['book'])
    # print(book['chapters'])
    # print(book['book'])
    # print(book)
    # print(i)

# book_titles
# chapters
# data['books']


