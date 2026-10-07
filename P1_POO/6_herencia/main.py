"""   
  Herencia.-  la herencia es el hecho de que una clase puede permitir el uso o implementacion o compartir de los atributos y metodos. Es decir cuando una clase hereda a otra se dice que es una super clase, clase padre o principal que es la que hereda los atributos y metodos a la o las clases llamadas sub clases o clases hijas o secundaias
""" 

from coches import Coches, Camionetas, Camiones

coche1=Camiones('VW','Blanco','2022','220','150','5')
coche2=Coches('Nissan','Azul','2020','180','150','6')

camion1=Camiones('Dina','Negro','2020','180','300','12','8','2500')
camion2=Camiones('Star','Blanco','2019','150','200','14','6','2000')

camioneta1=Camiones('Renault','Amarillo','2025','240','250','8',"Delantera",True)
camioneta2=Camiones('Nissan','Blanca','2020','180','180','150','6',"Trasera", False)