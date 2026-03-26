def ft_count_harvest_iterative():
    # Pedimos el número de días hasta la cosecha
    days = int(input("Days until harvest: "))
    
    # Recorremos desde el día 1 hasta el número indicado
    for i in range(1, days + 1):
        print("Day", i)
    
    # Mensaje final cuando termina el conteo
    print("Harvest time!")