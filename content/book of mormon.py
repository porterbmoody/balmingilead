#%%

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/bcbooks/scriptures-json/refs/heads/master/book-of-mormon.json'
resp = requests.get(url)
data = json.loads(resp.text)

df = pd.json_normalize(data)

df_bom = pd.DataFrame()
book_titles = []
chapter_numbers = []
reference_numbers = []
chapters_verses = []
verse_references = []
verses = []
chapters = []

for i, book in enumerate(data['books']):
    for chapter in book['chapters']:
        # chapters.append(chapters)
        # chapters_verses.append(chapter['verses'])
        for i, chapter_verse in enumerate(chapter['verses']):
            # print(chapter_verse)
            book_titles.append(book['book'])
            chapter_numbers.append(chapter['chapter'])
            verse_references.append(chapter_verse['reference'])
            verses.append(chapter_verse['text'])
            # for verse in chapter_verses:
                # reference_numbers.append(chapter['reference'])
                # verse_references.append(verse['reference'])
# print(verse_references)
# print(verses)

df_bom = (pd.DataFrame({'book_title':book_titles,'chapter_number':chapter_numbers,'verse_reference':verse_references, 'verse':verses}))
df_bom.to_csv('data.csv',index=False)

# df_bom = (pd.DataFrame({'book_titles':book_titles,'chapter_numbers':chapter_numbers,'reference_numbers':reference_numbers,'reference':verse_references,'verse':verses}))

df_bom['word_count'] = df_bom['verse'].apply(lambda x: len(x.split()))
# df_bom.to_csv('data.csv',index=False)
df_bom

#%%
df_bom.groupby('book_title').agg({'word_count': 'sum'}).reset_index()


# %%
df_grouped = df_bom.groupby('book_title')['word_count'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['book_title'], df_grouped['word_count'], color='skyblue')
plt.xlabel('Book Titles')
plt.ylabel('Total Word Count')
plt.title('Total Word Count by Book in the Book of Mormon')
plt.xticks(rotation=45, ha='right')
plt.show()


#%%
import re

pattern = r'\b(Christ|Savior|Redeemer|Almighty|Almighty God|Alpha and Omega|Being|Beloved|Beloved Son)\b'
# pattern = r'\b(Christ)\b'

df_bom['christ_references'] = df_bom['verse'].str.count(pattern, flags=re.IGNORECASE)
df_grouped = df_bom.groupby('book_title').agg({'christ_references': 'sum'}).reset_index()

# total_references = df_bom['christ_references'].sum()

# print(f"Total references to Christ-related terms: {total_references}")
df_grouped

#%%

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['book_title'], df_grouped['christ_references'], color='skyblue')
plt.xlabel('Book Title')
plt.ylabel('Total Word Count')
plt.title('Total Christ References in the Book of Mormon')
plt.xticks(rotation=45, ha='right')
plt.show()



#%%

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df_grouped = df_bom.groupby('book_title')['word_count'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['book_title'], df_grouped['word_count'], color='skyblue')
plt.xlabel('Book Title')
plt.ylabel('Total Word Count')
plt.title('Total Word Count by Book in the Book of Mormon')

plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.xticks(rotation=45, ha='right')
plt.show()
#%%

df_grouped = df_bom.query('book_title == "Alma"').groupby('chapter_number').agg({'word_count': 'sum'}).reset_index()
df_grouped

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['chapter_number'], df_grouped['word_count'], color='skyblue')
plt.xlabel('chapter')
plt.ylabel('Total Word Count')
plt.title('Total Word Count by chapter in alma')

plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.xticks(rotation=45, ha='right')
plt.show()


#%%

df_grouped = df_bom.groupby(['book_title','chapter_number']).agg({'word_count': 'sum'}).reset_index()
df_grouped['combined'] = df_grouped['book_title'] + df_grouped['chapter_number'].astype(str)
df_grouped


import matplotlib.ticker as ticker

plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['combined'], df_grouped['word_count'], color='skyblue')
plt.xlabel('chapter')
plt.ylabel('Total Word Count')
plt.xticks(rotation=75, ha='right', fontsize=10)

plt.title('Total Word Count by chapter')

plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.xticks(rotation=45, ha='right')
plt.show()


#%%

plt.barh(df_grouped['combined'], df_grouped['word_count'], color='skyblue')
plt.xlabel('Total Word Count')
plt.ylabel('Chapter')
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.show()


