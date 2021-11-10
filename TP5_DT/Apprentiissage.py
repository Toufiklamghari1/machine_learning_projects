import os
import time

import cv2
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier

from database import getIndexTest, getIndex

# lire les images d'un dossie et faire l'etiqutage
# des images d'apprentissage


def readImages(path):
    # variable dans laquelle
    # en enregistre les paths des image
    paths = []
    # variable dans laquelle en enregistre
    # la lettre correspond a chaque image
    d = []
    # listdir retourne la liste des images
    # trouvé dans le dossie path
    listTmages = os.listdir(path)
    for i in range(len(listTmages)):
        paths.append(path+listTmages[i])
        d.append(
            # getIndex fonction qui
            # return la lettre de chaque image
            getIndex(
                int(
                    (os.path.splitext(listTmages[i])[0])
                )
            )
        )
    return paths, d

# lire les images d'un dossie et faire l'etiqutage
# des images de test


def readImagesT(path):
    paths = []
    d = []
    listTmages = os.listdir(path)
    for i in range(len(listTmages)):
        paths.append(path+listTmages[i])
        d.append(
            getIndexTest(
                int(
                    (os.path.splitext(listTmages[i])[0])
                )
            )
        )
    return paths, d

# appliquer la fonction getImageVect
# sur l'ensemble des image d'apprentissage


def getImage(paths):
    X = []
    for i in range(len(paths)):
        c = getImageVect(paths[i])
        X.append(c)
    return X

# fonction qui retourne l'image aplatie


def getImageVect(image):
    # lire une image en espace niveaux de gris
    img = cv2.imread(image, 0)
    # seuillage
    data, imageTh = cv2.threshold(
        img, (np.max(img)-np.min(img))/2, 1, cv2.THRESH_BINARY
    )
    # Aplatie pour la mettre dans un tableau monodimensionne
    c = imageTh.flatten()
    return c

# Decision Tree Classifier


def decisionTreeCl():
    dt = DecisionTreeClassifier()
    X, d = X_D()
    start_time = time.time()
    dt.fit(X, d)
    end_time = time.time()
    tauxT = tauxRec_base_test(dt)
    tauxA = tauxdRec_base_appr(dt, X, d)
    print("\n le taux de connaissance"
          " a base d'apprentissage du "
          "DecisionTreeClassifier "
          " est : ", tauxA, " %")
    return dt, end_time - start_time, tauxT

# Decision Tree Classifier


def extraTreeCl():
    et = ExtraTreeClassifier()
    X, d = X_D()
    start_time = time.time()
    et.fit(X, d)
    end_time = time.time()
    tauxT = tauxRec_base_test(et)
    tauxA = tauxdRec_base_appr(et, X, d)
    print("\n le taux de connaissance"
          " a base d'apprentissage du "
          "ExtraTreeClassifier "
          " est : ", tauxA, " %")
    return et, end_time - start_time, tauxT


def tauxdRec_base_appr(c, X, d):
    # le taux d'apprentissage
    y_pred = c.predict(X)
    ac_appr = accuracy_score(y_pred, d)
    return round(ac_appr * 100, 2)

# fonction qui faire le pretraitement
# sur les images d'aprrentissage


def X_D():
    # le dossie ou se trouve notre images
    path = "images/apprentissage/"
    # étiquetage
    paths, d = readImages(path)
    # les images Aplatié dans un vecteur
    X = getImage(paths)
    return X, d

# la précision du MLPClassifier dans la phase du test


def tauxRec_base_test(c):
    path = "images/TEST/"
    paths, d = readImagesT(path)
    X = getImage(paths)
    y_pred = c.predict(X)
    ac_test = accuracy_score(y_pred, d)
    return round(ac_test*100, 4)
