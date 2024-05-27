class ValidadorIp:
    def validar_direccion_ipv4(self, direccion_ip):
        valores_octetos = direccion_ip.split(".")
        if len(valores_octetos) != 4:
            return False
        try:
            octetos = [Octeto(octeto) for octeto in valores_octetos]
        except ValueError:
            return False
        if octetos[3] == Octeto("0") or octetos[3] == Octeto("255"):
            return False
        return True


class Octeto:
    def __init__(self, valor):
        if int(valor) < 0 or int(valor) > 255:
            raise ValueError()
        if int(valor) > 0 and valor.startswith("0"):
            raise ValueError()
        self.__valor = valor

    def __eq__(self, other):
        return self.__valor == other.__valor
