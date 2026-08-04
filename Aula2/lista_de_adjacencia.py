def criar_lista_adjacencia(V,E):
    grafo= {v: set() for v in V }

    for u, v in E:
        grafo[u].add(v)
        grafo[v].add(u)

    return grafo
V= {1,2,3,4}
E= {    
    (1,3),
    (1,4),
    (3,4)
}
grafo = criar_lista_adjacencia(V, E)

print (grafo)

def grau(grafo, v):
    return len (grafo [v])

print("Grau do vertice 1:", grau(grafo, 1))
print("Grau do vertice 2:", grau(grafo, 2))
print("Grau do vertice 3:", grau(grafo, 3))
print("Grau do vertice 4:", grau(grafo, 4))