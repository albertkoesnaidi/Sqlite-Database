import sqlite3

conn=sqlite3.connect('Ariane_Database.db')
c=conn.cursor()


def customer_data():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS customer(
        cust_id text,
        tanggal_pasang text,
        nama text, 
        no_telp text,
        alamat text,
        koordinat text,
        kota text,
        tipe_tangki text,
        jumlah int,
        keterangan text
        )''')
    

def service_data():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS service(

            cust_id text,
            tanggal_service text,
            keterangan_service text)''')

def addcust_backend(cust_id, tanggal_pasang, nama, no_telp, alamat, koordinat, kota,tipe_tangki, jumlah, keterangan):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute("INSERT INTO customer VALUES (?,?,?,?,?,?,?,?,?,?)",(cust_id, tanggal_pasang, nama, no_telp, alamat, koordinat, kota,tipe_tangki, jumlah, keterangan))
    conn.commit()
    conn.close()

def viewdata_backend(): 
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customer")
    return c.fetchall()

def deletecust_backend(alamat):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute('DELETE FROM customer WHERE alamat=?',(alamat,))
    conn.commit()
    conn.close()

def updatedata_backend(cust_id="", tanggal_pasang="", nama="", no_telp="", alamat="", koordinat="", kota="", tipe_tangki="",jumlah="", keterangan=""):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute('UPDATE customer SET cust_id =?, tanggal_pasang=?, nama=?, no_telp=?, alamat=?, koordinat=?, kota=?,tipe_tangki=?, jumlah=?, keterangan=?')
    conn.commit()
    conn.close()

#"%"+alamat+"%", nama))
def searchdata_backend(cust_id="", alamat="", nama="",):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    if len(cust_id)!=0:
        c.execute("SELECT * FROM customer WHERE cust_id=?",(cust_id,))
        rows=c.fetchall()
    elif len (alamat)!=0:
        c.execute("SELECT * FROM customer WHERE alamat LIKE ?",("%"+alamat+"%",))
        rows=c.fetchall()
    elif len(nama) !=0:
        c.execute("SELECT * FROM customer WHERE nama LIKE ?",("%"+nama+"%",))
        rows=c.fetchall()
    else:
        c.execute("SELECT * FROM customer WHERE cust_id=? OR alamat LIKE ?",(cust_id,"%"+alamat+"%",))
        rows=c.fetchall()
    conn.close()
    return rows
 
    

#########################################################Service#################################################### 

def addserv_backend(cust_id, tanggal_service, keterangan_service):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute("INSERT INTO service VALUES (?,?,?)",(cust_id, tanggal_service, keterangan_service))
    conn.commit()
    conn.close()

def viewservice_backend(cust_id): 
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute("SELECT  tanggal_service, keterangan_service FROM service WHERE cust_id=?",(cust_id,))
    return c.fetchall()
   

def deleteservice_backend(tanggal_service):
    conn=sqlite3.connect('Ariane_Database.db')
    c=conn.cursor()
    c.execute("DELETE FROM service WHERE tanggal_service=?",(tanggal_service,))
    conn.commit()
    conn.close()




customer_data()
service_data()

conn.commit()
conn.close()

