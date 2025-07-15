productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

#stock = {modelo: [precio, stock]}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def valida_numero_entero_positivo(mnsj_input):
    while True:
        try:
            numero = int(input(mnsj_input))
            if numero <= 0:
                print("No se pueden ingresar números negativos o el cero (0)")
                continue
            else:
                return numero
        except ValueError:
            print("Solo ingresar números enteros positivos")

def valida_texto(mnsj_input):
    while True:
        texto = input(mnsj_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto
        
def buscar_marca(marca:str):
    for i in productos:
        if marca.lower() == productos[i][0].lower():
            print(productos[i])
            





def menu():
    while True:
        print("*** MENÚ PRINCIPAL ***")
        print("1.- Stock marca.")
        print("2.- Busqueda por precio.")
        print("3.- Actualizar precio.")
        print("4.- Salir")

        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("Solo ingresar números (1-4)")

        if opc == 1:
            print("1")

        elif opc == 2:
            print("2")

        elif opc == 3:
            print("3")

        elif opc == 4:
            print("Saliendo!!")
            break

        else:
            print("Opcion no disponible (solo 1-4)")

            
menu()       
            