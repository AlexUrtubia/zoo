class Animal ():
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = nivel_salud
        self.nivel_felicidad = nivel_felicidad
        
    def alimentar(self):
        self.nivel_felicidad += 10
        self.nivel_salud += 10
        return self
    
    def mostar_info(self):
        print("*"*20)
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Nivel salud: ",self.nivel_salud)
        print("Nivel felicidad: ",self.nivel_felicidad)
        return self
        
class Panda(Animal):
    def __init__(self, nombre, edad, nivel_salud=90, nivel_felicidad=90):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
    
    def alimentar(self):
        self.nivel_felicidad += 12
        self.nivel_salud += 5
        return self
        
class Elefante(Animal):
    def __init__(self, nombre, edad, tipo, nivel_salud=80, nivel_felicidad=45):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.tipo = tipo
        
    def alimentar(self):
        self.nivel_felicidad += 5
        self.nivel_salud += 12
        return self
    
    def mostar_info(self):
        super().mostar_info()
        print("Tipo:",self.tipo)
        return self
    
class Tigre(Animal):
    def __init__(self, nombre, edad, nivel_salud=75, nivel_felicidad=55):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
    def alimentar(self):
        self.nivel_felicidad += 5
        self.nivel_salud += 5
        return self
    
class Mandril(Animal):
    def __init__(self, nombre, edad, nivel_salud=65, nivel_felicidad=85):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        
    def alimentar(self):
        self.nivel_felicidad += 13
        self.nivel_salud += 9
        return self
    
# panda1 = Panda("Pili",5).mostar_info()
# panda2 = Panda("Santi",6,nivel_salud=68,nivel_felicidad=76).mostar_info()
# panda2.alimentar().mostar_info()

# elef1 = Elefante("Agusto",21,"africano").mostar_info()
# elef1.alimentar().mostar_info()

# mandril1 = Mandril("Tito",2).mostar_info()
# mandril2 = Mandril("Juna",12,nivel_felicidad=62).alimentar().mostar_info()

# tigre1 = Tigre("Justin",5,nivel_salud=90).alimentar().mostar_info()

class Zoo:
    def __init__(self, zoo_name):
        self.animales = []
        self.name = zoo_name
        
    #def add_panda(self, nombre ,edad):
    #    self.animales.append( Panda(nombre,edad))
        
    #def add_elefante(self, nombre, edad, tipo):
    #    self.animales.append( Elefante(nombre, edad, tipo))
        
    #def add_tigre(self, nombre ,edad):
    #    self.animales.append( Tigre(nombre,edad))
        
    #def add_mandril(self, nombre ,edad):
    #    self.animales.append( Mandril(nombre,edad))
        
    def add_animal(self,Especie,nombre,edad):
        self.animales.append(Especie(nombre, edad))
        return self
        
    def alimentar_animales(self):
        for Animal in self.animales:
            Animal.alimentar()
        return self
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for Animal in self.animales:
            Animal.mostar_info()
        return self
            
zoo1 = Zoo("Zoologicofeo")
zoo1.add_elefante("uno",1,"asiatico")
zoo1.add_mandril("Julio",4)
zoo1.add_panda("Piti",2)
zoo1.add_tigre("Khan",7)
zoo1.print_all_info()

zoo1.alimentar_animales().print_all_info()
https://www.youtube.com/watch?v=bxhXQG1qJPM