from src.validador_ip import ValidadorIp


def test_retornar_true_si_es_una_direccion_ip():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("1.1.1.1")
    assert validador_ip.validar_direccion_ipv4("192.168.1.1")
    assert validador_ip.validar_direccion_ipv4("10.0.0.1")
    assert validador_ip.validar_direccion_ipv4("127.0.0.1")


def test_retornar_false_si_la_direccion_no_tiene_4_octetos():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("1") is False
    assert validador_ip.validar_direccion_ipv4("1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.1.1.1") is False


def test_retornar_false_si_la_direccion_ip_esta_vacia():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("") is False
    assert validador_ip.validar_direccion_ipv4(" ") is False


def test_retornar_false_si_los_octetos_son_invalidos():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("256.1.1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.256.1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.256.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.1.256") is False
    assert validador_ip.validar_direccion_ipv4("-1.1.1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.-1.1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.-1.1") is False
    assert validador_ip.validar_direccion_ipv4("1.1.1.-1") is False


def test_retornar_false_si_el_cuarto_octeto_es_0_o_255():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("1.1.1.0") is False
    assert validador_ip.validar_direccion_ipv4("1.1.1.255") is False


def test_retornar_false_si_el_tercer_octeto_empieza_con_():
    validador_ip = ValidadorIp()

    assert validador_ip.validar_direccion_ipv4("1.1.1.01") is False
    assert validador_ip.validar_direccion_ipv4("1.1.01.1") is False
    assert validador_ip.validar_direccion_ipv4("1.01.1.1") is False
    assert validador_ip.validar_direccion_ipv4("01.1.1.1") is False
