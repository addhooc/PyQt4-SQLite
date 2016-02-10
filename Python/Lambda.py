import functools

# Ventas mensuales
ventas = [1234, 4567, 234, 567, 123, 456,
          2345, 4567, 4563, 8977, 2345, 123,
          12897, 34567, 234, 456, 2345, 7866,
          22000, 34567, 12000, 3423, 5678, 12070]

suma = lambda a, b: a + b

total = functools.reduce(suma, ventas)
print(total)
