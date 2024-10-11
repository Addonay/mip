#!/usr/bin/env python
# coding: utf-8

# In[3]:


import polars as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[4]:


df = pl.read_csv('/home/addo/dev/projects/mip/dumped_stuff/assets/hehe.csv')
df.head(15)


# In[5]:


# checking for null values
df.drop_nulls()


# In[6]:


df = df.rename({"sex": "gender"})


# In[7]:


df = df.filter(df.is_unique())
df.filter(df.is_duplicated())


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df.select("age", "bmi", "charges"))  # Replace with your columns
plt.show()


# In[9]:


# check for data distribution
df_pd = df.to_pandas()
df_pd[["age", "bmi", "charges"]].hist(bins=20, figsize=(10, 5))
plt.show()


# In[10]:


sns.heatmap(df_pd.corr(method='pearson', numeric_only=True), annot=True, cmap='coolwarm')
plt.show()


# In[11]:


le = LabelEncoder()
df = df.with_columns(pl.Series("gender", le.fit_transform(df["gender"].to_list())))
df = df.with_columns(pl.Series("smoker", le.fit_transform(df["smoker"].to_list())))
df = df.with_columns(pl.Series("region", le.fit_transform(df["region"].to_list())))
df = df.with_columns(pl.Series("heart_disease_history", le.fit_transform(df["heart_disease_history"].to_list())))
df = df.with_columns(pl.Series("occupation", le.fit_transform(df["occupation"].to_list())))
df.head(15)


# ## Model Creation

# In[12]:


X = df.drop("charges").to_numpy()
y = df["charges"].to_numpy()

y_log = np.log(y + 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_log, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[13]:


param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
}

rf_model = RandomForestRegressor(random_state=42)

grid_search = GridSearchCV(
    estimator=rf_model, param_grid=param_grid, cv=5, scoring="neg_mean_squared_error"
)

grid_search.fit(X_train_scaled, y_train)

best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

print(f"Best Parameters: {best_params}")

y_pred_best = best_model.predict(X_test_scaled)


y_pred_best_original = np.exp(y_pred_best) 

np_stuff = np.exp(y_test)
mse_best = mean_squared_error(np_stuff, y_pred_best_original)
mae_best = mean_absolute_error(np_stuff, y_pred_best_original)
r2_best = r2_score(np_stuff, y_pred_best_original)

print(f"Best Random Forest MSE: {mse_best}")
print(f"Best Random Forest MAE: {mae_best}")
print(f"Best Random Forest R²: {r2_best}")


# In[14]:


import pickle


with open("/home/addo/dev/projects/mip/dumped_stuff/model/rf_model.pkl", "wb") as f:
    pickle.dump(best_model, f)


# In[ ]:




