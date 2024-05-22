
class ValidadorIp:
    def validar_direccion_ipv4(self, direccion_ip):
        octetos = direccion_ip.split(".")
        if len(octetos) != 4:
            return False
        for octeto in octetos:
            if int(octeto) < 0 or int(octeto) > 255:
                return False
            if int(octeto) > 0 and octeto.startswith("0"):
                return False
        if int(octetos[3]) == 0 or int(octetos[3]) == 255:
            return False
        return True
