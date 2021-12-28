import pandas as pd

from sklearn.decomposition import PCA

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib

dt_heart = pd.read_csv('./data/heart.csv')

# Seleccion de caracteristicas
dt_features = dt_heart.drop(['target'], axis=1)
dt_target = dt_heart['target']

# Normalizacion de datos
dt_features = StandardScaler().fit_transform(dt_features)

# Separacion de datos
X_train, X_test, y_train, y_test = train_test_split(dt_features, dt_target, test_size=0.2, random_state=None) # Dividir los datos en train y test

# Entrenando PCA (13 features -> 4 features)
pca = PCA(n_components=4)
pca.fit(X_train)

# Reduccion de la dimensionalidad de train y de test
dt_train = pca.transform(X_train)
dt_test = pca.transform(X_test)

# Entrenamiento de la inteligencia artificial
boost = GradientBoostingClassifier(n_estimators=190).fit(dt_train, y_train)

boost_pred = boost.predict(dt_test)

score = accuracy_score(boost_pred, y_test.values)

# print(score)

joblib.dump(boost, 'model.pkl')
joblib.dump(pca, 'pca.pkl')