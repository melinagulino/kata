class ValidadorIp:
    def validar_direccion_ipv4(self, direccion_ip):
        try:
            ip = DireccionIpv4.desde_string(direccion_ip)
        except ValueError:
            return False
        return ip.asignable_a_host()


class DireccionIpv4:
    @classmethod
    def desde_string(cls, valor):
        return cls(cls.__instanciar_octetos(valor))

    @classmethod
    def __instanciar_octetos(cls, valor):
        octetos = valor.split(".")
        cls.__asegurar_que_son_cuatro_octetos(octetos)
        return [Octeto.desde_string(octeto) for octeto in octetos]

    @classmethod
    def __asegurar_que_son_cuatro_octetos(cls, octetos):
        if len(octetos) != 4:
            raise ValueError()

    def __init__(self, octetos):
        self.__octetos = octetos

    def asignable_a_host(self):
        # dentro de los límites de la kata
        return self.__octetos[3] != Octeto("0") and self.__octetos[3] != Octeto("255")


class Octeto:
    @classmethod
    def desde_string(cls, valor):
        cls.__asegurar_que_el_valor_esta_dentro_del_rango_valido(valor)
        cls.__asegurar_que_el_valor_no_empieza_con_cero(valor)
        return cls(valor)

    @classmethod
    def __asegurar_que_el_valor_no_empieza_con_cero(cls, valor):
        if int(valor) > 0 and valor.startswith("0"):
            raise ValueError()

    @classmethod
    def __asegurar_que_el_valor_esta_dentro_del_rango_valido(cls, valor):
        if int(valor) < 0 or int(valor) > 255:
            raise ValueError()

    def __init__(self, valor):
        self.__valor = valor

    def __eq__(self, other):
        return self.__valor == other.__valor
