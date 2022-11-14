"""
Universidad Nacional Autónoma de México
Facultad de Ingeniería
Inteligencia Artificial
Grupo 02

Profesor: Dr. José Abel Herrera Camacho
Autor(es): Zuriel Zárate García, Aldo Abad Vásquez y Ana Laura Mendoza Millán
Fecha: 14 de noviembre de 2022

Descripción: Programa que implementa el algorítmo A* para encontrar 
             la ruta óptima desde cualquier ciudad a Bucharest, con
             base en el mapa de Rumania.
"""

import networkx as nx
import matplotlib
import os

"""
Desc: Implementa el algorítmo A*
Param: 
    rb      -> Diccionario de distancias rectas desde todas la ciudades a Bucharest
    ciudad  -> Grafo ponderado de la ciudad con estructura de diccionario
    inicio  -> Ciudad desde donde se inicia la búsqueda

Ret: Retorna una lista con la ruta final y el costo total
"""
def aEstrella(rb,ciudad,inicio):
    print("\n")
    visitadas = []
    tierra = [] #Las ciudades que se van a tierra :u
    costo = 0
    actual = inicio

    gElegida = 0 #La g(n) acumulada inicial es 0
    while actual != "Bucharest":
        print("========== ",actual," ==========")
        aux = 0
        min = 0
        elegida = ""
        for c in ciudad[actual]:
            if (c in visitadas) == False: #Si ya está visitada la ciudad
                print(c)
                g = gElegida + int(ciudad[actual][c]["weight"]) 
                h = int(rb[c])
                f = g+h
                print("f(n) = ",g," + ",h," = ",f)
                
                #Revisamos si es el menor
                if aux==0:
                    min = f #El primer f es el mínimo automáticamente
                    elegida = c
                    gAcum = g
                if f<min:
                    min = f
                    elegida = c
                    gAcum = g
                aux+=1
        visitadas.append(actual)
        gElegida = gAcum #La g(n) acumulada para el menor valor
        print("\nMínimo: ",min)
        print("Ciudad elegida: ",elegida)
        print("Visitadas: ",visitadas)
        print("g(n) acumulada: ",gElegida,"\n")
        actual = elegida
    visitadas.append(actual)
    return visitadas,gAcum

