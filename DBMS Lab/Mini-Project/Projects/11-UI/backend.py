import mysql.connector
#import `DBMS Proj`1_frontend

def PharmData():
        con = mysql.connector.connect(host="localhost",user="root",database="DBMS Proj")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Medicine (drug_name CHAR(255) NOT NULL,batch_number BIGINT NOT NULL,MedicineType CHAR(255) NOT NULL,Manufacturer CHAR(255) NOT NULL,stock_quantity BIGINT NOT NULL,expiry_date DATE NOT NULL,Price BIGINT NOT NULL,PRIMARY KEY (drug_name,batch_number))")
        con.commit()
        con.close()              
def addStdRec(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price):
        con=con = mysql.connector.connect(host="localhost",user="root")
        cur=con.cursor()
        cur.execute("use `DBMS Proj`")
        cur.execute("INSERT INTO Medicine VALUES(%s,%s,%s,%s,%s,%s,%s)",(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price))
        con.commit()
        con.close() 
def viewData():
        con=con = mysql.connector.connect(host="localhost",user="root")
        cur=con.cursor()
        cur.execute("use `DBMS Proj`")
        cur.execute("select * from Medicine")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(drug_name,batch_number):
        con=con = mysql.connector.connect(host="localhost",user="root")
        cur=con.cursor()
        cur.execute("use `DBMS Proj`")
        cur.execute("DELETE FROM Medicine WHERE drug_name=%s or batch_number=%s",(drug_name,batch_number))
        con.commit()
        con.close()         
def searchData(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price):
        con=con = mysql.connector.connect(host="localhost",user="root")
        cur=con.cursor()
        cur.execute("use `DBMS Proj`")
        cur.execute("SELECT * FROM Medicine WHERE drug_name=%s or batch_number=%s or MedicineType=%s or Manufacturer=%s or stock_quantity=%s or expiry_date=%s or Price=%s",(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,drug_name="",batch_number="",MedicineType="",Manufacturer="",stock_quantity="",expiry_date="",Price=""):
        con = mysql.connector.connect(host="localhost",user="root")
        cur=con.cursor()
        cur.execute("use `DBMS Proj`")
        cur.execute("UPDATE srkanth SET drug_name=%s,batch_number=%s,MedicineType=%s,Manufacturer=%s,stock_quantity=%s,expiry_date=%s,Price=%s WHERE id=%s",(drug_name,batch_number,MedicineType,Manufacturer,stock_quantity,expiry_date,Price))
        con.commit()
        con.close()    