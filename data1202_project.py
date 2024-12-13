# -*- coding: utf-8 -*-
"""DATA1202_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gxvm7EH-LXeAdsRipNM5rcB3jGhU76Fu

# Introduction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

filepath = '/content/drive/MyDrive/DATA 1202 Project/Bank Customer Churn Prediction.csv'
df = pd.read_csv(filepath)
df.head()

df.describe().T

df.info()

"""# Explotary Data Analysis & Data Cleaning"""

df.isna().sum().sort_values(ascending=False)

df.duplicated().sum()

df1 = df.copy()

sns.set(style="whitegrid")

df1['country'] = df1['country'].map({'France': 0, 'Spain': 1, 'Germany': 2})

df1['gender'] = df1['gender'].map({'Female': 0, 'Male': 1})

plt.figure(figsize=(12, 6))
sns.heatmap(df1.corr(), annot=True, cmap="YlGnBu")
plt.title('Correlation Heatmap')
plt.show()

sns.set(style="whitegrid")

sns.countplot(x='churn', data=df)
plt.title('Churn Distribution')
plt.show()

sns.set(style="darkgrid")

sns.distplot( a=df["credit_score"],hist=True, kde=False, rug=False )

sns.histplot(
    data=df,
    x="age",
    y="balance",
    hue="churn",
)
plt.show()

sns.boxplot(
    x="products_number",
    y="balance",
    showmeans=True,
    data=df
)

sns.histplot(
    data=df,
    x="country",
    hue="churn")

sns.countplot(x="churn",hue="gender", data=df)
plt.show()

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(15,20))
axs=axs.flat
for i in range(len(df.columns)-1):
    sns.histplot(data=df, x=df.columns[i],hue="churn",ax=axs[i])

"""# Data Preprocessing and Feature Engineering"""

df['country'] = df['country'].map({'France': 0, 'Spain': 1, 'Germany': 2})

df['gender'] = df['gender'].map({'Female': 0, 'Male': 1})

data = df.copy()

X = data.drop(columns=['churn'])
y = data['churn']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

"""# Principal Component Analysis"""

# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Select numerical features for PCA
numerical_features = ['credit_score', 'age', 'tenure', 'balance', 'products_number', 'estimated_salary']
X = df[numerical_features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
n_components = 2
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

# Create a DataFrame for PCA results
pca_df = pd.DataFrame(data=X_pca, columns=['Principal Component 1', 'Principal Component 2'])
pca_df['Churn'] = df['churn']

# Visualize the results
plt.figure(figsize=(10, 8))
sns.scatterplot(data=pca_df, x='Principal Component 1', y='Principal Component 2',
                hue='Churn', palette='viridis', alpha=0.7)
plt.title('PCA of Bank Customer Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Churn', loc='best')
plt.show()

# Print explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

"""# Logistic Regression"""

from math import log
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

logreg_model = LogisticRegression()
logreg_model.fit(x_train, y_train)

y_pred = logreg_model.predict(x_test)

print("     Confusion Matrix ")
print(confusion_matrix(y_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y_test, y_pred))

log_reg_report = classification_report(y_test, y_pred, output_dict=True)

#Plot the confusion matrix

sns.heatmap(confusion_matrix(y_test, y_pred),cmap='crest',annot=True,fmt='8')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()

"""# Naive Bayes

"""

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

nb_model = GaussianNB()
nb_model.fit(x_train, y_train)

y_pred = nb_model.predict(x_test)

print("     Confusion Matrix ")
print(confusion_matrix(y_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y_test, y_pred))

nb_model_report = classification_report(y_test, y_pred, output_dict=True)

#Plot the confusion matrix

sns.heatmap(confusion_matrix(y_test, y_pred),cmap='crest',annot=True,fmt='8')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()

"""# Decision Tree & Random Forest Classfier

"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dt_model = DecisionTreeClassifier()
dt_model.fit(x_train, y_train)

y_pred = dt_model.predict(x_test)

print("     Confusion Matrix ")
print(confusion_matrix(y_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y_test, y_pred))

dt_model_report = classification_report(y_test, y_pred, output_dict=True)

#Plot the confusion matrix

sns.heatmap(confusion_matrix(y_test, y_pred),cmap='crest',annot=True,fmt='8')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

rf_model = RandomForestClassifier()
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)

print("     Confusion Matrix ")
print(confusion_matrix(y_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y_test, y_pred))

rf_model_report = classification_report(y_test, y_pred, output_dict=True)

# feature_names = X.columns

# feature_importance = pd.Series(rf_model.feature_importances_, index=feature_names).sort_values(ascending=True)
# feature_importance.plot(kind='barh')
# plt.xlabel('Feature Importance')
# plt.ylabel('Features')
# plt.title('Feature Importance in Random Forest')
# plt.tight_layout()
# plt.show()

#Plot the confusion matrix

sns.heatmap(confusion_matrix(y_test, y_pred),cmap='crest',annot=True,fmt='8')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()

"""# Neural Network

"""

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

nn_model = MLPClassifier(hidden_layer_sizes=(10, 5, 3), max_iter=1000, random_state=42)
nn_model.fit(x_train, y_train)

y_pred = nn_model.predict(x_test)

print("     Confusion Matrix ")
print(confusion_matrix(y_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y_test, y_pred))

print()
print("     Accuracy Score ")
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%')

nn_model_report = classification_report(y_test, y_pred, output_dict=True)

#Plot the confusion matrix

sns.heatmap(confusion_matrix(y_test, y_pred),cmap='crest',annot=True,fmt='8')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()

"""# Model Comparison"""

data = {
    'Model': ['Logistic Regression', 'Neural Network', 'Decision Tree', 'Naive Bayes', 'Random Forest'],
    'Accuracy': [log_reg_report['accuracy'], nn_model_report['accuracy'], dt_model_report['accuracy'], nb_model_report['accuracy'], rf_model_report['accuracy']],
    'Precision': [log_reg_report['1']['precision'], nn_model_report['1']['precision'], dt_model_report['1']['precision'], nb_model_report['1']['precision'], rf_model_report['1']['precision']],
    'Recall': [log_reg_report['1']['recall'], nn_model_report['1']['recall'], dt_model_report['1']['recall'], nb_model_report['1']['recall'], rf_model_report['1']['recall']],
    'F1-Score': [log_reg_report['1']['f1-score'], nn_model_report['1']['f1-score'], dt_model_report['1']['f1-score'], nb_model_report['1']['f1-score'], rf_model_report['1']['f1-score']]
}

df = pd.DataFrame(data)

df_melted = df.melt(id_vars='Model', var_name='Metric', value_name='Score')

df_heatmap = df.set_index('Model')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title('Performance Metrics Heatmap')
plt.ylabel('Models')
plt.xlabel('Metrics')
plt.tight_layout()
plt.show()

sns.set(style="whitegrid")


plt.figure(figsize=(12, 6))
barplot = sns.barplot(x='Model', y='Score', hue='Metric', data=df_melted)


for bar in barplot.patches:
    bar_height = bar.get_height()
    bar_x = bar.get_x() + bar.get_width() / 2
    plt.text(bar_x, bar_height + 0.01, f'{bar_height:.2f}', ha='center', va='bottom', fontsize=10)

# Customize plot
plt.title('Comparison of ML Model Performance Metrics', fontsize=16)
plt.xlabel('Models', fontsize=14)
plt.ylabel('Score', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Metric')
plt.tight_layout()

# Show plot
plt.show()

"""# ROC/AUC Curve"""

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
# Initialize models
models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": GaussianNB(),
    "Random Forest": RandomForestClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Neural Network": MLPClassifier(hidden_layer_sizes=(10, 5, 3), max_iter=1000, random_state=42)
}

# Plot ROC curves
plt.figure(figsize=(10, 10))
for name, model in models.items():
    # Train the model
    model.fit(x_train, y_train)

    # Predict probabilities
    y_pred = model.predict_proba(x_test)[:, 1]

    # Compute ROC curve and AUC score
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred)

    # Plot the ROC curve
    plt.plot(fpr, tpr,linewidth=2,label=f"{name} (AUC = {auc:.2f})")

