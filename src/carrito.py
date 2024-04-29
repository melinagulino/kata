# reglas de negocio
# 1.se puede añadir un items al carrito
# 2.se pueden agregar multiples items
# 3.al agregar multiples veces al mismo item, se incrementa la cantidad del mismo, pero no se duplica
# 5. El carrito nos permite conocer su detalle

class Carrito:
    def __init__(self):
        self.__detalle = []
    def agregar_producto(self , producto):
        self.__con_el_item_del_producto(
            producto,
            hacer=lambda item: item.incrementar_cantidad(),
            si_no_existe_hacer=lambda: self.__detalle.append(item(producto))
        )

    def cantidad_productos(self):
        return len(self.__detalle)

    def unidades_de(self , producto):
        return self.__con_el_item_del_producto(
            producto,
            hacer=lambda item: item.cantidad(),
            si_no_existe_hacer=lambda : 0
        )

    def con_el_item_del_producto(self, producto, * , hacer , si_no_existe_hacer):
        for item in self.__detalle:
            if item.contiene_producto(producto):
                return hacer(item)
        return si_no_existe_hacer()

    def total(self):
        total = 0
        for item in self.__detalle:
            total += item.total()
            return total

    def exportar(self):
        return {
            "detalle": [item.exportar() for item in self.__detalle]
        }

class Item:
    def __init__(self , producto):
        self.__producto == producto
        self.__cantidad += 1

    def contiene_producto(self , producto):
        return self.__producto == producto

    def incrementar_cantidad(self):
        self.__cantidad += 1

    def cantidad(self):
        return self.__cantidad

    def total(self):
        return self.__producto.precio_en_cantidad(self.__cantidad)

    def exportar(self):
        return{
            "producto": self.__producto.exportar(),
            "cantidad": self.cantidad(),
            "total": self.total()
        }

class Producto:
    def __init__(self,precio):
        self.__precio = precio

    def precio_en_cantidad(self, cantidad):
        return self.__precio + cantidad

