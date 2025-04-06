#%%
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import kagglehub
pd.set_option('display.max_colwidth', None)

def load_data():
    path = kagglehub.dataset_download("phyred23/bibleverses")
    print("Path to dataset files:", path)

    url = 'https://raw.githubusercontent.com/bcbooks/scriptures-json/refs/heads/master/book-of-mormon.json'
    resp = requests.get(url)
    data = json.loads(resp.text)
    book_titles = []
    chapter_numbers = []
    verse_references = []
    verses = []
    for i, book in enumerate(data['books']):
        for chapter in book['chapters']:
            for i, chapter_verse in enumerate(chapter['verses']):
                book_titles.append(book['book'])
                chapter_numbers.append(chapter['chapter'])
                verse_references.append(chapter_verse['reference'])
                verses.append(chapter_verse['text'])
    book_of_mormon = (pd.DataFrame({'book':book_titles,'chapter_number':chapter_numbers,'verse_reference':verse_references, 'text':verses}))
    book_of_mormon.to_csv('data/book_of_mormon.csv', index = False)

    pearl_of_great_price = pd.read_csv('data/pearl.csv', index_col=False).assign(book_title='Moses')
    pearl_of_great_price.to_csv('data/pearl_of_great_price.csv', index = False)
    pearl_of_great_price




#%%
def read_scriptures():
    book_of_mormon = pd.read_csv('data/book_of_mormon.csv')
    books = [
        'Genesis', 'Exodus', 'Leviticus', 
        'Numbers', 'Deuteronomy', 'Joshua',
        'Judges', 'Ruth', '1 Samuel', '2 Samuel', 
        '1 Kings', '2 Kings', '1 Chronicles',
        'Ezra', 'Nehemiah', 'Esther', 'Job',
        'Psalms', 'Proverbs', 
        'Ecclesiastes','Song of Solomon',
        'Isaiah', 'Jeremiah', 'Lamentations',
        'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 
        'Obadiah', 'Jonah', 
        'Micah', 'Nahum', 'Habakkuk',
        'Zephaniah', 'Haggai', 'Zechariah', 'Malachi',
        'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians',
        '2 Corinthians', 'Galatians', 'Ephesians', 
        'Philippians', 'Colossians',
        '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy',
        'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter',
        '1 John', '2 John', 
        '3 John', 'Jude', 'Revelation',
        '1 Nephi', '2 Nephi', 'Jacob', 'Enos', 
        'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 
        'Helaman', '3 Nephi', 
        '4 Nephi', 'Mormon', 'Ether', 'Moroni',
        'Moses', ]

    data_bible = pd.read_csv('data/bible.csv')

    pearl_of_great_price = pd.read_csv('data/pearl.csv', index_col=False).assign(book_title='Moses')

    df_scriptures = pd.concat([data_bible, book_of_mormon, pearl_of_great_price], ignore_index=True)
    df_scriptures['book'] = pd.Categorical(df_scriptures['book'], categories=books, ordered=True)
    return df_scriptures

df_scriptures = read_scriptures()

word = 'jesus'
# df = data_bible[data_bible['text'].str.contains('jesus', case=False)].groupby('text').agg()
# data_bible[word] = data_bible['text'].str.lower().str.count(word.lower())

df1 = df_scriptures.groupby('book').agg('count').reset_index()[['book', 'text']]
df1


#%%

df = df1
plt.figure(figsize=(10, 15))
bars = plt.barh(df['book'], df['text'])
plt.xlabel('Number of verses')
plt.ylabel('Book')
plt.title("Number of verses/book")
plt.gca().invert_yaxis()
for bar in bars:
	x = bar.get_width()
	y = bar.get_y() + bar.get_height() / 2
	plt.text(x + 1, y, str(int(x)), va='center')
plt.show()

plt.savefig("verses_per_book.png")

#%%


# df_bom.to_csv('data.csv',index=False)

# df_bom = (pd.DataFrame({'book_titles':book_titles,'chapter_numbers':chapter_numbers,'reference_numbers':reference_numbers,'reference':verse_references,'verse':verses}))

df_bom['word_count'] = df_bom['verse'].apply(lambda x: len(x.split()))
# df_bom.to_csv('data.csv',index=False)
df_bom

#%%
df_bom

