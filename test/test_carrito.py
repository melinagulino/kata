from src.carrito import Carrito ,Producto

def test_el_carrito_esta_vacio():
    assert Carrito().cantidad_producto() == 0

def test_se_puede_añadir_un_producto_al_carrito():
    carrito = Carrito()
    carrito.agregar_producto(Producto())

    assert carrito.cantidad_de_productos() == 1

def test_se_pueden_agregar_multiples_productos_al_carrito():
    carrito = Carrito()
    carrito.agregar_producto(Producto())
    carrito.agregar_producto(Producto())

    assert carrito.cantidad_de_productos() == 2

def test_al_agregar_multiples_veces_el_mismo_producto_se_incrementa_el_numero_de_unidades_del_mismo():
    carrito = Carrito()
    producto1 = Producto()
    producto2 = Producto()
    producto3 = Producto()

    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto1)

    carrito.agregar_producto(producto2)


    assert carrito.unidades_de(producto3) == 0
    assert carrito.unidades_de(producto2) == 1
    assert carrito.unidades_de(producto1) == 2

def test_el_carrito_nos_permite_conocer_el_total_de_la_compra():
    carrito = Carrito()
    un_producto = Producto(2_500_000)
    otro_producto = Producto(600)

    assert carrito.total() == 0

    carrito.agregar_producto(un_producto)
    assert carrito.total()

def test_el_carrito_nos_permite_conocer_el_total_de_la_compra():
    carrito.agregar_producto(un_producto)
    representacion_esperada = {
        "detalle": [
            {
                "producto": {
                    "precio": 2_500_000
                },
                "cantidad": 1,
                "total": 2_500_000
            },
            {
                "producto": {
                    "precio": 600_000
                },
                "cantidad": 2,
                "total": 1_200_000
            }
        ]
    }

    assert carrito.exportar() == representacion_esperada

    carrito.agregar_producto(un_producto)

    representacion_esperada = {
            "detalle": [
                {
                    "producto": {
                        "precio": 2_500_000
                    },
                    "cantidad": 1,
                    "total": 2_500_000
                },
                {
                    "producto": {
                    "precio": 600_000
                },
                "cantidad": 2,
                "total": 1_200_000
            }
        ]
    }




