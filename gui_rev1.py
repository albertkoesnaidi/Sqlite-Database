from os import stat_result
from tkinter import Tk, Label, Frame, RIDGE, TOP, BOTTOM, LEFT, RIGHT, LabelFrame, W, StringVar, IntVar, \
Entry, END, Text, Button, Scrollbar, Listbox, Y, HORIZONTAL, X
from tkinter import ttk
from tkinter import messagebox
#from tkinter.constants import HORIZONTAL
import dbase_backend
import time



class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title('Customer Database')
        self.root.geometry('2050x1350+0+0')
        self.root.config(bg='olive drab')

        cust_id=StringVar()
        tanggal_pasang=StringVar()
        nama=StringVar()
        no_telp=StringVar()
        alamat=StringVar()
        koordinat=StringVar()
        kota=StringVar()  
        jumlah=IntVar()
        tanggal_service=StringVar()

        
#####################################################Functions#############################################
        def iExit():
                iExit=messagebox.askyesno('Customer Database Management Systems', 'Confirm if you want to exit')
                if iExit>0:
                        root.destroy()

        def clearData():
                self.txtcust_id.delete(0,END)
                self.txttanggal_pasang.delete(0,END)
                self.txtnama.delete(0,END)
                self.txtno_telp.delete(0,END)
                self.txtalamat.delete(0,END)
                self.txtkoordinat.delete(0,END)
                self.txtkota.delete(0,END)
                self.txtjumlah.delete(0,END)
                self.comboboxtipe_tangki.set('')
                self.txtketerangan_pasang.delete(1.0,END)
                detailslist.delete(0,END)
                ###Service###
                self.txttipe_tangki.delete(0,END)
                self.txttanggal_service.delete(0,END)
                self.txtketerangan_service.delete(1.0,END)
                servicelist.delete(0,END)
        
        def CustomerRec(event):
                global index_customer
                b=detailslist.curselection()
                if len(b)>0:
                        searchCust=detailslist.curselection()[0]
                        index_customer=detailslist.get(searchCust)
                        self.txtcust_id.delete(0,END)
                        self.txtcust_id.insert(END,index_customer[0])
                        self.txttanggal_pasang.delete(0,END)
                        self.txttanggal_pasang.insert(END,index_customer[1])
                        self.txtnama.delete(0,END)
                        self.txtnama.insert(END,index_customer[2])
                        self.txtno_telp.delete(0,END)
                        self.txtno_telp.insert(END,index_customer[3])
                        self.txtalamat.delete(0,END)
                        self.txtalamat.insert(END,index_customer[4])
                        self.txtkoordinat.delete(0,END)
                        self.txtkoordinat.insert(END,index_customer[5])
                        self.txtkota.delete(0,END)
                        self.txtkota.insert(END,index_customer[6])
                        self.txttipe_tangki.delete(0,END)
                        self.txttipe_tangki.insert(END,index_customer[7])
                        self.txtjumlah.delete(0,END)
                        self.txtjumlah.insert(END,index_customer[8])
                        self.txtketerangan_pasang.delete(1.0,END)
                        self.txtketerangan_pasang.insert(END,index_customer[9])
                        

        def adddata_frontend():
                if(len(cust_id.get())!=0):
                        dbase_backend.addcust_backend(cust_id.get(), tanggal_pasang.get(), nama.get(), no_telp.get(), alamat.get(), koordinat.get(), kota.get(),self.comboboxtipe_tangki.get(), jumlah.get(), self.txtketerangan_pasang.get(1.0,END))
                        detailslist.delete(0,END)
                        detailslist.insert(END,(cust_id.get(), tanggal_pasang.get(), nama.get(), no_telp.get(),alamat.get(), koordinat.get(), kota.get(), self.comboboxtipe_tangki.get(), jumlah.get(), self.txtketerangan_pasang.get(1.0,END)))
                        
        def displaydata_frontend():
                detailslist.delete(0,END)
                for i in dbase_backend.viewdata_backend():
                        detailslist.insert(END,i,str(""))

        
        def searchdata_frontend():
                detailslist.delete(0,END)
                for i in dbase_backend.searchdata_backend(cust_id.get(), alamat.get()):
                        detailslist.insert(END,i,str(""))
        
        def deletedata_frontend():
                if(len(alamat.get())!=0):
                        dbase_backend.deletecust_backend(index_customer[4])
                        clearData()
                        displaydata_frontend()

        def updatedata_frontend():
                if(len(cust_id.get())!=0):
                        dbase_backend.deletecust_backend(index_customer[4])
                if(len(cust_id.get())!=0):
                        dbase_backend.addcust_backend(cust_id.get(), tanggal_pasang.get(), nama.get(), no_telp.get(),alamat.get(), koordinat.get(), kota.get(),self.comboboxtipe_tangki.get(), jumlah.get(), self.txtketerangan_pasang.get(1.0,END))
                        detailslist.delete(0,END)
                        detailslist.insert(END,(cust_id.get(), tanggal_pasang.get(), nama.get(), no_telp.get(), alamat.get(), koordinat.get(), kota.get(),self.comboboxtipe_tangki.get(), jumlah.get(), self.txtketerangan_pasang.get(1.0,END)))

        def ServiceRec(event):
                global index_service
                c=servicelist.curselection()
                if len(c)>0:
                        searchServ=servicelist.curselection()[0]
                        index_service=servicelist.get(searchServ)
                        self.txttanggal_service.delete(0,END)
                        self.txttanggal_service.insert(END,index_service[0])
                        self.txtketerangan_service.delete(1.0,END)
                        self.txtketerangan_service.insert(END,index_service[1])
                

        def addservice_frontend():
                if(len(cust_id.get())!=0):
                        dbase_backend.addserv_backend(cust_id.get(),tanggal_service.get(), self.txtketerangan_service.get(1.0,END))
                        servicelist.delete(0,END)
                        servicelist.insert(END, cust_id.get(),tanggal_service.get(), self.txtketerangan_service.get(1.0,END))
        
        def displayservice_frontend():
                servicelist.delete(0,END)
                for i in dbase_backend.viewservice_backend(cust_id.get()):
                        servicelist.insert(END,i,str(""))
                
        def deleteservice_frontend():
                if(len(tanggal_service.get())!=0):
                        dbase_backend.deleteservice_backend(index_service[0])
                        clearData()
                        displayservice_frontend()

        def tanggal():
                tanggal=time.strftime("%d.%m.%Y")
                self.tanggalLabel.config(text=tanggal)
        
        def clock():
                clockdate=time.strftime("%H:%M:%S")
                self.clockLabel.config(text=clockdate)
                self.clockLabel.after(200,clock)

