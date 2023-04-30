# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# insert line 171
# remove line 189
# search line 198
# edit/decreasekey line 207
# 2 tables to display data
# tableWidget and tableWidget_3
# data loads in tableWidget from self.loaddata1() / tableWidget_3 from self.loaddata2()
# when searching use self.search_loaddata()

import sys
import os
import platform
from pairingheap import patient_heap

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from pairingheap import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Medical Triage System"
        description = "DS2 Project"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.textEdit_2.setTextColor('black')
        widgets.textEdit_3.setTextColor('black')
        widgets.textEdit_4.setTextColor('black')
        widgets.textEdit_5.setTextColor('black')
        widgets.textEdit_9.setTextColor('black')
        widgets.textEdit_10.setTextColor('black')
        widgets.textEdit_11.setTextColor('black')
        widgets.textEdit_12.setTextColor('black')
        

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.insert_btn.clicked.connect(self.buttonClick)
        widgets.search_btn_2.clicked.connect(self.buttonClick)
        widgets.edit_btn_2.clicked.connect(self.buttonClick)
        widgets.remove_btn.clicked.connect(self.buttonClick)
        widgets.restet_btn.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.tableWidget.clicked.connect(self.mousePressEvent)
        widgets.tableWidget_3.clicked.connect(self.mousePressEvent)

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.loaddata1()

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.loaddata2()

        if btnName == "insert_btn": 
            if widgets.textEdit_2.toPlainText() == "" or widgets.textEdit_3.toPlainText()== "" or widgets.textEdit_4.toPlainText() == "":
                widgets.textEdit_5.setPlainText("You need to fill all the required fields")
                return
            #creates the patient class object
            patient = Patient(widgets.textEdit_2.toPlainText(),widgets.textEdit_3.toPlainText(),widgets.textEdit_4.toPlainText(), patient_heap.inserts)
            # lst.append(patient)
            # print(patient.name)
            patient_heap.insert(patient)
            patient_heap.display()
            patient_heap.inserts += 1
            # print("aaa")
            widgets.textEdit_2.clear()
            widgets.textEdit_3.clear()
            widgets.textEdit_4.clear()
            self.loaddata1()
            widgets.textEdit_5.setPlainText("Patient Successfully Added. Patient ID: "+str(patient.id))
            widgets.textEdit_5.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            

        if btnName == "remove_btn":  
            patient_heap.deleteMax()   #removes the root
            self.loaddata1()

        if btnName == "restet_btn":    
            self.loaddata2()    

        if btnName == "search_btn_2":  
            #calling the find function from pairing heap class
            p = patient_heap.find(int(widgets.textEdit_11.toPlainText())) #will give the node with the patient having the given id
            if p is not None:
                self.search_loaddata(p.patient)
            else:
                widgets.tableWidget_3.clearContents()

            
        if btnName == "edit_btn_2":
            #search for patient entered in textEdit_11
            id = int(widgets.textEdit_11.toPlainText())
            name = widgets.textEdit_12.toPlainText()
            age = widgets.textEdit_9.toPlainText()
            symptoms = widgets.textEdit_10.toPlainText()
            #calling the update function from pairing heap class
            p = patient_heap.update(id, name, age, symptoms) #updates the data and returns the patient node that was updated
            self.search_loaddata(p)
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self):
        # SET DRAG POS WINDOW
        # self.dragPos = event.globalPos()
        widgets.textEdit_5.clear()
        a = widgets.tableWidget_3.currentRow()
        pid = widgets.tableWidget_3.item(a,0).text()
        pname = widgets.tableWidget_3.item(a,1).text()
        page = widgets.tableWidget_3.item(a,2).text()
        psymptoms = widgets.tableWidget_3.item(a,4).text()
        widgets.textEdit_12.setPlainText(pname)
        widgets.textEdit_9.setPlainText(page)
        widgets.textEdit_10.setPlainText(psymptoms)
        widgets.textEdit_12.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        widgets.textEdit_9.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        widgets.textEdit_10.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        return (pid,pname,page,psymptoms)
         

    def loaddata1(self):
        lst = patient_heap.display()
        if lst is not None:
            lst.sort(key = lambda x : x.priority, reverse=True)
            row=0
            for patient in lst:
                widgets.tableWidget.setItem(row, 0, QTableWidgetItem(str(patient.id)))
                widgets.tableWidget.setItem(row, 1, QTableWidgetItem(patient.name))
                widgets.tableWidget.setItem(row, 2, QTableWidgetItem(patient.age))
                widgets.tableWidget.setItem(row, 3, QTableWidgetItem(str(patient.priority)))
                widgets.tableWidget.setItem(row, 4, QTableWidgetItem(patient.symptoms_str))
                row=row+1    

    def loaddata2(self):
        lst = patient_heap.display()
        if lst is not None:
            lst.sort(key = lambda x : x.priority, reverse=True)
            row=0
            for patient in lst:
                widgets.tableWidget_3.setItem(row, 0, QTableWidgetItem(str(patient.id)))
                widgets.tableWidget_3.setItem(row, 1, QTableWidgetItem(patient.name))
                widgets.tableWidget_3.setItem(row, 2, QTableWidgetItem(patient.age))
                widgets.tableWidget_3.setItem(row, 3, QTableWidgetItem(str(patient.priority)))
                widgets.tableWidget_3.setItem(row, 4, QTableWidgetItem(patient.symptoms_str))
                row=row+1                

    def search_loaddata(self,patient):
        widgets.tableWidget_3.clearContents()
        if patient is not None:
            row=0
            widgets.tableWidget_3.setItem(row, 0, QTableWidgetItem(str(patient.id)))
            widgets.tableWidget_3.setItem(row, 1, QTableWidgetItem(patient.name))
            widgets.tableWidget_3.setItem(row, 2, QTableWidgetItem(patient.age))
            widgets.tableWidget_3.setItem(row, 3, QTableWidgetItem(str(patient.priority)))
            widgets.tableWidget_3.setItem(row, 4, QTableWidgetItem(patient.symptoms_str))
                       
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
