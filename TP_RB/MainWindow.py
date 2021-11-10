
# importations
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton, QRadioButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from Appr import *
from TP_RB.Apprentiissage import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("RBN Classifiers")
        self.resize(300, 300)
        # accepte le glissement des images
        self.setAcceptDrops(True)
        self.file_path = " "
        # styles css
        self.styles = """
                   QWidget {
                           background-color: #252525;
                   }

                   [cssClass~="label_image"]{
                           font-size: 16px;
                           color: #fafafa;
                           border-radius: 10px;
                           border: 5px solid rgb(40, 40, 40);
                           background-color: rgb(30, 30, 30);
                           font-size: 17px;
                   }
                   [cssClass~="label_image"]:hover{
                           background-color:#151515;
                           color: #ccc;
                           border: 3px dashed rgb(50, 50, 50);

                   }
                   [cssClass~="button_test"] {
                           background-color: #6930c3;
                           color: rgb(30, 30, 30);
                           border-radius: 7px;
                           font-size: 16px;
                           padding: 0px 8px 0px 8px;
                           min-height: 32px;
                           
                   }
                   [cssClass~="button_test"]::hover {
                       background-color: #47A6E5;
                       color: rgb(40, 40, 40);

                       border-radius: 10px;
                   }
                   [cssClass~="label_reponse"] {
                       background-color: #151515;
                       color: #fff;
                       border-radius: 7px;
                       font-size: 16px;
                       padding: 0px 8px 0px 8px;
                       width: 100%;
                       max-height: 32px;
                   }
                   [cssClass~="titleRButton"] {
                       background-color: #151515;
                       color: #fff;
                       border-radius: 7px;
                       font-size: 16px;
                       padding: 0px 8px 0px 8px;
                       width: 100%;
                       max-height: 30px;
                   }
                   QRadioButton{
                        background-color: #151515;
                       color: #fff;
                       border-radius: 7px;
                       font-size: 16px;
                       padding: 0px 8px 0px 8px;
                       width: 100%;
                       max-height: 32px;
                   }
                   [cssClass~="table_field"] {
                       color: #fff;
                       border: 2px solid rgb(50, 50, 50);
                       padding: 0px;
                       font-size: 14px;
                       max-height: 30px;
                   }
               """

        # application des styles css
        self.setStyleSheet(self.styles)

        self.setup_ui()

    def setup_ui(self):
        # appele du fonction qui fais l'apprentissage
        self.cG, self.tempsG, self.tauxG = gaussianRNB()
        self.cB, self.tempsB, self.tauxB = bernoulliRNB()
        self.cM, self.tempsM, self.tauxM = multinomialRNB()
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.tester = QRadioButton("Tester")
        self.comp = QRadioButton("comparer")
        self.label_title = QLabel(" comparison des classifiers RBN ")
        self.label_image = QLabel('\n\n glisser une image ici \n\n')
        self.label_reponse = QLabel()
        self.apprendreGaussT = QPushButton("Tester Gauss")
        self.apprendreBernT = QPushButton("Tester Bernoulli")
        self.apprendreMultiNT = QPushButton("Tester Multinomiale")

        self.label1 = QLabel("Classifier")

        self.label2 = QLabel("Temps d'execution en (s)")

        self.label3 = QLabel("Precision du teste en (%)")

        self.label4 = QLabel("GausianNB")

        self.label5 = QLabel("BernoulliNB")

        self.label6 = QLabel("MultinomialeNB")

        self.label_GT = QLabel(" "+ str(self.tempsG) +" ")
        self.label_GP = QLabel(" "+ str(self.tauxG) +" ")
        self.label_BT = QLabel(" "+ str(self.tempsB) +" ")
        self.label_BP = QLabel(" "+ str(self.tauxB) +" ")
        self.label_MT = QLabel(" "+ str(self.tempsM) +" ")
        self.label_MP = QLabel(" "+ str(self.tauxM) +" ")


    def modify_widgets(self):
        # Alignment
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_reponse.setAlignment(Qt.AlignCenter)
        self.label_title.setAlignment(Qt.AlignCenter)
        # Styles
        self.label_image.setProperty("cssClass", "label_image")
        self.label_reponse.setProperty("cssClass", "label_reponse")
        self.apprendreBernT.setProperty("cssClass", "button_test")
        self.apprendreMultiNT.setProperty("cssClass", "button_test")
        self.apprendreGaussT.setProperty("cssClass", "button_test")
        self.label_title.setProperty("cssClass","titleRButton")

        self.label1.setProperty("cssClass", "table_field")
        self.label2.setProperty("cssClass", "table_field")
        self.label3.setProperty("cssClass", "table_field")
        self.label4.setProperty("cssClass", "table_field")
        self.label5.setProperty("cssClass", "table_field")
        self.label6.setProperty("cssClass", "table_field")
        self.label_BT.setProperty("cssClass", "table_field")
        self.label_GT.setProperty("cssClass", "table_field")
        self.label_MT.setProperty("cssClass", "table_field")
        self.label_BP.setProperty("cssClass", "table_field")
        self.label_GP.setProperty("cssClass", "table_field")
        self.label_MP.setProperty("cssClass", "table_field")
        # visibility
        self.label_reponse.setVisible(False)

    def create_layouts(self):
        self.mainLayout = QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.mainLayout.addWidget(self.label_title, 0, 0, 1, 3)
        self.mainLayout.addWidget(self.tester, 1, 0, 1, 1)
        self.mainLayout.addWidget(self.comp, 1, 2, 1, 1)

        # Partie du teste
        self.mainLayout.addWidget(self.label_image, 2, 0, 1, 3)
        self.mainLayout.addWidget(self.apprendreBernT, 3, 0, 1, 1)
        self.mainLayout.addWidget(self.apprendreGaussT, 3, 1, 1, 1)
        self.mainLayout.addWidget(self.apprendreMultiNT, 3, 2, 1, 1)
        self.mainLayout.addWidget(self.label_reponse, 4, 0, 1, 3)

        # Partie du comparision

        self.mainLayout.addWidget(self.label1,2,0,1,1)
        self.mainLayout.addWidget(self.label2,2,1,1,1)
        self.mainLayout.addWidget(self.label3,2,2,1,1)

        self.mainLayout.addWidget(self.label4,3,0,1,1)
        self.mainLayout.addWidget(self.label_GT,3,1,1,1)
        self.mainLayout.addWidget(self.label_GP,3,2,1,1)

        self.mainLayout.addWidget(self.label5,4,0,1,1)
        self.mainLayout.addWidget(self.label_BT,4,1,1,1)
        self.mainLayout.addWidget(self.label_BP,4,2,1,1)
        self.mainLayout.addWidget(self.label6,6,0,1,1)
        self.mainLayout.addWidget(self.label_MT,6,1,1,1)
        self.mainLayout.addWidget(self.label_MP,6,2,1,1)


        self.label_image.setVisible(False)
        self.apprendreBernT.setVisible(False)
        self.apprendreGaussT.setVisible(False)
        self.apprendreMultiNT.setVisible(False)
        self.label_reponse.setVisible(False)

        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5.setVisible(False)
        self.label6.setVisible(False)
        self.label_MT.setVisible(False)
        self.label_MP.setVisible(False)
        self.label_GT.setVisible(False)
        self.label_GP.setVisible(False)
        self.label_BP.setVisible(False)
        self.label_BT.setVisible(False)

    def setup_connections(self):
        # connections
        self.apprendreBernT.clicked.connect(self.testApprB)
        self.apprendreGaussT.clicked.connect(self.testApprG)
        self.apprendreMultiNT.clicked.connect(self.testApprM)
        self.tester.toggled.connect(self.testSelected)
        self.comp.toggled.connect(self.compSelected)
        # affichage de l'image en utilisant un Qlabel

    def set_image(self, file_path):
        self.label_image.setPixmap(QPixmap(file_path))
        self.label_reponse.setVisible(False)

    def testSelected(self,selected):
        if selected:
            self.label_image.setVisible(True)
            self.apprendreBernT.setVisible(True)
            self.apprendreGaussT.setVisible(True)
            self.apprendreMultiNT.setVisible(True)

            self.label1.setVisible(False)
            self.label2.setVisible(False)
            self.label3.setVisible(False)
            self.label4.setVisible(False)
            self.label5.setVisible(False)
            self.label6.setVisible(False)
            self.label_MT.setVisible(False)
            self.label_MP.setVisible(False)
            self.label_GT.setVisible(False)
            self.label_GP.setVisible(False)
            self.label_BP.setVisible(False)
            self.label_BT.setVisible(False)

    def compSelected(self,selected):
        if selected:
            self.label_image.setVisible(False)
            self.apprendreBernT.setVisible(False)
            self.apprendreGaussT.setVisible(False)
            self.apprendreMultiNT.setVisible(False)
            self.label_reponse.setVisible(False)

            self.label1.setVisible(True)
            self.label2.setVisible(True)
            self.label3.setVisible(True)
            self.label4.setVisible(True)
            self.label5.setVisible(True)
            self.label6.setVisible(True)
            self.label_MT.setVisible(True)
            self.label_MP.setVisible(True)
            self.label_GT.setVisible(True)
            self.label_GP.setVisible(True)
            self.label_BP.setVisible(True)
            self.label_BT.setVisible(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
        # est utilisé lorsque l’action glisser-déposer est en cours.

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
        # se produit lorsque le largage est terminé.
        # L’action proposée de l’événement
        # peut être acceptée ou rejetée sous condition.

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            self.file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(self.file_path)
            event.accept()
        else:
            event.ignore()

        # Fonction qui fais le test sur les images

    def testApprB(self):
        if self.file_path == " ":
            self.label_reponse.setText("glisser une image dans la zone ")
            self.label_reponse.setVisible(True)
        else:
            Y = getImageVect(self.file_path)
            self.label_reponse.setText(" Teste Bernoulli : " + self.cB.predict([Y])[0])
            self.label_reponse.setVisible(True)

    def testApprG(self):
        if self.file_path == " ":
            self.label_reponse.setText("glisser une image dans la zone ")
            self.label_reponse.setVisible(True)
        else:
            Y = getImageVect(self.file_path)
            self.label_reponse.setText("Teste Gauss : " + self.cG.predict([Y])[0])
            self.label_reponse.setVisible(True)
    def testApprM(self):
        if self.file_path == " ":
            self.label_reponse.setText("glisser une image dans la zone ")
            self.label_reponse.setVisible(True)
        else:
            Y = getImageVect(self.file_path)
            self.label_reponse.setText("Teste MultiNomial : " + self.cM.predict([Y])[0])
            self.label_reponse.setVisible(True)