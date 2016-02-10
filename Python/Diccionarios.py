
precios = {
    "Gravity's Rainbow" : 1200,
    "Los sorias" : 4500,
    "Ulysses" : 960,
    "El Jardín de las Máquinas Parlantes" : 780,
    "Rayuela" : 750,
    "Criptonomicon" : 1299    
}

# Caja de libros favoritos
caja = zip(precios.values(), precios.keys())
for c in caja: print(c)

# -------------------------------------------------------

# Buscando el menor precio con min
menor_fail = min(precios)
print('''Menor precio fail:
      Considera menor a Criptonomicon
      porque la letra C se encuentra en primer lugar
      de la ordenación alfabética respecto
      del resto de letras iniciales --->''',menor_fail)
#--------------------------------------------------------


# Buscando el menor precio con zip
menor_precio = min(zip(precios.values(), precios.keys()))
print("Menor precio -->",menor_precio)

# Buscando el mayor precio con zip
mayor_precio = max(zip(precios.values(), precios.keys()))
print("Mayor precio -->",mayor_precio)