# Plot settings
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')  # Random chance line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves for Multiple Models')
plt.legend(loc='lower right')
plt.grid()
plt.show()

"""# Adding Changes"""

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

x1_train, x1_test, y1_train, y1_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=100)

logreg_model1 = LogisticRegression()
logreg_model1.fit(x1_train, y1_train)

y_pred = logreg_model1.predict(x1_test)

print("     Confusion Matrix ")
print(confusion_matrix(y1_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y1_test, y_pred))

log_reg_report1 = classification_report(y1_test, y_pred, output_dict=True)

dt_model1 = DecisionTreeClassifier()
dt_model1.fit(x1_train, y1_train)

y_pred = dt_model1.predict(x1_test)

print("     Confusion Matrix ")
print(confusion_matrix(y1_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y1_test, y_pred))

dt_model_report1 = classification_report(y1_test, y_pred, output_dict=True)

rf_model1 = RandomForestClassifier()
rf_model1.fit(x1_train, y1_train)

y_pred = rf_model1.predict(x1_test)

print("     Confusion Matrix ")
print(confusion_matrix(y1_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y1_test, y_pred))

rf_model_report1 = classification_report(y1_test, y_pred, output_dict=True)

nb_model1 = GaussianNB()
nb_model1.fit(x1_train, y1_train)

y_pred = nb_model1.predict(x1_test)

print("     Confusion Matrix ")
print(confusion_matrix(y1_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y1_test, y_pred))

nb_model_report1 = classification_report(y1_test, y_pred, output_dict=True)

nn_model1 = MLPClassifier(hidden_layer_sizes=(10, 5, 3), max_iter=1000, random_state=150)

nn_model1.fit(x1_train, y1_train)

y_pred = nn_model1.predict(x1_test)

print("     Confusion Matrix ")
print(confusion_matrix(y1_test, y_pred))

print()

print("     Classification Report ")
print()
print(classification_report(y1_test, y_pred))

nn_model_report1 = classification_report(y1_test, y_pred, output_dict=True)

data = {
    'Model': ['Logistic Regression', 'Neural Network', 'Decision Tree', 'Naive Bayes', 'Random Forest'],
    'Accuracy': [log_reg_report1['accuracy'], nn_model_report1['accuracy'], dt_model_report1['accuracy'], nb_model_report1['accuracy'], rf_model_report1['accuracy']],
    'Precision': [log_reg_report1['1']['precision'], nn_model_report1['1']['precision'], dt_model_report1['1']['precision'], nb_model_report1['1']['precision'], rf_model_report1['1']['precision']],
    'Recall': [log_reg_report1['1']['recall'], nn_model_report1['1']['recall'], dt_model_report1['1']['recall'], nb_model_report1['1']['recall'], rf_model_report1['1']['recall']],
    'F1-Score': [log_reg_report1['1']['f1-score'], nn_model_report1['1']['f1-score'], dt_model_report1['1']['f1-score'], nb_model_report1['1']['f1-score'], rf_model_report1['1']['f1-score']]
}

df = pd.DataFrame(data)

df_melted = df.melt(id_vars='Model', var_name='Metric', value_name='Score')

df_heatmap = df.set_index('Model')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title('Performance Metrics Heatmap')
plt.ylabel('Models')
plt.xlabel('Metrics')
plt.tight_layout()
plt.show()