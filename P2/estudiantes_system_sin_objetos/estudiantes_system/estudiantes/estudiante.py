import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexionBD import cursor, conexion

class Estudiantes:

    @staticmethod   
    def insertar (self, nombre, nota):
        try:
            cursor.execute("insert into estudiante values (null,%s,%s)",(nombre, nota))
            conexion.commit()
            return True
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False

    @staticmethod    
    def consultar():
        try: 
            cursor.execute("select * from estudiante")
            
            return cursor.fetchall()
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return []

    @staticmethod
    def eliminar(id):
        try: 
            cursor.execute("delete from estudiante where id=%s",(id,))
            conexion.commit()
            return True
        except: 
            return False 

    @staticmethod
    def actualizar( nombre, nota, id):
        try:

            cursor.execute("update estudiante set nombre=%s, nota=%s where id=%s",(nombre, nota, id))
            conexion.commit()
            return True 
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return False
