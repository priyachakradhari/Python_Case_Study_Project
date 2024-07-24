# -*- coding: utf-8 -*-
"""Blank_notebook

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17nNvOlo2l1vCKaYMP8OTWa8mTPbvXSGD

# **INTRODUCTION:**

The Adults dataset is a comprehensive collection of socio-economic and demographic information, used primarily for predictive modeling and classification tasks in data science. This dataset includes various attributes such as 'age', 'workclass', 'fnlwgt' (final weight), 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'hours-per-week', 'native-country', and 'income'. The 'age' column represents the age of the individuals. 'Workclass' provides information about the type of employment sector the individual is engaged in, while 'fnlwgt' is a census weight that indicates how many people the observation represents. 'Education' details the highest level of education achieved. 'Marital-status' describes the marital status of the individuals, and 'occupation' outlines their profession. 'Relationship' denotes familial relationships, 'race' captures the racial background, and 'gender' specifies the gender of the individuals. 'Hours-per-week' shows the average number of working hours per week. 'Native-country' indicates the country of origin, and 'income' is a binary attribute that classifies whether an individual's income is above or below a certain threshold. This dataset is commonly used for exploring correlations between demographic factors and income levels, providing valuable insights for socio-economic studies and machine learning applications.

**Import Laibraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""**Import dataset**"""

df=pd.read_csv("/content/adult.csv")
df.head(10)

df.tail(10)

df.shape

print("number of rows : ",df.shape[1])
print("number of columns :",df.shape[0])

#GETTING INFORMATION ABOUT OUR DATASET LINKE TOTAL NUMBER OF ROWS AND COLUMNS, DATATYPES OF EACH COLUMNS AND MEMORY REQUIREMENT

df.info()

#FETCH RANDOM SAMPLE FROM THE DATASET(50%)

df.sample(frac=0.50,random_state=100)

#CHECK NULL VALUES IN THE DATASET

df.isnull().sum()

# USING HEAT MAP FOR FINDING NULL VALUES

sns.heatmap(df.isnull())

"""OBSERVATION: As we can see, there are no null values present in the above heat map."""

#  PERFORM DATA CLEANING [REPLACE "?" WITH NAN]

df.isin(['?']).sum()

df['workclass'].replace("?",np.nan,inplace=True)
df['occupation'].replace("?",np.nan,inplace=True)
df['native-country'].replace("?",np.nan,inplace=True)

df.isin(["?"]).sum()

df.isnull().sum()

sns.heatmap(df.isnull())

"""OBSERVATION: In the above heap map, light area shows the null values."""

#  FINDING THE PERCENTAGE VALUE OF NULL VALUE IN EACH COLUMNS

(df.isnull().sum()*100)/len(df)

#DROP ALL THE MISSING VALUES

df.dropna(how="any",inplace=True)

print(df.shape)
print("The number of null values :",48842-45222)

# CHECK FOR DUMPLICATE DATA AND DROP THEM

df.duplicated().sum()

#DROP THE DUPLICATE DATA

df.drop_duplicates(inplace=True)

#CHECK THE NUMBER OF DUMPLICATE

df.duplicated().sum()

#CHECK THE SHAPE OF THE DATASET

df.shape

# GET OVERALL STATISTICS ABOUT THE DATAFRAME

df.describe()

# DROP THE UNWANTED COLUMNS

df.drop(['educational-num','capital-gain','capital-loss'],axis=1,inplace=True)

df.describe()

"""# **UNIVARIATE ANALYSIS**"""

# FINDING THE DISTRIPUTION OF THE AGE

df['age'].hist()
plt.title("Distribution of age")
plt.xlabel("age")
plt.ylabel("count")

df.columns

"""Que -  Find the total number of persons having age between 17 to 48 (inclusive) Using Between Method"""

sum(df['age'].between(17,48,inclusive='both'))

# FINDING THE DISTRIBUTION OF THE workclass column

plt.figure(figsize=(10,5))
df['workclass'].hist()
plt.title("Distribution of workclass")
plt.xlabel("workclass")
plt.ylabel("count")

"""OBSERVATIONS: Most of the employee are form the private sector"""

df['education'].unique()

"""Que - How many person having bachelors or masters degree?"""

f1=df['education']=='Bachelors'
f2=df['education']=='Masters'

len(df[f1 | f2])

len(df['education']=='Masters')

"""# Bivariate analysis"""

df.columns

sns.boxplot(x='income',y='age',data=df)

"""OBSERVATION: Most of the people are younger having salary <=50K and most of the people are having salary >50K.

Que - Replace the salary value [<=50K,>50K] with 0 and 1
"""

df['income'].unique()

df.replace(to_replace=['<=50K','>50K'],value=[0,1],inplace=True)

df.head()

"""Que - Which Workclass getting the hightest salary"""

df.groupby('workclass')['income'].mean().sort_values(ascending=False).head(1)

"""Que - How has better chance to get salary >50K male or female?"""

df.groupby('gender')['income'].mean().sort_values(ascending=False)

