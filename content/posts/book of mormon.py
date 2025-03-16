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
reference_numbers = []
chapters_verses = []
verse_references = []
verses = []
chapters = []

for i, book in enumerate(data['books'][0:2]):
    for chapter in book['chapters']:
        # chapters.append(chapters)
        chapters_verses.append(chapter['verses'])
        for i, chapter_verses in enumerate(chapters_verses):
            # print(chapter_verses)
            for verse in chapter_verses:
                book_titles.append(book['book'])
                chapter_numbers.append(chapter['chapter'])
                reference_numbers.append(chapter['reference'])
                print(verse['text'])
                verses.append(verse['text'])
                verse_references.append(verse['reference'])

        # print(chapter)
        # print(chapter['chapter'])

# print(book_titles)
# print(chapter_numbers)
# print(reference_numbers)
# print(chapters_verses)
# print(verse_references)
# print(verses)


<<<<<<< HEAD

    # chapter_numbers.append(book['chapters'])
    # print(book['book'])
    # print(book['chapters'])
    # print(book['book'])
    # print(book)
    # print(i)
=======
# %%
>>>>>>> 978a82c9a11fb7484e6a66b8033f9c34466dc6f3

df_bom = (pd.DataFrame({'book_titles':book_titles,'chapter_numbers':chapter_numbers,'reference_numbers':reference_numbers,'reference':verse_references,'verse':verses}))

df_bom['word_count'] = df_bom['verse'].apply(lambda x: len(x.split()))
df_bom




# %%
