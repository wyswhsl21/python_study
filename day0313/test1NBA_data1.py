import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from matplotlib import font_manager
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import auc, roc_curve, accuracy_score, f1_score
from sklearn.svm import SVC # 서포트 벡터 머신
from sklearn.tree import DecisionTreeClassifier # 결정트리
from sklearn.linear_model import LogisticRegression # 로지스틱 회귀
from sklearn.ensemble import RandomForestClassifier # 랜덤 포레스트
from sklearn.preprocessing import StandardScaler

mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

df = pd.read_csv('./data/nba_source.csv')

print(df)
print()
print(df.info())
print()

'''
해결 1) Awards 필드는 삭제
해결 2) 걀측값은 100% 숫자형 데이터이기 때문에 모두 평균값으로 대체
해결 3) [500 rows x 32 columns] 대신 100x31 행렬로 추출하여 변형
해결 4) 훈련 데이터, 테스트 데이터 분리
해결 5) 로지스틱 회귀, 결정트리, SVM, 랜덤 포레스트 모델 선언언
해결 6) 정답 데이터가 될 타겟 값 설정
해결 7) SVC(C, gamma) 설정
해결 8) fit(), predict, accuracy_score() 사용
'''

# 해결 1)
df = df.drop('Awards', axis=1)
# print(df)

# 해결 2)
cols_to_fill = ['3P', '3P%', '2P%', 'FT%', 'TRB', 'BLK']
df[cols_to_fill] = df[cols_to_fill].fillna(df[cols_to_fill].mean())
# print(df.info())

# 해결 3)
# df = df.iloc[:100, :]
# print(df)

# 플롯 저장 디렉터리 생성
plot_dir = './plots'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

# 해결 4)
X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 해결 5, 6, 7)

logi_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', random_state=42, max_iter=1000)
dt = DecisionTreeClassifier(criterion='gini', max_depth=5, min_samples_split=10, min_samples_leaf=5, random_state=42)
svm = SVC(kernel='rbf', probability=True, C=1.0, gamma='scale', random_state=42)
rf = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_split=2, min_samples_leaf=1, max_features='sqrt', bootstrap=True, random_state=42)

# 해결 8)

logi_reg.fit(X_train, y_train)
dt.fit(X_train, y_train)
svm.fit(X_train, y_train)
rf.fit(X_train, y_train)

y_pred_logi_reg = logi_reg.predict(X_test)
y_pred_dt = dt.predict(X_test)
y_pred_svm = svm.predict(X_test)
y_pred_rf = rf.predict(X_test)

print("Logistic Regression Report:")
print(confusion_matrix(y_test, y_pred_logi_reg))
print(classification_report(y_test, y_pred_logi_reg))
print()
print(f"Accuracy: {accuracy_score(y_test, y_pred_logi_reg)}")
print(f"F1 Score: {f1_score(y_test, y_pred_logi_reg)}")
print()

print("Decision Tree Report:")
print(confusion_matrix(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))
print()
print(f"Accuracy: {accuracy_score(y_test, y_pred_dt)}")
print(f"F1 Score: {f1_score(y_test, y_pred_dt)}")
print()

print("SVM Report:")
print(confusion_matrix(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))
print()
print(f"Accuracy: {accuracy_score(y_test, y_pred_svm)}")
print(f"F1 Score: {f1_score(y_test, y_pred_svm)}")
print()

print("Random Forest Report:")
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
print()
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf)}")
print(f"F1 Score: {f1_score(y_test, y_pred_rf)}")
print()
# ROC. AUC 시각화

plt.figure(figsize=(10, 8))

# 로지스틱 회귀, 결정트리, SVM, 랜덤 포레스트

y_prob_logi_reg = logi_reg.predict_proba(X_test)[:,1]
y_prob_dt = dt.predict_proba(X_test)[:,1]
y_prob_svm = svm.predict_proba(X_test)[:,1]
y_prob_rf = rf.predict_proba(X_test)[:,1]

fpr_logi_reg, tpr_logi_reg, _ = roc_curve(y_test, y_prob_logi_reg)
fpr_dt, tpr_dt, _ = roc_curve(y_test, y_prob_dt)
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_prob_svm)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)

auc_logi_reg = auc(fpr_logi_reg, tpr_logi_reg)
auc_dt = auc(fpr_dt, tpr_dt)
auc_svm = auc(fpr_svm, tpr_svm)
auc_rf = auc(fpr_rf, tpr_rf)

sns.lineplot(x=fpr_logi_reg, y=tpr_logi_reg, label=f'Logistic Regression (AUC = {auc_logi_reg:.2f})', palette='pastel')
sns.lineplot(x=fpr_dt, y=tpr_dt, label=f'Decision Tree (AUC = {auc_dt:.2f})', palette='pastel')
sns.lineplot(x=fpr_svm, y=tpr_svm, label=f'SVM (AUC = {auc_svm:.2f})', palette='pastel')
sns.lineplot(x=fpr_rf, y=tpr_rf, label=f'Random Forest (AUC = {auc_rf:.2f})', palette='pastel')

plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig(os.path.join(plot_dir, 'roc_curve.png'))
plt.show()

# 포지션별 득점 분포 시각화 (박스 플롯)
plt.figure(figsize=(12, 6))
sns.boxplot(x='Pos', y='PTS', data=df, palette='pastel')
plt.title('Points Distribution by Position')
plt.xlabel('Position(Pos)')
plt.ylabel('Points (PTS)')
plt.savefig(os.path.join(plot_dir, 'points_boxplot.png'))
plt.show()

# 포지션별 3점슛 성공률 분포 시각화 (바이올린 플롯)
plt.figure(figsize=(12, 6))
sns.violinplot(x='Pos', y='3P%', data=df, palette='pastel')
plt.title('3-Point Percentage Distribution by Position')
plt.xlabel('Position(Pos)')
plt.ylabel('3-Point Percentage (3P%)')
plt.savefig(os.path.join(plot_dir, '3p_percentage_violinplot.png'))
plt.show()

# 포지션별 출전 시간 분포 시각화 (히스토그램)
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='MP', hue='Pos', kde=True, palette='pastel')
plt.title('Minutes Played Distribution by Position')
plt.xlabel('Minutes Played (MP)')
plt.ylabel('Frequency')
plt.savefig(os.path.join(plot_dir, 'minutes_played_histplot.png'))
plt.show()

# 포지션별 평균 득점 및 리바운드 시각화 (막대 그래프)
pos_stats = df.groupby('Pos')[['PTS', 'TRB']].mean().reset_index()
pos_stats = pos_stats.melt(id_vars='Pos', var_name='Stat', value_name='Value')

plt.figure(figsize=(12, 6))
sns.barplot(x='Pos', y='Value', hue='Stat', data=pos_stats, palette='pastel')
plt.title('Average Points and Rebounds by Position')
plt.xlabel('Position(Pos)')
plt.ylabel('Average Value')
plt.savefig(os.path.join(plot_dir, 'average_points_rebounds_barplot.png'))
plt.show()


