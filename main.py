from warnings import catch_warnings
class Cliente:
    def __init__(self, nit, nombre):
        self.__nit = nit
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    def get_nit(self):
        return self.__nit
    def __str__(self):
        return f"Nombre: {self.get_nombre()} | NIT: {self.get_nit()}"

class Producto:
    def __init__(self,codigo ,nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    def get_codigo(self):
        return self.__codigo
    def get_nombre_producto(self):
        return self.__nombre
    def get_precio_producto(self):
        return self.__precio

    def __str__(self):
        return f"Cod: {self.get_codigo()} | Producto: {self.get_nombre_producto()} | Precio: {self.get_precio_producto()}"

class Pedidos:
    #Para generar un pedido se necesita un objeto tipo ṕedido y un objeto tipo cliente
    def __init__(self, cliente):
        self.cliente = cliente #Datos del cliente
        self.productos = {} #El producto queda guardado como un diccionario de productos
        self.urgente = False
        self.entregado = False
        self.sub_total = 0

    def get_tipo_pedido(self):
        return self.urgente
    def get_pedido_entregado(self):
        return self.entregado

    def agregar_a_pedido(self, producto, cantidad):
        producto_agregado = producto #se agrega al pedido que el cliente esta realizando
        self.sub_total = producto_agregado.get_precio_producto() * cantidad
    def __str__(self):
        return f"Producto {self.productos} | NIT Cliente: {self.cliente.get_nit()}"



class Notificar:
    def __init__(self):
        notificaciones = {}

    def pedido_urgente(self, pedido):
        tipo = pedido.get_tipo_pedido
        if tipo:
            print('Pedido Urgente')
        else:
            print('Pedido Normal')
    def pedido_entregado(self, pedido):
        estado = pedido.get_pedido_entregado()
        if estado != True:
            print('Pedido En Camino')
        else:
            print('Pedido Entregado')

class Gestion:
    def __init(self):
        self.diccionario_productos = {}
        self.diccionario_pedidos = {}
        self.diccionario_clientes = {}


    def existencia_codigo(self, codigo):
        if codigo in self.diccionario_productos:
            return True
        else:
            return False


    def vender(self):
        fin_menu = True
        while fin_menu:
            try:
                print('\t\t==Bienvenido Uusario:==')
                print('1. Ingresar Productos')
                print('2. Registrar Pedidos, \n3.Listar Pedidos Urgentes primero \n4. Salir')
                opcion = int(input('Ingrese la opción que desea ingresar: '))
                match opcion:
                    case 1:
                        while True:
                            print('Presione N/n cuando finalice el ingreso de productos ')
                            codigo = len(list(self.diccionario_productos)) + 5
                            print(f'Código añadido de forma automatica: {codigo}')
                            nombre = input('Ingrese el nombre del producto: ')
                            if nombre.upper() == "N":
                                print('Saliendo')
                                break
                            else:
                                while True:
                                    precio = int(input('Precio: '))
                                    if precio > 0:
                                        print('Producto añadido con exito')
                                        producto_tmp = Producto(codigo, nombre, precio)
                                        self.diccionario_productos[codigo] = producto_tmp
                                        return
                                    else:
                                        print('El precio debe ser mayor a 0 ')

                    case 2:
                        while True:
                            print('Presione N/n para finalizar el pedido: ')
                            id_pedido = len(self.diccionario_pedidos)
                            nit = input('NIT: ')
                            if nit in self.diccionario_clientes:
                                print('Cliente existe')
                                break
                            else:
                                print('Ingreso de un nuevo cliente complete datos')
                                nombre = input('Nombre Cliente: ')
                                cliente_tmp = Cliente(nit, nombre)
                                self.diccionario_clientes[nit] = cliente_tmp  # Se agrega con exito el ciente
                                pedido_tmp = Pedidos(self.diccionario_clientes[nit])  # Se crea el pedido y luego ya se le colocan las atribuciones
                                break

                        while True:
                            print('Presione 0 para finalizar el pedido: ')
                            codigo = int(input('Ingrese el codigo del producto: '))
                            if self.existencia_codigo(codigo):
                                print(f'Cuantas unidades desea llevarse de {self.diccionario_productos[codigo]}: ')
                                cantidad_producto = int(input())
                                pedido_tmp.agregar_a_pedido(self.diccionario_productos[codigo], cantidad_producto)

                            if codigo ==0:
                                print('Cancelando el pedido')
                                return
                            else:
                                print('Este codigo no existe por favor ingrese uno correcto')



                    case 3:
                        if not self.diccionario_pedidos:
                            print('Aún mno hay pedidos realizados')
                        else:
                            print('Pedidos Urgentes: ')

                    case 4:
                        pass
                    case _:
                        print('Opción incorrecta por favor verificar')


            except Exception as e:
                print('Error por favor vuelva a intentarlo ')


dia_laboral = Gestion()
dia_laboral.vender()