#####################################################Frames#############################################
        
        MainFrame=Frame(self.root, bg='olive drab')
        MainFrame.grid()
        TitleFrame=Frame(MainFrame, bd=2, padx=70, pady=20, bg='Ghost white',relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.TitleLabel=Label(TitleFrame, font=('Arial',20,'bold'),text='Customer database',width=24,height=1,bg='Ghost white')
        self.TitleLabel.grid(row=0, column=2)
        self.tanggalLabel=Label(TitleFrame, text="", font=('arial',15,'bold'),bg='ghost white')
        self.tanggalLabel.grid(row=0, column=0)
        self.clockLabel=Label(TitleFrame, text="", font=('arial',15,'bold'),bg='ghost white')
        self.clockLabel.grid(row=1,column=0)
        tanggal()
        clock()

        ButtonFrame=Frame(MainFrame, bd=2, width=200, height=200, padx=18, pady=10, bg='olive drab', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        #ButtonFrameEXIT=Frame(ButtonFrame, bd=2, width=80, height=50, padx=18, pady=10, bg='olive drab', relief=RIDGE)
        #ButtonFrameEXIT.pack(side=BOTTOM)
        #ButtonFrameTOP=Frame(ButtonFrame, bd=2, width=80, height=200, padx=18, pady=10, bg='olive drab', relief=RIDGE)
        #ButtonFrameTOP.pack(side=TOP)
        #ButtonFrameBOTTOM=Frame(ButtonFrame, bd=2, width=80, height=200, padx=18, pady=10, bg='olive drab', relief=RIDGE)
        #ButtonFrameBOTTOM.pack(side=BOTTOM)
        

        ServiceFrame=Frame(MainFrame, bd=1, width=1200, height=300, padx=20, pady=20, bg='olive drab', relief=RIDGE)
        ServiceFrame.pack(side=BOTTOM)
        DataFrame=Frame(MainFrame, bd=1, width=1500, height=500, padx=20, pady=20, bg='olive drab', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        ###Service###
        ServiceFrameLEFT=LabelFrame(ServiceFrame, bd=1, width=700, height=200, padx=10, relief=RIDGE, bg='Ghost white',font=('arial',20,'bold'),text='Service info\n')
        ServiceFrameLEFT.pack(side=LEFT)
        ServiceFrameRIGHT=LabelFrame(ServiceFrame, bd=1, width=700, height=200, padx=31, pady=3, relief=RIDGE, bg='ghost white',font=('arial',18,'bold'),text='Service details\n')
        ServiceFrameRIGHT.pack(side=RIGHT)

        DataFrameLEFT=LabelFrame(DataFrame, bd=1, width=1100, height=500, padx=10, relief=RIDGE, bg='Ghost white',font=('arial',20,'bold'),text='Customer info\n')
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT=LabelFrame(DataFrame, bd=1, width=900, height=300, padx=31, pady=3, relief=RIDGE, bg='ghost white',font=('arial',18,'bold'),text='Detail info\n')
        DataFrameRIGHT.pack(side=RIGHT)
        

#############################################Scrollbar and Listbox#############################################

        scrlbar_detailslist_y=Scrollbar(DataFrameRIGHT)
        scrlbar_detailslist_y.pack(side=RIGHT, fill=Y)
        scrlbar_detailslist_x=Scrollbar(DataFrameRIGHT, orient=HORIZONTAL)
        scrlbar_detailslist_x.pack(side=BOTTOM, fill=X)
        detailslist=Listbox(DataFrameRIGHT, width=50, height=10, font=('arial',12,'bold'),yscrollcommand=scrlbar_detailslist_y.set, xscrollcommand=scrlbar_detailslist_x.set)
        detailslist.bind('<<ListboxSelect>>',CustomerRec)
        detailslist.pack()
        scrlbar_detailslist_y.config(command=detailslist.yview)
        scrlbar_detailslist_x.config(command=detailslist.xview)

        ###Service###
        scrlbar_servicelist_y=Scrollbar(ServiceFrameRIGHT)
        scrlbar_servicelist_y.pack(side=RIGHT, fill=Y)
        scrlbar_servicelist_x=Scrollbar(ServiceFrameRIGHT,orient=HORIZONTAL)
        scrlbar_servicelist_x.pack(side=BOTTOM,fill=X)
        servicelist=Listbox(ServiceFrameRIGHT,width=50, height=6, font=('arial',12,'bold'),yscrollcommand=scrlbar_servicelist_y.set, xscrollcommand=scrlbar_servicelist_x.set)
        servicelist.bind('<<ListboxSelect>>',ServiceRec)
        servicelist.pack()
        scrlbar_servicelist_y.config(command=servicelist.yview)
        scrlbar_servicelist_x.config(command=servicelist.xview)


#############################################Labels and Entry#############################################
        self.Labelcust_id=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Customer ID: ', padx=2, pady=2, bg='Ghost white')
        self.Labelcust_id.grid(row=0, column=0, sticky=W)
        self.txtcust_id=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=cust_id,width=30)
        self.txtcust_id.grid(row=0,column=1)

        self.Labeltanggal_pasang=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Tanggal Pasang: ', padx=2, pady=2, bg='Ghost white')
        self.Labeltanggal_pasang.grid(row=1, column=0, sticky=W)
        self.txttanggal_pasang=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=tanggal_pasang,width=30)
        self.txttanggal_pasang.grid(row=1,column=1)

        self.Labelnama=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Nama: ', padx=2, pady=2, bg='Ghost white')
        self.Labelnama.grid(row=2, column=0, sticky=W)
        self.txtnama=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=nama,width=30)
        self.txtnama.grid(row=2,column=1)

        self.Labelno_telp=Label(DataFrameLEFT, font=('arial',12,'bold'),text='No. Telp: ', padx=2, pady=2, bg='Ghost white')
        self.Labelno_telp.grid(row=3, column=0, sticky=W)
        self.txtno_telp=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=no_telp,width=30)
        self.txtno_telp.grid(row=3,column=1)

        self.Labelalamat=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Alamat: ', padx=2, pady=2, bg='Ghost white')
        self.Labelalamat.grid(row=4, column=0, sticky=W)
        self.txtalamat=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=alamat,width=30)
        self.txtalamat.grid(row=4,column=1)

        self.Labelkoordinat=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Koordinat: ', padx=2, pady=2, bg='Ghost white')
        self.Labelkoordinat.grid(row=5, column=0, sticky=W)
        self.txtkoordinat=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=koordinat,width=30)
        self.txtkoordinat.grid(row=5,column=1)


        self.Labelkota=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Kota: ', padx=2, pady=2, bg='Ghost white')
        self.Labelkota.grid(row=6, column=0, sticky=W)
        self.txtkota=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=kota,width=30)
        self.txtkota.grid(row=6,column=1)

        self.Labeltipe_tangki=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Tipe Tangki: ', padx=2, pady=2, bg='Ghost white')
        self.Labeltipe_tangki.grid(row=7, column=0, sticky=W)
        self.comboboxtipe_tangki=ttk.Combobox(DataFrameLEFT,font=('arial',12,'bold'),state='readonly',width=30)
        self.comboboxtipe_tangki ['value']=('', '100 Coil', '100 DT', '150 DT', '200 Coil', '300 DT', '300 Coil', '150 Flat SS', 
        '300 Flat SS', '150 Flat SS Bluetech', '300 Flat SS Bluetech', '150 Enamel', '300 Enamel', '150 Spit', '300 Split')
        self.comboboxtipe_tangki.bind('<<Comboboxselection>>',CustomerRec)
        self.comboboxtipe_tangki.current(0)
        self.comboboxtipe_tangki.grid(row=7,column=1)

        self.Labeljumlah=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Jumlah: ', padx=2, pady=2, bg='Ghost white')
        self.Labeljumlah.grid(row=8, column=0, sticky=W)
        self.txtjumlah=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=jumlah,width=30)
        self.txtjumlah.grid(row=8,column=1)
        self.txtjumlah.delete(0,END)

        self.Labelketerangan_pasang=Label(DataFrameLEFT, font=('arial',12,'bold'),text='Keterangan: ', padx=2, pady=2, bg='Ghost white')
        self.Labelketerangan_pasang.grid(row=9, column=0, sticky=W)
        self.txtketerangan_pasang=Text(DataFrameLEFT, font=('arial',12,'bold'),width=30, height=2)
        self.txtketerangan_pasang.grid(row=9,column=1)


        ###Service###
        self.Labeltipe_tangki=Label(ServiceFrameLEFT, font=('arial',12,'bold'),text='Tipe tangki: ', padx=2, pady=2, bg='Ghost white')
        self.Labeltipe_tangki.grid(row=0, column=0, sticky=W)
        self.txttipe_tangki=Entry(ServiceFrameLEFT, font=('arial',12,'bold'), width=30)
        self.txttipe_tangki.grid(row=0,column=1)

        self.Labeltanggal_service=Label(ServiceFrameLEFT, font=('arial',12,'bold'),text='Tanggal Service: ', padx=2, pady=2, bg='Ghost white')
        self.Labeltanggal_service.grid(row=1, column=0, sticky=W)
        self.txttanggal_service=Entry(ServiceFrameLEFT, font=('arial',12,'bold'),textvariable= tanggal_service, width=30)
        self.txttanggal_service.grid(row=1,column=1)

        self.Labelketerangan_service=Label(ServiceFrameLEFT, font=('arial',12,'bold'),text='Keterangan service: ', padx=2, pady=2, bg='Ghost white')
        self.Labelketerangan_service.grid(row=2, column=0, sticky=W)
        self.txtketerangan_service=Text(ServiceFrameLEFT, font=('arial',12,'bold'),width=30, height=2)
        self.txtketerangan_service.grid(row=2,column=1)