abraham_verses = df_bom[df_bom['verse'].str.contains('Abraham', case=False)]
abraham_verses.head(3)
# abraham_verses = list(abraham_verses['verse_reference'])
for index, row in abraham_verses.iterrows():
    print(f'{row['verse_reference']}' + ' | ' + f'{row['verse']} |')

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
pattern = r'\b(Almighty|Almighty God|Being|Beloved|Beloved Son|Christ|Christ Jesus|Christ the Son|Counselor|Creator|Eternal Father|Eternal God|Eternal Head|Eternal Judge|Everlasting Father|Everlasting God|Father|Father of heaven|Father of heaven and of earth|Founder of Peace|God|God of Abraham|God of Abraham, and Isaac, and Jacob|God of Abraham, and of Isaac, and the God of Jacob|God of Isaac|God of Jacob|God of miracles|God of nature|God of the whole earth|Good shepherd|Great Creator|Great Spirit|Head|Holy Child|Holy God|Holy Messiah|Holy One|Holy One of Israel|Holy One of Jacob|Husband|Immanuel|Jehovah|Jesus|Jesus Christ|Keeper of the gate|King|King of heaven|Lamb|Lamb of God|Lord|Lord God|Lord God Almighty|Lord God Omnipotent|Lord God of Hosts|Lord Jehovah|Lord Jesus|Lord Jesus Christ|Lord of Hosts|Lord of the Vineyard|Lord Omnipotent|Maker|Man|Master|Mediator|Messiah|Mighty God|Mighty One of Israel|Mighty One of Jacob|Most High|Most High God|Only Begotten of the Father |Only Begotten Son|Prince of Peace|Prophet|Redeemer|Redeemer of Israel|Redeemer of the world|Rock|Savior|Savior Jesus Christ|Savior of the world|Son|Son of God|Son of Righteousness|Son of the Eternal Father |Son of the Everlasting God|Son of the Most High God|Stone|Supreme Being|True and Living God|True Messiah|True Vine|Well Beloved|Wonderful)'

