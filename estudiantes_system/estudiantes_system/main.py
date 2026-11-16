from estudiantes import estudiante 
from tkinter import Tk,Label,Entry,Button,messagebox 

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Estudiantes")
        self.ventana.geometry("600x700")
        self.ventana.resizable(1,1)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
       self.borrarPantalla()
       Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
       Button(self.ventana,text="1.- Alumnos",command=self.menu_acciones).pack(pady=10)
       Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=10)
    
        
    def menu_acciones(self,tipo):
        self.borrarPantalla()
        Label(self.ventana,text=f"...::: Menu de Alumnos     :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)

def insertar_alumno_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Alumno").pack(pady=10)
        
        Label(self.ventana,text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana,text=":: Agregar ::",command=self.insertar_alumno_controller).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
       

def eliminar_alumno_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del alumno a eliminar...").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        Button(self.ventana,text=":: Eliminar ::",command=self.eliminar_alumno_controller).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
        













    def respuesta_sql(self,respuesta):
        if respuesta:
            input("...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")
    def menu_acciones(self,tipo):
            print(f"\t\t....:::: Menu de {tipo} ::::...\n")
            opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
            return opcion
    def menu_estudiante(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Estudiantes")
            match opc:
                case "1":
                    estudiantito= self.datos_estudiante("Estudiante")
                    estudiante1= estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    
                    respuesta= estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "2":
                    self.borrarPantalla()

                    id =input("Ingrese el ID del estudiante a eliminar: ").strip()
                    respuesta=estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del estudiante a eliminar: ").strip()
                    estudiantito=self.datos_estudiante(id)
                    estudiante1=estudiante.Estudiantes(
                        estudiantito['nombre'],
                        estudiantito['nota'],
                    )
                    respuesta=estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "4":
                    self.borrarPantalla()
                    registros=estudiante.Estudiantes.consultar()
                    num_estudiante=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\testudiante numero #: {num_estudiante}\n\t\tID: {fila[0]},\n\t\tNombre: {fila[1]}\n\t\tNota: {fila[2]}")
                            num_estudiante+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()
                case "5":
                    opc=False
                case _:
                    self.opcionInvalida()
              
    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\tIngresar los datos del {tipo}")
        estudiantito={}
        estudiantito['nombre']=input("Nombre: ").upper().strip()
        estudiantito['nota']=input("Nota: ").upper().strip()
        return estudiantito

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1- Estudiante\n\t2- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_estudiante()

                case "2":
                    self.borrarPantalla()
                    self.terminarSistema()
                    opcion=False
                case _:
                    self.opcionInvalida()    



if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
