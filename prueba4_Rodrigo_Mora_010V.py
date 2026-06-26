peliculas = []


def validar_titulo(titulo):
    return bool(titulo.strip())


def validar_duracion(duracion):
    try:
        valor = int(duracion)
    except ValueError:
        return None
    return valor if valor > 0 else None


def validar_calificacion(calificacion):
    try:
        valor = float(calificacion)
    except ValueError:
        return None
    return valor if 0.0 <= valor <= 10.0 else None


def agregar_pelicula(lista):
    titulo = input("Ingrese el titulo de la pelicula: ")
    duracion = input("Ingrese la duracion de la pelicula (en minutos): ")
    calificacion = input("Ingrese la calificacion de la pelicula (0.0 a 10.0): ")

    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio ni ser solo espacios en blanco.")
        return

    duracion_valida = validar_duracion(duracion)
    if duracion_valida is None:
        print("Error: La duracion debe ser un numero entero mayor que cero.")
        return

    calificacion_valida = validar_calificacion(calificacion)
    if calificacion_valida is None:
        print("Error: La calificacion debe ser un numero decimal entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": duracion_valida,
        "calificacion": calificacion_valida,
    }
    lista.append(pelicula)
    print(f"Pelicula '{titulo}' agregada exitosamente.")


def buscar_pelicula(lista, titulo):
    for i, pelicula in enumerate(lista):
        if pelicula["titulo"] == titulo:
            return i
    return -1


def eliminar_pelicula(lista, titulo):
    posicion = buscar_pelicula(lista, titulo)
    if posicion != -1:
        del lista[posicion]
        print(f"Pelicula '{titulo}' eliminada exitosamente.")
    else:
        print(f"La película '{titulo}' no se encuentra registrada.")


def actualizar_disponibilidad(lista):
    for pelicula in lista:
        pelicula["disponible"] = "si" if pelicula["calificacion"] >= 7.0 else "no"


def mostrar_peliculas(lista):
    if not lista:
        print("No hay películas registradas.")
        return
    

    print("=== LISTA DE PELICULAS ===")
    for pelicula in lista:
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")
        if "disponible" in pelicula:
            estado = "DISPONIBLE" if pelicula["disponible"] == "si" else "NO DISPONIBLE"
            print(f"Estado: {estado}")
        print("********************************************")


while True:
    print("Menu:")
    print("1. Agregar pelicula")
    print("2. Buscar pelicula")
    print("3. Eliminar pelicula")
    print("4. Cambiar disponibilidad de pelicula")
    print("5. Mostrar peliculas")
    print("6. Salir del programa")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_pelicula(peliculas)
    elif opcion == "2":
        titulo_buscar = input("Ingrese el titulo de la pelicula a buscar: ")
        posicion = buscar_pelicula(peliculas, titulo_buscar)
        if posicion != -1:
            pelicula = peliculas[posicion]
            print("=== PELICULA ENCONTRADA ===")
            print(f"Título: {pelicula['titulo']}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Calificación: {pelicula['calificacion']}")
            if "disponible" in pelicula:
                estado = "DISPONIBLE" if pelicula['disponible'] == "si" else "NO DISPONIBLE"
                print(f"Estado: {estado}")
            print("*" * 44)
        else:
            print(f"La película '{titulo_buscar}' no se encuentra registrada.")
    elif opcion == "3":
        titulo_eliminar = input("Ingrese el titulo de la pelicula a eliminar: ")
        eliminar_pelicula(peliculas, titulo_eliminar)
    elif opcion == "4":
        actualizar_disponibilidad(peliculas)
        print("Disponibilidad de peliculas actualizada exitosamente.")
    elif opcion == "5":
        actualizar_disponibilidad(peliculas)
        mostrar_peliculas(peliculas)
    elif opcion == "6":
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    else:
        print("Opcion invalida. Por favor seleccione una opcion del 1 al 6.")