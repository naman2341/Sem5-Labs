import numpy as np
import random
import pandas as pd
import math



def get_avg_attr_info(df, attri):
  avg_info = 0
  target = df.keys()[-1]
  new_df = df[[attri,target]]
  new_df.groupby(attri)
  a = dict(new_df[attri].value_counts())
  for i in a:
    x = new_df.loc[df[attri]==i]
    sum = 0
    e = 0
    category = dict(x[target].value_counts())
    for j in category:
      sum+= category.get(j)
      if category.get(j) == 0 or category.get(j)==len(x[target]):
              e = 0
      else:
              fraction = category.get(j)/len(x[target])
              e += -fraction*np.log2(fraction)
    avg_info += sum/len(df)*e
  return np.float(avg_info)


def get_entropy_of_dataset(df):
  col = df.keys()[-1]
  val = df[col].unique()
  ent = 0
  for v in val:
    prob = df[col].value_counts()[v]/len(df[col])
    ent += -prob * np.log2(prob)
  return np.float(ent)


def get_ig(df, attri):
  uni = np.unique(df[attri])
  g = get_entropy_of_dataset(df)
  for u in uni:
      subdata = df[df[attri] == u]
      sub_e = get_entropy_of_dataset(subdata)
      g -= (float(len(subdata)) / float(len(df))) * sub_e
  return g


def get_selected_attribute(df):
  infg = dict()
  result=list()
  for key in df.keys()[:-1]:
    infg[key]=get_entropy_of_dataset(df)-get_avg_attr_info(df,key)
  max_value_key=max(infg,key=lambda x:infg[x])
  result.append(infg)
  result.append(max_value_key)
  return tuple(result)