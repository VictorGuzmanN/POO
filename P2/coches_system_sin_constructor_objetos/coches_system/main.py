from coches import coches, cochesBD
print("\033c")

class App:
    def __init__(self):
        self.main()
    
    def borrarPantalla(self):
        print("\033c")
        
    def esperarTecla(self):
        input("...¡Oprima cualquier tecla para contunuar!...")
    def terminarSistema(self):
        input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")
    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self,tipo):
        print(f"\t\t....:::: Menu de {tipo} ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
        return opcion
    def menu_cocches(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case "1":
                    ##solicitar datos y crear objeto de Coches
                    cochesito= self.datos_coches("Coches")
                    coches1= coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    coches1= cochesBD.CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    '''
                    ## Mi metodo para ingresar los datos
                    cocheBD1=cochesBD.CochesBD(coches1.getMarca(),coches1.getColor(),coches1.getModelo(),coches1.getVelocidad(),coches1.getPotencia(),coches1.getAsientos())
                    '''
                    respuesta= coches1.insertar()
                    self.respuesta_sql(respuesta)
                    ##borrar objeto que no utilizas
                    del coches1
                case "2":
                    self.borrarPantalla()
                    # En lugar de solo .strip(), conviértelo a entero int()
                    id = int(input("Ingrese el ID del coche a actualizar: ").strip())
                    respuesta=cochesBD.CochesBD.eliminar(id)

                    self.respuesta_sql(respuesta)
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coches(id)
                    coches1 = cochesBD.CochesBD(
                        cochesito['marca'],
                        cochesito['color'],
                        cochesito['modelo'],
                        cochesito['velocidad'],
                        cochesito['potencia'],
                        cochesito['asientos']
                    )
                    respuesta=coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                case "4":
                    self.borrarPantalla()
                    #coches1=cochesBD.CochesBD('','','',0,0,0)
                    registros=cochesBD.CochesBD.consultar()
                    
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tCoche numero #: {num_coche}\n\t\tID: {fila[0]},\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]},\n\t\tVelocidad: {fila[4]},\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()
                    #del coches1
                case "5":
                    opc=False
                case _:
                    self.opcionInvalida()
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")
            
    def datos_coches(self,tipo):
        self.borrarPantalla()
        print(f"\n\tIngresar los datos del {tipo}")
        cochesito={}
        cochesito['marca']=input("Marca: ").upper().strip()
        cochesito['color']=input("Color: ").upper().strip()
        cochesito['modelo']=input("Modelo: ").upper().strip()
        cochesito['velocidad']=input("Velocidad: ").strip()
        cochesito['potencia']=input("Potencia: ").strip()
        cochesito['asientos']=input("Asientos: ").strip()
        return cochesito
        '''
        datos_valido=False
        while datos_valido ==False:
            try:
                marca=input("Ingrese la marca: ").lower().strip()
                color=input("Ingrese el color: ").lower().strip()
                modelo=input("Ingrese el modelo: ").lower().strip()
                velocidad=int(input("Ingrese la velocidad: "))
                potencia=int(input("Ingrese la potencia: "))  
                asientos=int(input("Ingrese el numero de asientos: ")) 
                datos_valido=True

            except:
                print("datos erroneos, verifica por favor.....")  
                
        if datos_valido:
            coche1=coches.Coches(marca,color,modelo,velocidad,potencia,asientos)
            return coche1
        '''
    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1- Coches\n\t2- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_cocches()

                case "2":
                    self.borrarPantalla()
                    self.terminarSistema()
                    opcion=False
                case _:
                    self.opcionInvalida()
if __name__=="__main__":
    app=App()
