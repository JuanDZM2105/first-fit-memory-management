def first_fit(memory, required, index):

    for i in range(len(memory)):
        #paso 1: obtener segmento objetivo

        base, limit = memory[(index+i) % len(memory)]

        #paso 2: verificar si el segmento objetivo es suficiente

        if base + required -1 <= limit:
            new_base = base + required
            new_index = ((index+i) % len(memory))+1

            #paso 3: actualizar la memoria

            memory[index] = (new_base, limit)
            return  memory, new_base, limit, new_index

        else:
            continue

    #paso 4: si no se encuentra un segmento suficiente en toda la memoria, se retorna none
    return  None


memory = [
    (0, 99),   # Página 0: Base = 0, Límite = 99 (Tamaño = 100)
    (100, 199),# Página 1: Base = 100, Límite = 199 (Tamaño = 100)
    (200, 299),# Página 2: Base = 200, Límite = 299 (Tamaño = 100)
    (300, 399),# Página 3: Base = 300, Límite = 399 (Tamaño = 100)
    (400, 499),# Página 4: Base = 400, Límite = 499 (Tamaño = 100)
    (500, 599),# Página 5: Base = 500, Límite = 599 (Tamaño = 100)
    (600, 699),# Página 6: Base = 600, Límite = 699 (Tamaño = 100)
    (700, 799),# Página 7: Base = 700, Límite = 799 (Tamaño = 100)
    (800, 899),# Página 8: Base = 800, Límite = 899 (Tamaño = 100)
    (900, 999) # Página 9: Base = 900, Límite = 999 (Tamaño = 100)
]

idx= 1
required = [50,1000,70,80,90,100,10]

for i in required:
    try:
        memory, new_base, new_limit, idx = first_fit(memory, i, idx)
        print(f"Espacio asignado para tamaño {i}: Nueva base = {new_base}, Nuevo límite = {new_limit}, nuevo indice = {idx}")

    except Exception as e:
        print(f"Error: no hay espacio, {e}")
