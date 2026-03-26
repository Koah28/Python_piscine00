def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    # Capitalizamos el nombre de la semilla
    seed = seed_type.capitalize()

    # Comprobamos el tipo de unidad
    if unit == "packets":
        print(seed + " seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed + " seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed + " seeds: covers", quantity, "square meters")
    else:
        # Caso no válido
        print("Unknown unit type")