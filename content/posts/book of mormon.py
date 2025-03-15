#%%



from lds_scriptures import LDSScriptures


scriptures = LDSScriptures()
BookOfMormon = scriptures.bookOfMormon()
# display(BookOfMormon)

BookOfMormon

#%%
ch=BookOfMormon.allBooks()[0].chapter(11)
ch
# vv=ch.verse(17)


#%%

# display(vv)

# print('')

verses=BookOfMormon.allVerses()
verses
# display(verses[1381])

#%%
import requests
import json
import pandas as pd  

url = 'https://raw.githubusercontent.com/bcbooks/scriptures-json/refs/heads/master/book-of-mormon.json'
resp = requests.get(url)
data = json.loads(resp.text)

df = pd.json_normalize(data)
df


