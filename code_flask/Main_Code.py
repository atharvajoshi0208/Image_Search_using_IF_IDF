import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import math
import os
import re
from collections import Counter, defaultdict, OrderedDict
from datetime import datetime
from itertools import chain

from nltk.corpus import stopwords  

import pandas as pd
import nltk, string

image_Descprtion =  defaultdict(dict)

nltk.download('punkt') # if necessary...
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def get_image_Descprtion(Image_Name,Descprtion):
    image_Descprtion[Image_Name] = Descprtion

def main_Function(query):
   
    df = pd.read_csv (r'F:\CA6005\Assignment 2\ProductDict.csv')
    df.rename(columns = {'0':'Image_Name', '1':'Descprtion'}, inplace = True)
    print('please enter your search query...')
    print(query)
    df['Query_Similarity'] = df.apply(lambda x:cosine_sim(query,x.Descprtion), axis=1)

    top_images = df.sort_values(by=['Query_Similarity'],ascending= False ).head(5)
    df_test = top_images.loc[top_images['Query_Similarity'] > 0]
    for index, row in df_test.iterrows():
        get_image_Descprtion(row['Image_Name'], row['Descprtion']) 
    
    return image_Descprtion 