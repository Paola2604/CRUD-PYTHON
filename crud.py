from tkinter import *
from tkinter import messagebox 
import sqlite3 
#------------ FUNCIONES--------------#
def conexbbdd():
    miconexion=sqlite3.connect("Usuario")
    micursor=miconexion.cursor()
    try:
        micursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR (8),
            APELLIDO VARCHAR (10),
            DIRECCION VARCHAR (30)
            )               
            ''')
        miconexion.commit()
        miconexion.close()            
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion!", "La base de datos ya existe!")
def saliraplicacion():
    valor=messagebox.askquestion("Salir","¿Esta seguro que desea salir de la aplicación?")
    if(valor=="yes"):
        root.destroy()
def limpiarCampos():
    minombre.set("")  
    miId.set("")     
    miapellido.set("") 
    mipassword.set("") 
    midireccion.set("")    
        
def crear():
    miconexion=sqlite3.connect("Usuario")      
    micursor=miconexion.cursor()
    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + minombre.get() + 
        "','" + mipassword.get() +
        "','"+ miapellido.get() + 
        "','"+ midireccion.get()+ "')")
    
    if miId.get()!="":
        messagebox.showwarning("Atencion!", "el campo ID debe estar vacio!")
        miconexion.close()
    else:
        miconexion.commit()
        messagebox.showinfo("ÉXITO","Registro creado con exito")
        limpiarCampos()
    miconexion.close()

def leer():
    miconexion=sqlite3.connect("Usuario")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    elusurio=micursor.fetchall() ##convierte a un array los datos de la tabla
    for usuario in elusurio:
        miId.set(usuario[0])
        minombre.set(usuario[1])
        miapellido.set(usuario[3])
        mipassword.set(usuario[2])
        midireccion.set(usuario[4])
        
    miconexion.commit()
    
def actualizar():
    miconexion=sqlite3.connect("Usuario")      
    micursor=miconexion.cursor()
    micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + minombre.get() + 
        "', PASSWORD= '" + mipassword.get() +
        "', APELLIDO='"+ miapellido.get() + 
        "',DIRECCION='"+ midireccion.get()+ "'WHERE ID="+ miId.get()) 
    miconexion.commit()
     
    messagebox.showinfo("ÉXITO","Registro acualizado con exito")
    limpiarCampos()
    miconexion.close()    
    
def borrar():
    miconexion=sqlite3.connect("Usuario")
    micursor=miconexion.cursor()
    micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    valor=messagebox.askquestion("BBDD","¿Esta seguro que desea eliminar el registro?")
    if(valor=="yes"):
        miconexion.commit()
        messagebox.showinfo("BBDD","Registro eliminado con exito")
        limpiarCampos()
#-------------- MENU -----------------------#   
root=Tk()
barramenu=Menu(root)
fondobg="#1FEE9C"
root.config(menu=barramenu, width=300,height=300,background=fondobg)

bbddMenu=Menu(barramenu,tearoff=0,borderwidth=2)
bbddMenu.add_command(label="Conectar", command=conexbbdd)
bbddMenu.add_command(label="Salir",command=saliraplicacion)

borrarMenu=Menu(barramenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barramenu,tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=borrar)

ayudaMenu=Menu(barramenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barramenu.add_cascade(label="BBDD",menu=bbddMenu)
barramenu.add_cascade(label="Borrar",menu=borrarMenu)
barramenu.add_cascade(label="CRUD",menu=crudMenu)
barramenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#---------------------------------------------#

#-------------- FRAME 1 ----------------------------#
frame1=Frame(root)
frame1.pack(fill="both", expand="True")
frame1.config(width=300,height=300,bg=root.cget('bg'))

miId=StringVar()
minombre=StringVar()
mipassword=StringVar()
miapellido=StringVar()
midireccion=StringVar()


id=Label(frame1,text="Id:",fg="black",font=18,bg=fondobg).grid(row=2,column=0,sticky="e")
cuadroid=Entry(frame1,textvariable=miId)
cuadroid.grid(row=2,column=1,pady=10,columnspan=4)
cuadroid.config(background="white", fg="black", justify="right")

nombre=Label(frame1,text="Nombre:",fg="black",font=18,bg=fondobg).grid(row=3,column=0,sticky="e")
cuadronombre=Entry(frame1,textvariable=minombre)
cuadronombre.grid(row=3,column=1,pady=10,columnspan=4)
cuadronombre.config(background="white", fg="black", justify="right")

password=Label(frame1,text="Password:",fg="black",font=18,bg=fondobg).grid(row=4,column=0,sticky="e")
cuadropas=Entry(frame1,textvariable=mipassword)
cuadropas.grid(row=4,column=1,pady=10,columnspan=4)
cuadropas.config(background="white", fg="black", justify="right",show="*")

apellido=Label(frame1,text="Apellido:",fg="black",font=18,bg=fondobg).grid(row=5,column=0,sticky="e")
cuadroapellido=Entry(frame1,textvariable=miapellido)
cuadroapellido.grid(row=5,column=1,pady=10,columnspan=4)
cuadroapellido.config(background="white", fg="black", justify="right")

direccion=Label(frame1,text="Dirección:",fg="black",font=18,bg=fondobg).grid(row=6,column=0,sticky="e")
cuadrodir=Entry(frame1,textvariable=midireccion)
cuadrodir.grid(row=6,column=1,pady=10,columnspan=4)
cuadrodir.config(background="white", fg="black", justify="right")

frame2=Frame(root)
frame2.pack()
frame2.config(width=300,height=300,bg=root.cget('bg'))

boton1=Button(frame2,text="Crear", width=8,bg="white", command=crear).grid(row=0,column=0)
boton2=Button(frame2,text="Leer", width=8,bg="white",command=leer).grid(row=0,column=1)
boton1=Button(frame2,text="Actualizar", width=8,bg="white",command=actualizar).grid(row=0,column=2)
botonres=Button(frame2,text="Borrar", width=8,bg="white",command=borrar).grid(row=0,column=3)
root.mainloop()