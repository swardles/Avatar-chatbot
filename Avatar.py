#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re


# In[3]:


alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


# In[4]:


df = pd.read_csv("Avatar.csv");


# In[5]:


Aang = df[df['name'] == "Aang"]
Aang.dropna(inplace=True)
Aang.reset_index(drop=True, inplace=True)
Aang['script'][4]
re.sub("[\[].*?[\]]", "",Aang['script'][4])

i = 0
for script in Aang['script']:
        script = re.sub("[\[].*?[\]]", "", script)
        Aang['script'][i] = script
        i += 1

finalAang = []
i = 0
for script in Aang['script']:
    Aang['script'][i] = split_into_sentences(script)
    i += 1
    finalAang += split_into_sentences(script)
    
for i in range (len(finalAang)):
    sentence = finalAang[i].strip()
    if (('!' == sentence) | ('!!' == sentence) | ('?' == sentence) | ('??' == sentence) | ('.' == sentence)):
        finalAang[i] = 0
while (0 in finalAang):
    finalAang.remove(0)


# In[ ]:


Katara = df[df['name'] == "Katara"]
Katara.dropna(inplace=True)
Katara.reset_index(drop=True, inplace=True)
Katara['script'][4]
re.sub("[\[].*?[\]]", "",Katara['script'][4])

i = 0
for script in Katara['script']:
        script = re.sub("[\[].*?[\]]", "", script)
        Katara['script'][i] = script
        i += 1

finalKatara = []
i = 0
for script in Katara['script']:
    Katara['script'][i] = split_into_sentences(script)
    i += 1
    finalKatara += split_into_sentences(script)
    
for i in range (len(finalKatara)):
    sentence = finalKatara[i].strip()
    if (('!' == sentence) | ('!!' == sentence) | ('?' == sentence) | ('??' == sentence) | ('.' == sentence)):
        finalKatara[i] = 0
while (0 in finalKatara):
    finalKatara.remove(0)


# In[ ]:


Sokka = df[df['name'] == "Sokka"]
Sokka.dropna(inplace=True)
Sokka.reset_index(drop=True, inplace=True)
Sokka['script'][4]
re.sub("[\[].*?[\]]", "",Sokka['script'][4])

i = 0
for script in Sokka['script']:
        script = re.sub("[\[].*?[\]]", "", script)
        Sokka['script'][i] = script
        i += 1

finalSokka = []
i = 0
for script in Sokka['script']:
    Sokka['script'][i] = split_into_sentences(script)
    i += 1
    finalSokka += split_into_sentences(script)
    
for i in range (len(finalSokka)):
    sentence = finalSokka[i].strip()
    if (('!' == sentence) | ('!!' == sentence) | ('?' == sentence) | ('??' == sentence) | ('.' == sentence)):
        finalSokka[i] = 0
while (0 in finalSokka):
    finalSokka.remove(0)


# In[ ]:


Zuko = df[df['name'] == "Zuko"]
Zuko.dropna(inplace=True)
Zuko.reset_index(drop=True, inplace=True)
Zuko['script'][4]
re.sub("[\[].*?[\]]", "",Zuko['script'][4])

i = 0
for script in Zuko['script']:
        script = re.sub("[\[].*?[\]]", "", script)
        Zuko['script'][i] = script
        i += 1

finalZuko = []
i = 0
for script in Zuko['script']:
    Zuko['script'][i] = split_into_sentences(script)
    i += 1
    finalZuko += split_into_sentences(script)

for i in range (len(finalZuko)):
    sentence = finalZuko[i].strip()
    if (('!' == sentence) | ('!!' == sentence) | ('?' == sentences) | ('??' == sentences) | ('.' == sentences)):
        finalZuko[i] = 0
while (0 in finalZuko):
    finalZuko.remove(0)


# In[ ]:


Toph = df[df['name'] == "Toph"]
Toph.dropna(inplace=True)
Toph.reset_index(drop=True, inplace=True)
Toph['script'][4]
re.sub("[\[].*?[\]]", "",Toph['script'][4])

i = 0
for script in Toph['script']:
        script = re.sub("[\[].*?[\]]", "", script)
        Toph['script'][i] = script
        i += 1

finalToph = []
i = 0
for script in Toph['script']:
    Toph['script'][i] = split_into_sentences(script)
    i += 1
    finalToph += split_into_sentences(script)
    
for i in range (len(finalToph)):
    sentence = finalToph[i].strip()
    if (('!' == sentence) | ('!!' == sentence) | ('?' == sentences) | ('??' == sentences) | ('.' == sentences)):
        finalToph[i] = 0
while (0 in finalToph):
    finalToph.remove(0)


# In[6]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance


# In[7]:


bot = ChatBot('Aang',
    logic_adapters=[
            'chatterbot.logic.BestMatch'
    ])


# In[8]:


trainer = ListTrainer(bot)
trainer.train(finalAang)


# In[17]:


aangPhrases = {}
aangPhrases["Hi"] = "Hi there."
aangPhrases["What's your name?"] = "My name is Aang, what's yours?"
aangPhrases["How're you?"] = "I'm great! About to go penguin sledding!"
aangPhrases["Are you the avatar?"] = "Yeah, but I never wanted to be..."


inputString = "How are you?"

if inputString in aangPhrases.keys():
    response = aangPhrases[inputString]
else:
    response = bot.get_response(inputString)
    
print("RESPONSE:", response)
