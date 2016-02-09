
precios = {
    'Gravity\'s Rainbow' : 1200,
    'Los sorias' : 4500,
    'Ulysses' : 960,
    'El Jardín de las Máquinas Parlantes' : 780,
    'Rayuela' : 750,
    'Criptonomicon' : 1299    
}

# Caja de libros favoritos
caja = zip(precios.values(), precios.keys())
for c in caja: print(c)

# ------------------------------------------

# Buscando el menor precio con min
menor_fail = min(precios)
print("Menor precio fail -->",menor_fail)

# Buscando el menro precio con zip
menor_precio = min(zip(precios.values(), precios.keys()))
print("Menor precio -->",menor_precio)