#############################################Button Widget#############################################

        self.btnaddnew=Button(ButtonFrame, text='Add New', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=adddata_frontend)
        self.btnaddnew.grid(row=0, column=0)
        self.btnclear=Button(ButtonFrame, text='Clear', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=clearData)
        self.btnclear.grid(row=0, column=1)
        self.btndelete=Button(ButtonFrame, text='Delete', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=deletedata_frontend)
        self.btndelete.grid(row=0, column=2)
        self.btnupdate=Button(ButtonFrame, text='Update', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=updatedata_frontend)
        self.btnupdate.grid(row=0, column=3)
        self.btnsearch=Button(ButtonFrame, text='Search', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=searchdata_frontend)
        self.btnsearch.grid(row=0, column=4)

        self.btnservice=Button(ButtonFrame, text='Add Service', font=('arial',12, 'bold'),height=1, width=10, bg='light salmon', bd=4, command=addservice_frontend)
        self.btnservice.grid(row=0, column=5)
        self.btnserdisplay=Button(ButtonFrame, text='Disp Service', font=('arial',12, 'bold'),height=1, width=10, bd=4, bg='light salmon',command=displayservice_frontend)
        self.btnserdisplay.grid(row=0, column=6)
        self.btnserdisplay=Button(ButtonFrame, text='Del Service', font=('arial',12, 'bold'),height=1, width=10, bd=4, bg='light salmon',command=deleteservice_frontend)
        self.btnserdisplay.grid(row=0, column=7)

        self.btnexit=Button(ButtonFrame, text='Exit', font=('arial',12, 'bold'),height=1, width=10, bd=4, command=iExit)
        self.btnexit.grid(row=0, column=8)


if __name__=='__main__':
    root=Tk()
    application=Customer(root)
    root.mainloop()