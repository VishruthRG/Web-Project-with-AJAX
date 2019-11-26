#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR


# In[2]:


def normalise_row(row):
    normalise_dict = {1 : 12, 2 : 6, 3 : 3, 4 : 3, 5 : 4 , 6 : 4}
    #print(row)
    #print(row['essay_set'])
    return row['domain1_score'] / normalise_dict[row['essay_set']]


# In[3]:


# read the data file
essays = pd.read_csv("essays.csv", encoding = 'latin1')
#print(essays)


# In[4]:


# see domain1_score distribution

#get_ipython().run_line_magic('matplotlib', 'inline')
#essays.boxplot(column = 'domain1_score', by = 'essay_set', figsize = (10,10))


# In[5]:


#  important for prediction

essay_data = essays[['essay_set', 'essay', 'domain1_score']].copy()
essay = essays['essay']
essay_score = essays['domain1_score']


# In[6]:


# using bag of words



# In[7]:


#print(X_train)


# In[8]:




# In[9]:




# In[10]:





# In[11]:


# see which svm model is the best




# In[13]:


# lets try with tfidf

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(essay_data[(essay_data['essay_set'] == 1) | (essay_data['essay_set'] == 2)]['essay'])
y = essay_data[(essay_data['essay_set'] == 1) | (essay_data['essay_set'] == 2)]['domain1_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# In[14]:


#print(X_train.shape)


# In[18]:




# In[19]:



# In[20]:
#new_X = vectorizer.fit_transform(['Hello my name is Vishruth'])

# lets also try SVMs
svr = SVR(kernel='rbf',C=0.5)
svr.fit(X_train,y_train)

new = pd.read_csv('test.csv', encoding="latin1")
text = new['essay']
print(text)
new_text = vectorizer.fit_transform(new[(essay_data['essay_set'] == 1) | (new['essay_set'] == 2)]['essay'])
y_pred = svr.predict(new_text)

#print("Mean squared error: %.2f" % mean_squared_error(y_test,y_pred))

#ypred = svr.predict(X_test[0].reshape(-1, 1))   #change to xtest[i] where i is the index of test case

#print("Predicted - SVM linear kernel")
#for i in list(y_pred):
    #print(i)
    #(np.ceil(i))




