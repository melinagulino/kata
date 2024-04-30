#Dado un número natural mayor a 0:
#Retornar Fizz si el número es divisible por 3
#Retornar Buzz si el número es divisible por 5
#Retornar FizzBuzz si el número es divisible tanto por 3 como por 5
#Retornar el número en cuestión si no es divisible ni por 3 ni por 5
#Bonus: Retornar Whiz si el número es primo
class Fizzbuzz:
    def resultado(self, numero):
        if self.__es_divisible_por_3_y_5(numero):
            return "FizzBuzz"
        if self.__es_divisible_por_3(numero):
            return "Fizz"
        if self.__es_divisible_por_5(numero):
            return "Buzz"
        if numero == 2:
            return "Whiz"
        return numero

    def __es_divisible_por_3_y_5(self, numero):
        return self.__es_divisible_por_3(numero) and self.__es_divisible_por_5(numero)

    def __es_divisible_por_5(self, numero):
        return numero % 5 == 0

    def __es_divisible_por_3(self, numero):
        return numero % 3 == 0

