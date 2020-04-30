#!/bin/python
# Importar Bibliotecas
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

# Banco de Dados
cancer = pd.read_csv('./data.csv', index_col=0)

# Configurar Variáveis
diag = {'M':0, 'B':1}
cancer.diagnosis = [diag[item] for item in cancer.diagnosis]
X = cancer[cancer.columns[1:31]].to_numpy()
y = cancer[['diagnosis']].to_numpy()

# Funções
best_score = 0
max_score = 0
for n in range(1,10):
  knn = KNeighborsClassifier(n_neighbors=n, weights='uniform')
  scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
  if  scores.mean() > max_score:
    max_score = scores.mean()
    max_n = n
function_print = 'KneighborsClassifier:\t' + str(max_score) + '\t(n_neighbors=' + str(max_n) + ')'
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

max_score = 0
for n in range(1,10):
  tree = DecisionTreeClassifier(max_depth=n, random_state=0)
  scores = cross_val_score(tree, X, y, cv=10, scoring='accuracy')
  if  scores.mean() > max_score:
    max_score = scores.mean()
    max_n = n
function_print = 'DecisionTreeClassifier:\t' + str(max_score) + '\t(max_depth=' + str(max_n) + ')'
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

max_score = 0
for n in range(1,10):
  forest = RandomForestClassifier(n_estimators= n*10, random_state=0)
  scores = cross_val_score(forest, X, y, cv=10, scoring='accuracy')
  if  scores.mean() > max_score:
    max_score = scores.mean()
    max_n = n*10
function_print = 'RandomForestClassifier:\t' + str(max_score) + '\t(max_depth='+ str(max_n) + ')'
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

svm = SVC(kernel='poly',degree=1)
scores = cross_val_score(svm, X, y, cv=10, scoring='accuracy')
function_print = 'SuppotVectorMachine:\t' + str(scores.mean())
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

gnb = GaussianNB()
scores = cross_val_score(gnb, X, y, cv=10, scoring='accuracy')
function_print = 'GaussianNB:\t\t' + str(scores.mean())
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

mlp = MLPClassifier(solver='adam', alpha=0.0001, hidden_layer_sizes=(10,20,40),
random_state=42, learning_rate='constant', learning_rate_init=0.01, max_iter=100,
activation='logistic', momentum=0.9, tol=0.0001)
scores = cross_val_score(mlp, X, y, cv=10, scoring='accuracy')
function_print = 'MLPClassifier:\t\t' + str(scores.mean())
print(function_print)
if max_score > best_score:
  best_score = max_score
  best_function=function_print

# Resultados
print("\nBest Functions is:")
print(best_function)
