def ft_count_harvest_recursive():
    # Pedimos el número de días hasta la cosecha
    days = int(input("Days until harvest: "))

    # Función auxiliar recursiva que recorre los días
    def helper(day):
        # Caso base: si hemos superado el número de días
        if day > days:
            print("Harvest time!")
            return
        
        # Mostramos el día actual
        print("Day", day)
        
        # Llamada recursiva al siguiente día
        helper(day + 1)

    # Iniciamos la recursión desde el día 1
    helper(1)