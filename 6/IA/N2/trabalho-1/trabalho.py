import numpy as np 
from sklearn.datasets import fetch_openml 
from sklearn.model_selection import train_test_split   

# Carrega o dataset CIFAR-10 
cifar10 = fetch_openml('cifar_10', version=1, cache=True) 

# Separa os dados e os rótulos 
X = cifar10.data 
y = cifar10.target 

# Converte os rótulos para inteiros 
y = y.astype(np.uint8) 

# Divide os dados em conjuntos de treinamento e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Normaliza os dados 
X_train = X_train / 255.0 
X_test = X_test / 255.0