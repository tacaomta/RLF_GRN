#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random
import pandas as pd
import numpy as np


# In[11]:


def get_balance(imbalanced_set):
    true_set = imbalanced_set[imbalanced_set['interaction']==1]
    false_set = imbalanced_set[imbalanced_set['interaction']==0]

    false_selected_indices = random.sample(list(false_set.index), k=true_set.shape[0])
    selected_false_set = false_set.loc[false_selected_indices]
    balanced_set = pd.concat([true_set, selected_false_set], ignore_index=True)
    return balanced_set


# In[12]:


def prepare_data(data):
    data['size'] = data['size'].astype(str)
    data_dummies = pd.get_dummies(data, columns=['size'])
    X = data_dummies.drop(['sample', 'regulator', 'target', 'interaction'], axis=1).values
    y = data_dummies['interaction'].values
    X = np.asarray(X).astype(np.float32)
    y = np.asarray(y).astype(np.float32)
    return X, y


# In[3]:


def performance_metrics(y, y_predicted):
    tp=fp=tn=fn=0
    for i in range(len(y)):
        if y[i]==y_predicted[i]:
            if y[i]==1:
                tp+=1
            else:
                tn+=1
        else:
            if y[i]==1:
                fn+=1
            else:
                fp+=1
    precision = tp/(tp+fp) if (tp+fp)!=0 else 0
    recall = tp/(tp+fn) if (tp+fn)!=0 else 0
    structural = (tp+tn)/(tp+fp+fn+tn)
    tpr = recall
    fpr = fp/(fp+tn) if (fp+tn)!=0 else 1
    return precision, recall, structural, tpr, fpr


# In[4]:


def get_performace(test_set, y_predicted):
    test_set['predicted'] = y_predicted
    result={}
    sample = set(test_set['sample'].values)
    for sp in sample:
        network = test_set[test_set['sample']==sp]
        p,r,st, tpr, fpr = performance_metrics(network['interaction'].values, network['predicted'].values)
        result[f'{sp}'] = {'precision':round(p, 4), 'recall':round(r,4), 'structural': round(st,4), 
                           'tpr':round(tpr, 4), 'fpr':round(fpr, 4)}
    return result


# In[15]:


def get_round(y_predicted, threshold=0.3):
    rounded_predicted = np.where(y_predicted >= threshold, np.ceil(y_predicted), np.floor(y_predicted))
    
    return rounded_predicted


# In[2]:


def get_roc_curve(y, y_predicted):
    tp=fp=tn=fn=0
    for i in range(len(y)):
        if y[i]==y_predicted[i]:
            if y[i]==1:
                tp+=1
            else:
                tn+=1
        else:
            if y[i]==1:
                fn+=1
            else:
                fp+=1
    TPR = tp/(tp+fn)
    FPR = fp/(fp+tn)
    return TPR, FPR


# In[ ]:




