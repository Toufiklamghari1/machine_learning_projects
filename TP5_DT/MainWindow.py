
# importations
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton, QRadioButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from Apprentiissage import *

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
        self.cD, self.tempsD, self.tauxD = decisionTreeCl()
        self.cE, self.tempsE, self.tauxE = extraTreeCl()

        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.tester = QRadioButton("Test")
        self.comp = QRadioButton("Info")
        self.label_title = QLabel(" Decision Tree Classifier ")
        self.label_image = QLabel('\n\n glisser une image ici \n\n')
        self.label_reponse = QLabel()

        self.apprendreDT = QPushButton("DecisionTree")
        self.apprendreET = QPushButton("ExtraTree")

        self.label1 = QLabel("Classifier")

        self.label2 = QLabel("Temps d'execution")

        self.label3 = QLabel("Precision du teste")

        self.label6 = QLabel("DecisionTree")
        self.label7 = QLabel("ExtraTree")

        self.label_DT = QLabel(" "+ str(self.tempsD) +" ")
        self.label_DP = QLabel(" "+ str(self.tauxD) +" ")
        self.label_ET = QLabel(" "+ str(self.tempsE) +" ")
        self.label_EP = QLabel(" "+ str(self.tauxE) +" ")

    def modify_widgets(self):
        # Alignment
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_reponse.setAlignment(Qt.AlignCenter)
        self.label_title.setAlignment(Qt.AlignCenter)
        # Styles
        self.label_image.setProperty("cssClass", "label_image")
        self.label_reponse.setProperty("cssClass", "label_reponse")

        self.apprendreDT.setProperty("cssClass", "button_test")
        self.apprendreET.setProperty("cssClass", "button_test")
        self.label_title.setProperty("cssClass","titleRButton")

        self.label1.setProperty("cssClass", "table_field")
        self.label2.setProperty("cssClass", "table_field")
        self.label3.setProperty("cssClass", "table_field")
        self.label6.setProperty("cssClass", "table_field")
        self.label7.setProperty("cssClass", "table_field")
        self.label_DT.setProperty("cssClass", "table_field")
        self.label_DP.setProperty("cssClass", "table_field")
        self.label_ET.setProperty("cssClass", "table_field")
        self.label_EP.setProperty("cssClass", "table_field")
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
        self.mainLayout.addWidget(self.apprendreDT, 3, 0, 1, 1)
        self.mainLayout.addWidget(self.apprendreET, 3, 1, 1, 1)
        self.mainLayout.addWidget(self.label_reponse, 4, 0, 1, 3)

        # Partie du comparision

        self.mainLayout.addWidget(self.label1,2,0,1,1)
        self.mainLayout.addWidget(self.label2,2,1,1,1)
        self.mainLayout.addWidget(self.label3,2,2,1,1)

        self.mainLayout.addWidget(self.label6,6,0,1,1)
        self.mainLayout.addWidget(self.label_DT,6,1,1,1)
        self.mainLayout.addWidget(self.label_DP,6,2,1,1)

        self.mainLayout.addWidget(self.label7,7,0,1,1)
        self.mainLayout.addWidget(self.label_ET,7,1,1,1)
        self.mainLayout.addWidget(self.label_EP,7,2,1,1)

        self.label_image.setVisible(False)
        self.apprendreDT.setVisible(False)
        self.apprendreET.setVisible(False)
        self.label_reponse.setVisible(False)

        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.label6.setVisible(False)
        self.label_DP.setVisible(False)
        self.label_DT.setVisible(False)

        self.label7.setVisible(False)
        self.label_EP.setVisible(False)
        self.label_ET.setVisible(False)

    def setup_connections(self):
        # connections
        self.apprendreDT.clicked.connect(self.testApprDT)
        self.apprendreET.clicked.connect(self.testApprET)
        self.tester.toggled.connect(self.testSelected)
        self.comp.toggled.connect(self.compSelected)
        # affichage de l'image en utilisant un Qlabel

    def set_image(self, file_path):
        self.label_image.setPixmap(QPixmap(file_path))
        self.label_reponse.setVisible(False)

    def testSelected(self,selected):
        if selected:
            self.label_image.setVisible(True)
            self.apprendreDT.setVisible(True)
            self.apprendreET.setVisible(True)

            self.label1.setVisible(False)
            self.label2.setVisible(False)
            self.label3.setVisible(False)
            self.label6.setVisible(False)
            self.label7.setVisible(False)

            self.label_DP.setVisible(False)
            self.label_DT.setVisible(False)
            self.label_EP.setVisible(False)
            self.label_ET.setVisible(False)

    def compSelected(self,selected):
        if selected:
            self.label_image.setVisible(False)
            self.apprendreDT.setVisible(False)
            self.apprendreET.setVisible(False)
            self.label_reponse.setVisible(False)

            self.label1.setVisible(True)
            self.label2.setVisible(True)
            self.label3.setVisible(True)
            self.label6.setVisible(True)
            self.label7.setVisible(True)

            self.label_DP.setVisible(True)
            self.label_DT.setVisible(True)
            self.label_EP.setVisible(True)
            self.label_ET.setVisible(True)

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

    def testApprDT(self):
        if self.file_path == " ":
            self.label_reponse.setText("glisser une image dans la zone ")
            self.label_reponse.setVisible(True)
        else:
            Y = getImageVect(self.file_path)
            self.label_reponse.setText("DecisionTreeClassifier  : " + self.cD.predict([Y])[0])
            self.label_reponse.setVisible(True)

    def testApprET(self):
        if self.file_path == " ":
            self.label_reponse.setText("glisser une image dans la zone ")
            self.label_reponse.setVisible(True)
        else:
            Y = getImageVect(self.file_path)
            self.label_reponse.setText("ExtraTreeClassifier  : " + self.cE.predict([Y])[0])
            self.label_reponse.setVisible(True)