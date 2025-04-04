#%%

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

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
# df_bom.to_csv('data.csv',index=False)

# df_bom = (pd.DataFrame({'book_titles':book_titles,'chapter_numbers':chapter_numbers,'reference_numbers':reference_numbers,'reference':verse_references,'verse':verses}))

df_bom['word_count'] = df_bom['verse'].apply(lambda x: len(x.split()))
# df_bom.to_csv('data.csv',index=False)
df_bom


#%%
df_bom

import pandas as pd
pd.set_option('display.max_colwidth', None)

abraham_verses = df_bom[df_bom['verse'].str.contains('Abraham', case=False)]

abraham_verses = list(abraham_verses['verse_reference'])

abraham_verses




#%%
df_grouped = df_bom.groupby('book_title')['word_count'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(df_grouped['book_title'], df_grouped['word_count'], color='skyblue')
word_count = df_grouped['word_count']
plt.bar_label(word_count)
plt.xlabel('Book Titles')
plt.ylabel('Total Word Count')
plt.title('Total Word Count by Book in the Book of Mormon')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.savefig("Book of Mormon Images/word count by book.png") 

#%%

# pattern = r'\b(Christ|Savior|Redeemer|Almighty|Almighty God|Alpha and Omega|Being|Beloved|Beloved Son)\b'
# pattern = r'\b(Christ)\b'
pattern = r'\b(Almighty|Almighty God|Being|Beloved |Beloved Son|Christ|Christ Jesus|Christ the Son|Counselor|Creator|Eternal Father|Eternal God|Eternal Head|Eternal Judge|Everlasting Father|Everlasting God|Father|Father of heaven|Father of heaven and of earth|Founder of Peace|God|God of Abraham|God of Abraham, and Isaac, and Jacob|God of Abraham, and of Isaac, and the God of Jacob|God of Isaac|God of Jacob|God of miracles|God of nature|God of the whole earth|Good shepherd|Great Creator|Great Spirit|Head|Holy Child|Holy God|Holy Messiah|Holy One|Holy One of Israel|Holy One of Jacob|Husband|Immanuel|Jehovah|Jesus|Jesus Christ|Keeper of the gate|King|King of heaven|Lamb|Lamb of God|Lord|Lord God|Lord God Almighty|Lord God Omnipotent|Lord God of Hosts|Lord Jehovah|Lord Jesus|Lord Jesus Christ|Lord of Hosts|Lord of the Vineyard|Lord Omnipotent|Maker|Man|Master|Mediator|Messiah|Mighty God|Mighty One of Israel|Mighty One of Jacob|Most High|Most High God|Only Begotten of the Father |Only Begotten Son|Prince of Peace|Prophet|Redeemer|Redeemer of Israel|Redeemer of the world|Rock|Savior|Savior Jesus Christ|Savior of the world|Son|Son of God|Son of Righteousness|Son of the Eternal Father |Son of the Everlasting God|Son of the Most High God|Stone|Supreme Being|True and Living God|True Messiah|True Vine|Well Beloved|Wonderful)'

patterns = [
    'Almighty','Almighty God','Being','Beloved','Beloved Son','Christ','Christ Jesus','Christ the Son','Counselor','Creator','Eternal Father','Eternal God','Eternal Head','Eternal Judge',
    'Everlasting Father',
    'Everlasting God',
    'Father',
    'Father of heaven',
    'Father of heaven and of earth',
    'Founder of Peace',
    'God',
    'God of Abraham',
    'God of Abraham, and Isaac, and Jacob',
    'God of Abraham, and of Isaac, and the God of Jacob',
    'God of Isaac',
    'God of Jacob',
    'God of miracles',
    'God of nature',
    'God of the whole earth',
    'Good shepherd',
    'Great Creator',
    'Great Spirit',
    'Head',
    'Holy Child',
    'Holy God',
    'Holy Messiah',
    'Holy One',
    'Holy One of Israel',
    'Holy One of Jacob',
    'Husband',
    'Immanuel',
    'Jehovah',
    'Jesus',
    'Jesus Christ',
    'Keeper of the gate',
    'King',
    'King of heaven',
    'Lamb',
    'Lamb of God',
    'Lord',
    'Lord God',
    'Lord God Almighty',
    'Lord God Omnipotent',
    'Lord God of Hosts',
    'Lord Jehovah',
    'Lord Jesus',
    'Lord Jesus Christ',
    'Lord of Hosts',
    'Lord of the Vineyard',
    'Lord Omnipotent',
    'Maker',
    'Man',
    'Master',
    'Mediator',
    'Messiah',
    'Mighty God',
    'Mighty One of Israel',
    'Mighty One of Jacob',
    'Most High',
    'Most High God',
    'Only Begotten of the Father',
    'Only Begotten Son',
    'Prince of Peace',
    'Prophet',
    'Redeemer',
    'Redeemer of Israel',
    'Redeemer of the world',
    'Rock',
    'Savior',
    'Savior Jesus Christ',
    'Savior of the world',
    'Son|Son of God',
    'Son of Righteousness',
    'Son of the Eternal Father',
    'Son of the Everlasting God',
    'Son of the Most High God',
    'Stone',
    'Supreme Being',
    'True and Living God',
    'True Messiah',
    'True Vine',
    'Well Beloved',
    'Wonderful',
]
for pattern in patterns:
    print(pattern)

#%%

# df_bom['christ_references'] = df_bom['verse'].str.count(pattern, flags=re.IGNORECASE)
# df_grouped = df_bom.groupby('book_title').agg({'christ_references': 'sum'}).reset_index()
# def count_words(df, word):
#     string = r'(?i)\b'+word+'\b'
#     df['count_'+str(word)] = df['verse'].str.count(string)
#     return df
# counts = []
# for pattern in patterns:
#     count = count_words(df_bom, pattern)['count_'+pattern].sum()#.query('count_christ > 0')
#     print(pattern, count)
# total_references = df_bom['christ_references'].sum()
# print(f"Total references to Christ-related terms: {total_references}")
# df_grouped[''] = df_bom['Text'].str.count('key_word', case=False)
# string_occurrences = df.Token.apply(lambda x: sum([x.count(substring) for substing in ['wooly', 'girl']]))
# total_occurrences = string_occurrences.sum()
# df_bom['verse'].str.match('(Christ)').str.get(0).count()

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


