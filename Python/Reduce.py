import functools

# Ventas mensuales
ventas = [1234, 4567, 234, 567, 123, 456,
          2345, 4567, 4563, 8977, 2345, 123,
          12897, 34567, 234, 456, 2345, 7866,
          22000, 34567, 12000, 3423, 5678, 12070]

# Funcion a utilizar como parametro para Reduce
def sum(a, b):
    return a + b

# Apicacion:
# Reducimos a un total mediante 'reduce' y la funcion sum
# total = functools.reduce(sum, ventas)
# print('Ventas:',total)

def total(*args):
    return functools.reduce(sum, ventas)

print(total(ventas))


# Clase Ventas_mensuales

class Ventas_mensuales():
    def sum(a, b):
        return a + b
    def total(*args):
        # Recibe una lista
        # Retorna un valor resultado de la reduccion sujeta a sum
        return functools.reduce(sum, ventas)

v = Ventas()
print(v.total(ventas))
