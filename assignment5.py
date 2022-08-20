# -*- coding: utf-8 -*-
"""Assignment5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1illeXzlAGFhu2aAIGI6KtNnbiV6hwQOK
"""

import pandas as pd
import numpy as np
import seaborn as sns

data=pd.read_csv("train.csv")

data.head()

data.shape

data.isna().sum()

data.dropna(axis=0,inplace=True)

data

data.reset_index(inplace=True)

data

#checking of balancing
sns.countplot(data["label"])

a=data["title"][0]
a

#preprocessing data
#regular expression

import re
a=re.sub('[^a-zA-Z]',' ',a)

#coverting to lowercase
a=a.lower()
a

#split the text
list=a.split()
list

!pip install nltk
import nltk

nltk.download('stopwords')

#removing the stopwords from the
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()
review=[ps.stem(word) for word in list if word not in set(stopwords.words('english'))]

review

' '.join(review)

corpus=[]

for i in range(0,len(data)):
  review=re.sub('[^a-zA-Z]',' ',data['title'][i])
  review=review.lower()
  list=review.split()
  review=[ps.stem(word) for word in list if not word in set(stopwords.words('english'))]
  corpus.append(' '.join(review))

corpus[0]

corpus

#bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()

x.shape

x[0]

y=data["label"]

y.shape

#training set and test set spliting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

x_train.shape

x_test.shape

from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

y_pred

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True)
cm

accuracy_score(y_test,y_pred)