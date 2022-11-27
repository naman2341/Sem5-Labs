#front end
from tkinter import *
import tkinter.messagebox
import backend as pb

class Med:
    
    def __init__(self,root):
       self.root=root 
       self.root.title("Pharmacy Database Management System")
       self.root.geometry(newGeometry="1328x585+0+0")
       self.root.config(bg="#021e2f")
       #ASSIGN SOME VARIABLE TO STORE OUR ENTRY FILELD VALUES
       drug_name=StringVar()
       batch_number=StringVar()
       MedicineType=StringVar()
       Manufacturer=StringVar()
       stock_quantity=StringVar()
       expiry_date=StringVar()
       Price=StringVar()
       '''drug_name=StringVar()
       batch_number=StringVar()
       MedicineType=StringVar()
       Manufacturer=StringVar()
       stock_quantity=StringVar()
       expiry_date=StringVar()
       Price=StringVar()
       Mobile=StringVar()'''
       ###########################FUNCTIONS#############
       pb.PharmData()
       def iExit():
              iExit=tkinter.messagebox.askyesno("Pharmacy Database Management System","Confirm if you want to exit")
              if iExit>0:
                     root.destroy()
                     return
       def clearData():
              self.txtdrug_name.delete(0,END)
              self.txtbatch_number.delete(0,END)
              self.txtMedicineType.delete(0,END)
              self.txtManufacturer.delete(0,END)
              self.txtstock_quantity.delete(0,END)
              self.txtexpiry_date.delete(0,END)
              self.txtPrice.delete(0,END) 
       pb.PharmData()
       def addData():
              if(len(drug_name.get())!=0):
                     
                     pb.addStdRec(drug_name.get(),batch_number.get(),MedicineType.get(),Manufacturer.get(),stock_quantity.get(),expiry_date.get(),Price.get())
                     pharmalist.delete(0,END)
                     pharmalist.insert(END,(drug_name.get(),batch_number.get(),MedicineType.get(),Manufacturer.get(),stock_quantity.get(),expiry_date.get(),Price.get()))

       def DisplayData():
              pharmalist.delete(0,END)
              for row in pb.viewData():
                  pharmalist.insert(END,row)
       def Records(event):
              global sd
              searchstd = pharmalist.curselection()[0]
              sd=pharmalist.get(searchstd)
              self.txtdrug_name.delete(0,END)
              self.txtdrug_name.insert(END,sd[0])
              self.txtbatch_number.delete(0,END)
              self.txtbatch_number.insert(END,sd[1])
              self.txtMedicineType.delete(0,END)
              self.txtMedicineType.insert(END,sd[2])
              self.txtManufacturer.delete(0,END)
              self.txtManufacturer.insert(END,sd[3])
              self.txtstock_quantity.delete(0,END)
              self.txtstock_quantity.insert(END,sd[4])
              self.txtexpiry_date.delete(0,END)
              self.txtexpiry_date.insert(END,sd[5])
              self.txtPrice.delete(0,END)
              self.txtPrice.insert(END,sd[6])                    
       def DeleteData():
              
              if(len(drug_name.get())!=0):
                     pb.deleteRec(drug_name.get(),batch_number.get())
                     clearData()
                     DisplayData()
       def searchDatabase():
              pharmalist.delete(0,END)
              for row in pb.searchData(drug_name.get(),batch_number.get(),MedicineType.get(),Manufacturer.get(),stock_quantity.get(),expiry_date.get(),Price.get()):
                     pharmalist.insert(END,row,str(""))       
       def update():
              if(len(drug_name.get())!=0):
                     pb.deleteRec(drug_name.get(),batch_number.get())
              if(len(drug_name.get())!=0):
                     pb.addStdRec(drug_name.get(),batch_number.get(),MedicineType.get(),Manufacturer.get(),stock_quantity.get(),expiry_date.get(),Price.get())
                     pharmalist.delete(0,END)
                     pharmalist.insert(END,(drug_name.get(),batch_number.get(),MedicineType.get(),Manufacturer.get(),stock_quantity.get(),expiry_date.get(),Price.get()))   

       #####################################FRAMES###################################################################
       MainFrame=Frame(self.root,bg="#032b45")
       MainFrame.grid()  #THIS IS MAIN FRAME OUR WINDOW
       TitFrame=Frame(MainFrame,bd=1,padx=54,pady=8,bg="#021e2f",relief=RIDGE)
       TitFrame.pack(side=TOP)#THIS IS STITLE FRAME
    
       self.lblTit=Label(TitFrame,font=('arial',30,'bold'),text="Pharmacy Database Management System",bg="#021e2f",fg="white")
       self.lblTit.grid()
              
       self.lblTit=Label(TitFrame,font=('arial',22),text="Naman Choudhary",bg="#021e2f",fg="white")
       self.lblTit.grid()

       self.lblTit=Label(TitFrame,font=('arial',18,'bold'),text="PES University",bg="#021e2f",fg="white")
       self.lblTit.grid()

       self.lblTit=Label(TitFrame,font=('arial',12),text="Electronic City",bg="#021e2f",fg="white")
       self.lblTit.grid()

       ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,bg="#021e2f",relief=RIDGE)
       ButtonFrame.pack(side=BOTTOM)#

       DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="#555",relief=RIDGE)
       DataFrame.pack(side=BOTTOM)#THIS IS STI
         
       DataFrameLeft=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="Black",relief=RIDGE,text="Medicine INFO\n")
       DataFrameLeft.pack(side=LEFT)

       DataFrameRight=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="Black",relief=RIDGE,text="Medicine DETAILS\n")
       DataFrameRight.pack(side=RIGHT)
