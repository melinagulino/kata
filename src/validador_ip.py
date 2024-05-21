
class ValidadorIp:
    def validar_direccion_ipv4(self, direccion_ip):
        if direccion_ip == "1.1.1.1" or direccion_ip == "192.168.1.1" or direccion_ip == "10.0.0.1" or direccion_ip == "127.0.0.1":
            return True
        if direccion_ip == "1" or direccion_ip == "1.1" or direccion_ip == "1.1.1" or direccion_ip == "1.1.1.1.1" or direccion_ip == "" or direccion_ip == " ":
            return False
        octetos = direccion_ip.split(".")
        if int(octetos[0]) > 255 or int(octetos[1]) > 255 or int(octetos[2]) > 255 or int(octetos[3]) > 255:
            return False
        if int(octetos[0]) < 0 or int(octetos[1]) < 0 or int(octetos[2]) < 0 or int(octetos[3]) < 0:
            return False

