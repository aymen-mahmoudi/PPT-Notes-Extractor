from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType 
import sys







from functions import*


#  import the gui :
#ui, _ = loadUiType('gui.ui')      # from gui.ui
from gui import Ui_Form  as ui    # from gui.py




class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        #self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        self.HandleButtons()

       
        
        
    def HandleButtons(self):
        self.browse_pushButton.clicked.connect(lambda: self.openFileNameDialog())
        self.export_pushButton.clicked.connect(lambda: self.open_save_dialog_exp())
        self.delete_pushButton.clicked.connect(lambda: self.open_save_dialog_del())



    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PPTX (*.pptx);;PPT (*.ppt)", options=options)
        if self.fileName:
            print(self.fileName)
            self.set_file_path(self.fileName) 
            
                  

    def open_save_dialog_exp(self):
        option = QFileDialog.Options()
        option |=  QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(self, "Save File Name Title", f"{self.fileName[:-5]}.txt", "All Files (*)", options=option)
        if self.fileName:
            #notes = self.extract_notes(self.fileName)
            notes = self.extract_notes(self.fileName)
            with open(file[0], 'w', encoding='utf-8') as f:
                f.write(notes)
                
        QMessageBox.information(self, 'Information',
                                        f"File exported as {self.fileName[:-5]}.txt" ,
                                        QMessageBox.Ok)
            
    def open_save_dialog_del(self):
        option = QFileDialog.Options()
        option |=  QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(self, "Save File Name Title", f"{self.fileName[:-5]}_clean.pptx", "All Files (*)", options=option)
        if self.fileName:
            base_file_name = file[0]
            #notes = self.extract_notes(self.fileName)
            #clean_ppt = self.delete_all_notes(self.fileName)
            # with open(file[0], 'w', encoding='utf-8') as f:
            #     clean_ppt
            self.delete_all_notes(self.fileName,base_file_name)

        QMessageBox.information(self, 'Information',
                                        f"File exported as {self.fileName[:-5]}_clean.pptx" ,
                                        QMessageBox.Ok)
            

        
       
    def extract_notes(self,path):
        ppt=Presentation(path)
        notes_text=''
        for page, slide in enumerate(ppt.slides):
            # this is the notes that doesn't appear on the ppt slide,
            # but really the 'presenter' note. 
            if slide.has_notes_slide:
                notes_slide = slide.notes_slide
                text = notes_slide.notes_text_frame.text

            
            # Write some text to the file
            notes_text+=str(page + 1) + "\n"
            notes_text+='================================'+ "\n"
            notes_text+=text+ "\n"
        return notes_text
    
 

    def delete_all_notes(self,path,output_file):
        # Load the PowerPoint presentation
        ppt=Presentation(path)
        # Loop through each slide and delete its notes
        for i, slide in enumerate(ppt.slides):
            if slide.has_notes_slide:
                notes_slide = slide.notes_slide
                if notes_slide.notes_text_frame.text == '':
                    print('no NOTES')
                # Clear existing notes
                notes_slide.notes_text_frame.clear()
                
                print(f"Notes deleted for Slide {i + 1}.")
            else:
                print(f"Slide {i + 1} has no notes section.")
            
        ppt.save(output_file)
        print(f"Presentation saved as {output_file}")
        


    def set_file_path(self,file_path):
        self.path_lineEdit.setText(file_path)

    

    # def extract_notes(self,path):
    #     ppt=Presentation(path)
    #     notes = []
    #     for page, slide in enumerate(ppt.slides):
    #         # this is the notes that doesn't appear on the ppt slide,
    #         # but really the 'presenter' note. 
    #         textNote = slide.notes_slide.notes_text_frame.text
    #         notes.append((page,textNote)) 
    #     return notes
    
   
    
      




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()



