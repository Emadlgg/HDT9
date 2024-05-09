import networkx as nx
import os

def cargar_rutas(nombre_archivo):
    grafo = nx.Graph()
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('"Pueblo Paleta", "Aldea Azalea", 100\n')
            archivo.write('"Aldea Azalea", "Ciudad Safiro", 150\n')
            archivo.write('"Pueblo Paleta", "Ciudad Safiro", 800\n')
            archivo.write('"Ciudad Lavanda", "Aldea Fuego", 300\n')
        print(f"Archivo {nombre_archivo} creado con rutas predefinidas.")
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            estacion_origen, estacion_destino, costo = linea.strip().split(',')
            costo = int(costo)
            grafo.add_edge(estacion_origen.strip(), estacion_destino.strip(), weight=costo)
    return grafo

def destinos_posibles(grafo, estacion_salida):
    return [vecino for vecino in grafo.neighbors(estacion_salida)]

def mejores_rutas(grafo, estacion_salida):
    return nx.single_source_dijkstra_path(grafo, estacion_salida)

def main():
    archivo_rutas = "rutas.txt"
    grafo = cargar_rutas(archivo_rutas)

    print("Estaciones disponibles:")
    for estacion in grafo.nodes():
        print(estacion)

    estacion_salida = input("Ingrese el nombre de la estación de salida: ").strip()

    if estacion_salida not in grafo.nodes():
        print("La estación de salida no es válida.")
        return

    print(f"Destinos posibles desde {estacion_salida}:")
    destinos = destinos_posibles(grafo, estacion_salida)
    for destino in destinos:
        print(destino)

    print("Mejores rutas:")
    mejores = mejores_rutas(grafo, estacion_salida)
    for destino, ruta in mejores.items():
        _, costo = nx.single_source_dijkstra(grafo, estacion_salida)
        costo = costo[destino]
        print(f"{estacion_salida} -> {destino}: {ruta} - Costo: {costo}")

if __name__ == "__main__":
    main()
