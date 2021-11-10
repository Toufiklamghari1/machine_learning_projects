import os
import time

import cv2
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import *
from sklearn.neural_network import MLPClassifier
from sklearn.tree import ExtraTreeClassifier

from database import getIndexTest, getIndex

# lire les images d'un dossie et faire l'etiqutage
# des images d'apprentissage
def readImages(path):
    #variable dans laquelle
    # en enregistre les paths des image
    paths =[]
    # variable dans laquelle en enregistre
    #la lettre correspond a chaque image
    d=[]
    #listdir retourne la liste des images
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
    return paths,d

# lire les images d'un dossie et faire l'etiqutage
# des images de test
def readImagesT(path):
    paths =[]
    d=[]
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
    return paths,d

# appliquer la fonction getImageVect
# sur l'ensemble des image d'apprentissage
def getImage(paths):
    X=[]
    for i in range(len(paths)):
        c=getImageVect(paths[i])
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
    return c;

# apprentissage par le classifier GaussianNB
def mLPClassifier():
    cl = MLPClassifier()#learning_rate_init=0.01, max_iter=500
    # cb = GaussianNB()
    X, d = X_D()
    start_time = time.time()
    cl.fit(X, d)
    end_time = time.time()
    tauxT = tauxRec_base_test(cl)
    tauxA = tauxdRec_base_appr(cl,X,d)
    print("\n le taux de connaissance a "
          "base d'apprentissage de MLPClassifier"
          " est : ",tauxA," %")
    return cl ,end_time - start_time,tauxT

# apprentissage par le classifier MultinomialNB
def multinomialRNB():
    cl = MultinomialNB(alpha=0.2);
    X, d = X_D()
    start_time = time.time()
    cl.fit(X, d)
    end_time = time.time()
    tauxT = tauxRec_base_test(cl)
    tauxA = tauxdRec_base_appr(cl, X, d)
    print("\n le taux de connaissance"
          " a base d'apprentissage de"
          "MultinomialNB est : ", tauxA, " %")
    return cl, end_time - start_time,tauxT

# apprentissage par le classifier BernoulliNB
def extraTreeClassifier():
    cl = ExtraTreeClassifier()
    X,d = X_D()
    start_time = time.time()
    cl.fit(X, d)
    end_time = time.time()
    tauxT = tauxRec_base_test(cl)
    tauxA = tauxdRec_base_appr(cl, X, d)
    print("\n le taux de connaissance"
          " a base d'apprentissage de ExtraTreeClassifier"
          " est : ", tauxA, " %")
    return cl, end_time - start_time,tauxT


def tauxdRec_base_appr(c,X,d):
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
    return X,d

 # la précision du MLPClassifier dans la phase du test
def tauxRec_base_test(c):
    path = "images/TEST/"
    paths, d = readImagesT(path)
    X = getImage(paths)
    y_pred = c.predict(X)
    ac_test = accuracy_score(y_pred, d)
    return round(ac_test*100,4)
