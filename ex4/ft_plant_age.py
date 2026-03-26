def ft_plant_age():
    # Pedimos la edad de la planta en días y la convertimos a entero
    age = int(input("Enter plant age in days: "))
    
    # Comprobamos si la planta tiene más de 60 días
    if age > 60:
        # Si es mayor, está lista para cosechar
        print("Plant is ready to harvest!")
    else:
        # Si no, aún necesita crecer
        print("Plant needs more time to grow.")