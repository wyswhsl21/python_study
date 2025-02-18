# Suppress warnings
import warnings

warnings.filterwarnings('ignore')

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import LabelEncoder

# Ensure inline plotting
# %matplotlib inline

# Load the dataset
# file_path = '/kaggle/input/healthcare-workforce-mental-health-dataset/Healthcare Workforce Mental Health Dataset.csv'
# df = pd.read_csv(file_path, encoding='ascii')

# Display the first few rows of the dataset
# df.head()

print('bigData 분석 시작')
su = [3, 7, 9, 12]

data = np.array(su)
print(data)