#########################################################Lables and entry widget #######################################################################
       
       self.lbldrug_name=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Drug Name:",bg="#000000")
       self.lbldrug_name.grid(row=0,column=0,sticky=W)
       
       self.txtdrug_name=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=drug_name,bg="ghost white",fg="black",width=39)
       self.txtdrug_name.grid(row=0,column=1)#drug_name

       self.lblbatch_number=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Batch Number:",bg="#000000")
       self.lblbatch_number.grid(row=1,column=0,sticky=W)
       
       self.txtbatch_number=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=batch_number,bg="ghost white",fg="black",width=39)
       self.txtbatch_number.grid(row=1,column=1)#batch_number


       self.lblMedicineType=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Medicine Type:",bg="#000000")
       self.lblMedicineType.grid(row=2,column=0,sticky=W)
       
       self.txtMedicineType=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=MedicineType,bg="ghost white",fg="black",width=39)
       self.txtMedicineType.grid(row=2,column=1)#MedicineType

       self.lblManufacturer=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Manufacturer",bg="#000000")
       self.lblManufacturer.grid(row=3,column=0,sticky=W)
       
       self.txtManufacturer=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Manufacturer,bg="ghost white",fg="black",width=39)
       self.txtManufacturer.grid(row=3,column=1)#Manufacturer

       self.lblstock_quantity=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Stock Quantity:",bg="#000000")
       self.lblstock_quantity.grid(row=4,column=0,sticky=W)
       
       self.txtstock_quantity=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=stock_quantity,bg="ghost white",fg="black",width=39)
       self.txtstock_quantity.grid(row=4,column=1)#stock_quantity

       self.lblexpiry_date=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Expiry Date:",bg="#000000")
       self.lblexpiry_date.grid(row=5,column=0,sticky=W)
       
       self.txtexpiry_date=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=expiry_date,bg="ghost white",fg="black",width=39)
       self.txtexpiry_date.grid(row=5,column=1)#expiry_date

       self.lblPrice=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Price:",bg="#000000")
       self.lblPrice.grid(row=6,column=0,sticky=W)
       
       self.txtPrice=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Price,bg="ghost white",fg="black",width=39)
       self.txtPrice.grid(row=6,column=1)#Price


       ###############################List Box and ScrollBar Widget############################################
       scrollbar=Scrollbar(DataFrameRight)
       scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

       pharmalist=Listbox(DataFrameRight,width=68,height=12,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
       pharmalist.bind('<<ListboxSelect>>',Records)
       pharmalist.grid(row=0,column=0,padx=10)
       scrollbar.config(command= pharmalist.yview)

       #######################################Button Widget####################################################
       self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=addData)
       self.btnAddData.grid(row=0,column=0)#ADD NEW

       self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayData)
       self.btnDisplay.grid(row=0,column=1)#DISPLAY

       self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=clearData)
       self.btnClear.grid(row=0,column=2)#CLEAR

       self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DeleteData)
       self.btnDelete.grid(row=0,column=3)#DELETE

       self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=searchDatabase)
       self.btnSearch.grid(row=0,column=4)#SEARCH

       self.btnUpdate=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=update)
       self.btnUpdate.grid(row=0,column=5)#UPDATE

       self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=iExit)
       self.btnExit.grid(row=0,column=6)#EXIT

if __name__=='__main__':
   root=Tk()#CREATE AN OBJECT
   application=Med(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
   root.mainloop()#RUN UNTIL CLOSING THE WINDOW MANUALLY