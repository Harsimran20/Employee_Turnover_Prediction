#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score


# In[41]:


employee_data = pd.read_csv("C:/Users/ACER/Downloads/employee_turnover.csv")


# In[43]:


employee_data.head()


# In[45]:


employee_data.columns
employee_data.info()
employee_data['Employee_Turnover'].nunique()


# In[46]:


X = employee_data.drop('Employee_Turnover',axis = 1)
y = employee_data["Employee_Turnover"]


# In[47]:


y.head()


# In[48]:


X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size = 0.2 , random_state = 42
)


# In[49]:


y_train[y_train == 1]
y_train[y_train == 0]


# In[51]:


model = LogisticRegression(max_iter = 1000)
model.fit(X_train,y_train)


# In[52]:


y_pred = model.predict(X_test)


# In[53]:


print("Accuracy Score:",accuracy_score(y_test,y_pred)*100,"%")


# In[61]:


print("Precision Score:",precision_score(y_test,y_pred)*100,"%")


# In[65]:


# L1 Regularization (Lasso)
lasso = LogisticRegression(penalty='l1', solver='liblinear', C=0.5)
lasso.fit(X_train, y_train)


# In[67]:


# L2 Regularization (Ridge)
ridge = LogisticRegression(penalty='l2', C=1, max_iter=200)
ridge.fit(X_train, y_train)


# In[69]:


from sklearn.metrics import accuracy_score, classification_report

models = {'Baseline': model, 'Lasso': lasso, 'Ridge': ridge}

for name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"\n{name}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


# In[ ]:




