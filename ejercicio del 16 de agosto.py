

class Empresa:
    def __init__(self,nom= "El mas barato",ruc="09999999" ,tel="09891663609",dir="Pedro Carbo"):
        self.nombre = nom 
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dir

    def mostrarEmpresa(self):
        print("Empresa: {:20} Ruc: {}".format(self.nombre,self.ruc))

class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono= tel


    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion=promocion

    @property
    #getter: obtener el valor del atributo privado
    def promocion(self):
        if self.__promocion == True:
            return "10% Descuento"
        else:
            return "No hay Promocion"

    # @contrato.setter
    # def contrato(self,value): #setter: asigna un valor al atributo privado
    #     self.__contrato = value


    def mostrarCliente(self):
        print(self.nombre,self.promocion)

# class ClienteCorporativo(Cliente):
#     def __init__(self,contrato):
#         self.__contrato=contrato

#     @property
#     # getter: obtener el valor del atributo privado
#     def contrato(self):
#         return self.__contrato

#     @contrato.setter
#     def contrato(self,value): #setter: asigna un valor al atributo privado
#         self.__contrato = value


#     def mostrarCliente(self):
#         print(self.nombre)

# emp= Empresa()
# emp.mostrarEmpresa()
# print(emp.nombre)

cli1= ClientePersonal("Luis","099999394","098982432",True)
cli1.mostrarCliente()