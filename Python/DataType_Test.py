# Un ejemplo para validar tipos de datos.
# La funcion recibe una clave del diccionario de tipos de datos
# y retorna la funcion asoiada (key) a dicha clave
# Cada funcion valida el tipo de dato

def data_type(data):

    def integer(n):
        if type(n) == int: return True
        else: return False

    def float(n):
        if type(n) == float: return True
        else: return False

    def string(n):
        if type(n) == str: return true
        else: return False

    def tupla(*args):
        if type(args) == tuple: return True
        else: return False

    def lista(*args):
        if type(args) == list: return True
        else: return False
            

    def dictionary(*args):
        if type(args) == dict: return True
        else: return False

    datas = {
            'integer' : integer,
             'float' : float,
             'string' : string,
             'tupla' : tupla,
             'lista': lista,
             'dictionary' : dictionary
             }
    return datas[data]


isTupla = data_type('tupla')
print(isTupla((1,2,3,4,5,6)))

c = data_type('float')
print(c(6))
























