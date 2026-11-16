"diccionario de peliculas"
peliculas = {
    "Inception": {"director": "Christopher Nolan", "año": 2010, "genero": "Ciencia ficción", "duracion": 148},
    "The Matrix": {"director": "Lana Wachowski, Lilly Wachowski", "año": 1999, "genero": "Ciencia ficción", "duracion": 136},
    "Interstellar": {"director": "Christopher Nolan", "año": 2014, "genero": "Ciencia ficción", "duracion": 169},
    "Back to the Future": {"director": "Robert Zemeckis", "año": 1985, "genero": "Ciencia ficción", "duracion": 108},
    "The Godfather": {"director": "Francis Ford Coppola", "año": 1972, "genero": "Crimen", "duracion": 175},
    "Batman Begins": {"director": "Christopher Nolan", "año": 2005, "genero": "Acción", "duracion": 140},
    "The Dark Knight": {"director": "Christopher Nolan", "año": 2008, "genero": "Acción", "duracion": 152},
    "The Dark Knight Rises": {"director": "Christopher Nolan", "año": 2012, "genero": "Acción", "duracion": 164},
    "Friday the 13th": {"director": "Sean S. Cunningham", "año": 1980, "genero": "Terror", "duracion": 93},
    "Shrek": {"director": "Andrew Adamson, Vicky Jenson", "año": 2001, "genero": "Animación", "duracion": 88},
    "The Lion King": {"director": "Roger Allers, Rob Minkoff", "año": 1994, "genero": "Animación", "duracion": 88},
    "Fast and Furious": {"director": "Rob Cohen", "año": 2001, "genero": "Acción", "duracion": 106},
    "The Avengers": {"director": "Joss Whedon", "año": 2012, "genero": "Acción", "duracion": 143},
    "The Lord of the Rings: The Fellowship of the Ring": {"director": "Peter Jackson", "año": 2001, "genero": "Fantasía", "duracion": 178},
}
def filtrar_peliculas_por_genero(peliculas, genero):
    """Devuelve una lista de películas que pertenecen al género especificado."""
    genero = genero.lower()
    return [titulo for titulo, info in peliculas.items() if info["genero"].lower() == genero]
def filtrar_por_año(peliculas, año):
    """Devuelve una lista de películas que fueron lanzadas en el año especificado."""
    return [titulo for titulo, info in peliculas.items() if info["año"] == año]
def ordenar_por_duracion(peliculas, descendente=False):
    """Devuelve una nueva lista ordenada por duración."""
    return sorted(peliculas, key=lambda p: p["duracion"], reverse=descendente)
def duracion_promedio(peliculas):
    """Calcula la duración promedio en minutos (0 si no hay películas)."""
    if not peliculas:
        return 0
    return sum(p["duracion"] for p in peliculas) / len(peliculas)

def mostrar_peliculas(peliculas):
    """Imprime la lista de películas con sus detalles."""
    for titulo, info in peliculas.items():
        print(f"{titulo} ({info['año']}) - {info['genero']} - {info['duracion']} min - Dirigida por {info['director']}")
def main():
    print("Películas disponibles:")
    mostrar_peliculas(peliculas)
    
    genero = input("\nIngrese un género para filtrar: ")
    peliculas_filtradas = filtrar_peliculas_por_genero(peliculas, genero)
    print(f"\nPelículas del género '{genero}':")
    for titulo in peliculas_filtradas:
        print(titulo)
    
    año = int(input("\nIngrese un año para filtrar: "))
    peliculas_por_año = filtrar_por_año(peliculas, año)
    print(f"\nPelículas del año {año}:")
    for titulo in peliculas_por_año:
        print(titulo)
    
    duracion_media = duracion_promedio(peliculas.values())
    print(f"\nDuración promedio de las películas: {duracion_media:.2f} minutos")
if __name__ == "__main__":
    main()