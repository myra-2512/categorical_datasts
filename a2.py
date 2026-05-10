import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('Titanic Dataset.csv')
print(df.head(5))

sns.set_style('whitegrid')

sns.countplot(x='Survived',data=df)
plt.show()

sns.countplot(x='Gender',hue='Survived',data=df)
plt.show()

sns.countplot(x='Embarked',data=df)
plt.show()

sns.countplot(x='Embarked',hue='Survived',data=df)
plt.show()

sns.countplot(x='Embarked',data=df)
plt.xticks(rotation=30,fontsize=20)
plt.show()