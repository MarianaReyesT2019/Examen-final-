from tkinter import *

root = Tk()

ancho = 460
alto = 250

root.geometry(str(ancho)+"x"+str(alto))
root.title("Examen Final Mariana Reyes ")

saludo = Label(text="Bienvenidos",font=("Times New Roman",20)).place(x=150,y=5)

lblname=Label(text="Nombre",font=("Arial",11)).place(x=70,y=30)
entrada=StringVar()
txtnombre=Entry(root,textvariable=entrada).place(x=135,y=40)

lblape=Label(text="Apellido",font=("Arial",11)).place(x=80,y=60)
entrada=StringVar()
txtape=Entry(root,textvariable=entrada).place(x=135,y=70)

lbldia=Label(text="Día ",font=("Arial",11)).place(x=80,y=90)
entrada=StringVar()
txtdia=Entry(root,textvariable=entrada).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Arial",11)).place(x=80,y=120)
entrada=StringVar()
txtmes=Entry(root,textvariable=entrada).place(x=135,y=130)

lblaño=Label(text="Año",font=("Arial",11)).place(x=80,y=150)
entrada=StringVar()
txtaño=Entry(root,textvariable=entrada).place(x=135,y=160)









root.mainloop()