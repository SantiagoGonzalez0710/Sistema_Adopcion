# Lista de mascotas disponibles
mascotas = [
    {"nombre": "Luna", "especie": "perro", "edad": 3, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Max", "especie": "perro", "edad": 2, "energia": "alta", "compatible_niños": "no"},
    {"nombre": "Coco", "especie": "perro", "edad": 5, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Mimi", "especie": "gato", "edad": 1, "energia": "baja", "compatible_niños": "sí"},
    {"nombre": "Bunny", "especie": "conejo", "edad": 4, "energia": "baja", "compatible_niños": "no"},
    {"nombre": "Nina", "especie": "gato", "edad": 3, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Thor", "especie": "perro", "edad": 7, "energia": "baja", "compatible_niños": "sí"},
    {"nombre": "Oliver", "especie": "gato", "edad": 6, "energia": "alta", "compatible_niños": "no"},
    {"nombre": "Toby", "especie": "perro", "edad": 4, "energia": "alta", "compatible_niños": "sí"},
    {"nombre": "Bella", "especie": "conejo", "edad": 2, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Simba", "especie": "gato", "edad": 2, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Rex", "especie": "perro", "edad": 5, "energia": "alta", "compatible_niños": "no"},
    {"nombre": "Cleo", "especie": "gato", "edad": 4, "energia": "baja", "compatible_niños": "sí"},
    {"nombre": "Rocky", "especie": "perro", "edad": 6, "energia": "media", "compatible_niños": "no"},
    {"nombre": "Daisy", "especie": "conejo", "edad": 3, "energia": "alta", "compatible_niños": "sí"},
    {"nombre": "Milo", "especie": "gato", "edad": 5, "energia": "alta", "compatible_niños": "no"},
    {"nombre": "Lola", "especie": "perro", "edad": 1, "energia": "baja", "compatible_niños": "sí"},
    {"nombre": "Ginger", "especie": "conejo", "edad": 4, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Oscar", "especie": "gato", "edad": 7, "energia": "baja", "compatible_niños": "no"},
    {"nombre": "Zeus", "especie": "perro", "edad": 3, "energia": "alta", "compatible_niños": "sí"},
    {"nombre": "Chloe", "especie": "gato", "edad": 2, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Bobby", "especie": "perro", "edad": 4, "energia": "baja", "compatible_niños": "no"},
    {"nombre": "Ruby", "especie": "conejo", "edad": 1, "energia": "alta", "compatible_niños": "sí"},
    {"nombre": "Felix", "especie": "gato", "edad": 3, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Duke", "especie": "perro", "edad": 5, "energia": "media", "compatible_niños": "no"},
    {"nombre": "Sasha", "especie": "conejo", "edad": 2, "energia": "baja", "compatible_niños": "sí"},
    {"nombre": "Simone", "especie": "gato", "edad": 4, "energia": "alta", "compatible_niños": "no"},
    {"nombre": "Buddy", "especie": "perro", "edad": 6, "energia": "alta", "compatible_niños": "sí"},
    {"nombre": "Lilly", "especie": "conejo", "edad": 3, "energia": "media", "compatible_niños": "no"},
    {"nombre": "Salem", "especie": "gato", "edad": 1, "energia": "media", "compatible_niños": "sí"},
    {"nombre": "Ace", "especie": "perro", "edad": 2, "energia": "alta", "compatible_niños": "sí"},
]

# Función para filtrar mascotas según preferencias del usuario

def filtrar_mascotas(lista, especie, edad_min, edad_max, energia, tiene_niños):
    mascotas_filtradas = []
    for mascota in lista: 
        
        # Verificamos cada condición
        
        especie_ok = mascota["especie"] == especie
        edad_ok = edad_min <= mascota["edad"] <= edad_max
        energia_ok = mascota["energia"] == energia
        niños_ok = (tiene_niños == "no") or (mascota["compatible_niños"] == "sí")

        # Si cumple todas las condiciones, la agregamos a la lista
        
        if especie_ok and edad_ok and energia_ok and niños_ok:
            mascotas_filtradas.append(mascota)
    return mascotas_filtradas

# Función para mostrar las mascotas y permitir la adopción

def mostrar_y_adoptar(mascotas):
    if not mascotas:
        print("No encontramos mascotas que coincidan exactamente con tus preferencias.")
        return

    for i, mascota in enumerate(mascotas, start=1):
        print(f"\nMascota {i}: {mascota['nombre']}, {mascota['especie']}, {mascota['edad']} años, energía {mascota['energia']}, compatible con niños: {mascota['compatible_niños']}")
        respuesta = input("¿Quieres adoptarla? (sí / no): ").lower()
        if respuesta == "sí":
            print(f"\n¡Felicidades! Has adoptado a {mascota['nombre']}")
            return
    print("\nHas terminado de revisar todas las opciones sin adoptar.")

# Programa principal

print("Bienvenido a Adopta tu mascota")

# Pedimos las preferencias al usuario

especie = input("¿Cuál especie te interesa? ").lower()
edad_min = int(input("Edad mínima: "))
edad_max = int(input("Edad máxima: "))
energia = input("¿Nivel de energía preferido? (alta, media, baja): ").lower()
tiene_niños = input("¿Tienes niños en casa? (sí - no): ").lower()

# Filtramos mascotas con función
mascotas_compatibles = filtrar_mascotas(mascotas, especie, edad_min, edad_max, energia, tiene_niños)

# Mostramos mascotas filtradas y preguntamos por adopción
mostrar_y_adoptar(mascotas_compatibles)