def main():
    os.system("cls")
    #Definimos distancias rectas a Bucharest en un diccionario
    rb = {
    "Arad":366, 
    "Bucharest":0, 
    "Craiova":160, 
    "Dobreta":242, 
    "Eforie":161, 
    "Fagaras":178, 
    "Giurgiu":77, 
    "Hirsova":151, 
    "Iasi":226,
    "Lugoj":244,
    "Mehadia":241,
    "Neamt":234,
    "Oradea":380,
    "Pitesti":98,
    "Rimnicu Vilcea":193,
    "Sibiu":253,
    "Timisoara":329,
    "Urziceni":80,
    "Vaslui":199,
    "Zerind":374
    }

    #Definimos grafo. Utilizamos NetworkX para ello. Vea la documentación pertinente.
    ciudad = nx.Graph()
    ciudad.add_edge("Arad", "Sibiu", weight=140)
    ciudad.add_edge("Arad","Timisoara",weight=118)
    ciudad.add_edge("Arad","Zerind",weight=75)
    ciudad.add_edge("Bucharest", "Giurgiu", weight=90)
    ciudad.add_edge("Bucharest","Pitesti",weight=101)
    ciudad.add_edge("Bucharest","Fagaras",weight=211)
    ciudad.add_edge("Bucharest","Urziceni",weight=85)
    ciudad.add_edge("Craiova", "Dobreta", weight=120)
    ciudad.add_edge("Craiova","Rimnicu Vilcea",weight=146)
    ciudad.add_edge("Craiova","Pitesti",weight=138)
    ciudad.add_edge("Dobreta", "Mehadia", weight=75)
    ciudad.add_edge("Eforie", "Hirsova", weight=86)
    ciudad.add_edge("Fagaras", "Sibiu", weight=99)
    ciudad.add_edge("Hirsova", "Urziceni", weight=98)
    ciudad.add_edge("Iasi", "Neamt", weight=87)
    ciudad.add_edge("Iasi", "Vaslui", weight=92)
    ciudad.add_edge("Lugoj", "Timisoara", weight=111)
    ciudad.add_edge("Lugoj", "Mehadia", weight=70)
    ciudad.add_edge("Oradea","Sibiu",weight=151)
    ciudad.add_edge("Oradea", "Zerind", weight=71)
    ciudad.add_edge("Pitesti", "Rimnicu Vilcea", weight=97)
    ciudad.add_edge("Rimnicu Vilcea", "Sibiu", weight=80)
    ciudad.add_edge("Urziceni", "Vaslui", weight=142)

    arte = """                                                                                                                                          

                   AAA                                         tttt                                                  lllllll lllllll                   
                  A:::A                                     ttt:::t                                                  l:::::l l:::::l                   
                 A:::::A                                    t:::::t                                                  l:::::l l:::::l                   
                A:::::::A                                   t:::::t                                                  l:::::l l:::::l                   
               A:::::::::A               ssssssssss   ttttttt:::::ttttttt    rrrrr   rrrrrrrrr       eeeeeeeeeeee     l::::l  l::::l   aaaaaaaaaaaaa   
              A:::::A:::::A            ss::::::::::s  t:::::::::::::::::t    r::::rrr:::::::::r    ee::::::::::::ee   l::::l  l::::l   a::::::::::::a  
             A:::::A A:::::A         ss:::::::::::::s t:::::::::::::::::t    r:::::::::::::::::r  e::::::eeeee:::::ee l::::l  l::::l   aaaaaaaaa:::::a 
            A:::::A   A:::::A        s::::::ssss:::::stttttt:::::::tttttt    rr::::::rrrrr::::::re::::::e     e:::::e l::::l  l::::l            a::::a 
           A:::::A     A:::::A        s:::::s  ssssss       t:::::t           r:::::r     r:::::re:::::::eeeee::::::e l::::l  l::::l     aaaaaaa:::::a 
          A:::::AAAAAAAAA:::::A         s::::::s            t:::::t           r:::::r     rrrrrrre:::::::::::::::::e  l::::l  l::::l   aa::::::::::::a 
         A:::::::::::::::::::::A           s::::::s         t:::::t           r:::::r            e::::::eeeeeeeeeee   l::::l  l::::l  a::::aaaa::::::a 
        A:::::AAAAAAAAAAAAA:::::A    ssssss   s:::::s       t:::::t    tttttt r:::::r            e:::::::e            l::::l  l::::l a::::a    a:::::a 
       A:::::A             A:::::A   s:::::ssss::::::s      t::::::tttt:::::t r:::::r            e::::::::e          l::::::ll::::::la::::a    a:::::a 
      A:::::A               A:::::A  s::::::::::::::s       tt::::::::::::::t r:::::r             e::::::::eeeeeeee  l::::::ll::::::la:::::aaaa::::::a 
     A:::::A                 A:::::A  s:::::::::::ss          tt:::::::::::tt r:::::r              ee:::::::::::::e  l::::::ll::::::l a::::::::::aa:::a
    AAAAAAA                   AAAAAAA  sssssssssss              ttttttttttt   rrrrrrr                eeeeeeeeeeeeee  llllllllllllllll  aaaaaaaaaa  aaaa                                                                                                                                               
    
    """
    print(arte)
    print("\n")

    flag = 0

    while(flag==0):
        inicio = input("     Ingresa el nombre de la ciudad de inicio: ")
        if inicio in rb:
            print("     Si existe la ciudad")
            ruta,costo = aEstrella(rb,ciudad,inicio)
            flag = 1
        else:
            os.system("cls")
            print("     No existe la ciudad que ingresaste. Intente de nuevo.")

    print("Ruta Final: ",ruta)
    print("Costo total: ",costo," [km]")

main()