patterns = [
    'Almighty','Almighty God','Being','Beloved','Beloved Son','Christ','Christ Jesus','Christ the Son','Counselor','Creator','Eternal Father','Eternal God','Eternal Head','Eternal Judge',
    'Everlasting Father','Everlasting God','Father','Father of heaven','Father of heaven and of earth','Founder of Peace','God','God of Abraham','God of Abraham, and Isaac, and Jacob',
    'God of Abraham, and of Isaac, and the God of Jacob','God of Isaac','God of Jacob','God of miracles','God of nature','God of the whole earth','Good shepherd','Great Creator',
    'Great Spirit','Head','Holy Child','Holy God','Holy Messiah','Holy One','Holy One of Israel','Holy One of Jacob','Husband','Immanuel','Jehovah','Jesus','Jesus Christ',
    'Keeper of the gate','King','King of heaven','Lamb','Lamb of God','Lord','Lord God','Lord God Almighty','Lord God Omnipotent','Lord God of Hosts',
    'Lord Jehovah','Lord Jesus','Lord Jesus Christ','Lord of Hosts','Lord of the Vineyard',
    'Lord Omnipotent','Maker','Man','Master','Mediator','Messiah','Mighty God',
    'Mighty One of Israel','Mighty One of Jacob','Most High','Most High God','Only Begotten of the Father','Only Begotten Son','Prince of Peace', 'Prophet','Redeemer','Redeemer of Israel',
    'Redeemer of the world','Rock','Savior','Savior Jesus Christ','Savior of the world','Son|Son of God','Son of Righteousness','Son of the Eternal Father','Son of the Everlasting God',
    'Son of the Most High God','Stone','Supreme Being','True and Living God','True Messiah',
    'True Vine','Well Beloved','Wonderful',
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

#%%
df_bom.head(3)

verse_counts = df_bom.groupby(['book_title']).agg('count').reset_index()[['book_title','verse']]

book_order = ['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni']

verse_counts
verse_counts['book_title'] = pd.Categorical(verse_counts['book_title'], categories=book_order, ordered=True)
verse_counts = verse_counts.sort_values('book_title')
verse_counts

# %%

bars = plt.barh(verse_counts['book_title'], verse_counts['verse'])
plt.xlabel('Number of verses')
plt.ylabel('Book')
plt.title('Number of verse in each book of the Book of Mormon')

plt.gca().invert_yaxis()

for bar in bars:
	x = bar.get_width()
	y = bar.get_y() + bar.get_height() / 2
	plt.text(x + 1, y, str(int(x)), va='center')  # Adjust +1 for spacing

plt.show()



# %%
verse_counts = df_bom[df_bom['verse'].str.contains('jesus', case=False)].groupby(['book_title']).agg('count').reset_index()[['book_title','verse']]
book_order = ['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni']
verse_counts['book_title'] = pd.Categorical(verse_counts['book_title'], categories=book_order, ordered=True)
verse_counts = verse_counts.sort_values('book_title')

bars = plt.barh(verse_counts['book_title'], verse_counts['verse'])
plt.xlabel('Number of verses')
plt.ylabel('Book')
plt.title("Number of verses in each book that contain the word 'jesus'")
plt.gca().invert_yaxis()
for bar in bars:
	x = bar.get_width()
	y = bar.get_y() + bar.get_height() / 2
	plt.text(x + 1, y, str(int(x)), va='center')
plt.show()

#%%
# word = 'ungodliness'

# df = df_bom[df_bom['verse'].str.contains(word, case=False)]

# df_bom['jesus_count'] = df_bom['verse'].str.lower().str.count('jesus')
# df_bom['jehovah_count'] = df_bom['verse'].str.lower().str.count('jesus')

df = df_bom
jesus_words = [
    'Beloved', 
    'Beloved Son','Christ', 
    'Christ Jesus','Christ the Son', 
    'Counselor','Creator', 
    'Eternal Father', 'Eternal God', 'Eternal Head', 
    # 'Eternal Judge', 'Everlasting Father', 
    # 'Everlasting God','Father','Father of heaven', 
    # 'Father of heaven and of earth', 
    # 'Founder of Peace', 'God',
    # 'God of Abraham', 'God of Abraham, and Isaac, and Jacob',
    # 'God of Abraham, and of Isaac, and the God of Jacob', 
    # 'God of Isaac', 'God of Jacob', 'God of miracles','God of nature', 
    # 'God of the whole earth', 'Good shepherd', 'Great Creator', 
    # 'Great Spirit', 'Head', 
    # 'Holy Child', 'Holy God', 
    # 'Holy Messiah', 'Holy One', 'Holy One of Israel', 'Holy One of Jacob', 
    # 'Husband', 'Immanuel', 'Jehovah', 'Jesus', 
    # 'Jesus Christ',
    # 'Keeper of the gate','King',
    # 'Almighty God', 
    # 'Almighty', 
    # 'Only Begotten Son', 
    # 'King of heaven',
    # 'Being',
    # 'Lamb',
    # 'Lamb of God',
    # 'Lord','Lord God',
    # 'Lord God Almighty',
    # 'Lord God Omnipotent','Lord God of Hosts',
    # 'Lord Jehovah','Lord Jesus','Lord Jesus Christ',
    # 'Lord of Hosts','Lord of the Vineyard','Lord Omnipotent', 
    # 'Maker', 
    # 'Man', 
    # 'Master','Mediator', 'Messiah', 'Mighty God', 
    # 'Mighty One of Israel', 'Mighty One of Jacob', 'Most High', 
    # 'Most High God','Only Begotten of the Father','Only Begotten Son',
    # 'Prince of Peace', 'Prophet', 'Redeemer', 'Redeemer of Israel', 
    # 'Redeemer of the world','Rock', 'Savior', 'Savior Jesus Christ', 
    # 'Savior of the world', 'Son','Son of God', 'Son of Righteousness', 
    # 'Son of the Eternal Father','Son of the Everlasting God', 
    # 'Son of the Most High God', 'Stone', 'Supreme Being', 
    # 'True and Living God', 'True Messiah', 
    # 'True Vine', 'Well Beloved', 
]
data = {}
for word in jesus_words:
    df[word] = df['verse'].str.lower().str.count(word.lower())
    data[word] = int(df[word].sum())

data = pd.DataFrame(data, index=['number of occurences']).melt().sort_values(by = 'value').query("value > 10")

bars = plt.barh(data['variable'], data['value'])
plt.xlabel('Number of verses')
plt.ylabel('Book')
plt.title("References to Jesus in The Book of Mormon")
plt.gca().invert_yaxis()
for bar in bars:
	x = bar.get_width()
	y = bar.get_y() + bar.get_height() / 2
	plt.text(x + 1, y, str(int(x)), va='center')
plt.show()

# df_bom.query(f"""word + '_count'""")
# df_bom[[word + '_count']]

# df[df['True Messiah'] > 0]

# df = df[df['verse'].str.contains('True Messiah', case=False)].groupby(['book_title']).agg('count').reset_index()[['book_title','verse']]
# df

#%%

word = 'moroni'

df = df_bom
df[word] = df['verse'].str.lower().str.count(word.lower())
df

#%%
print(df['Beloved'].sum())
print(df['Beloved Son'].sum())
print(df['Christ'].sum())

#%%

# df.groupby(['Beloved', 'Beloved Son', 'Christ']).size().reset_index(name='count')

pd.concat([
	df['Beloved'].value_counts(),
	df['Beloved Son'].value_counts(),
	df['Christ'].value_counts(),
], axis=1, keys=['Beloved', 'Beloved Son', 'Christ'])


#%%



bars = plt.barh(df['book_title'], df['verse'])
plt.xlabel('Number of verses')
plt.ylabel('Book')
plt.title("Number of verses in each book that contain the word '" + word + "'")
plt.gca().invert_yaxis()
for bar in bars:
	x = bar.get_width()
	y = bar.get_y() + bar.get_height() / 2
	plt.text(x + 1, y, str(int(x)), va='center')
plt.show()


# %%
