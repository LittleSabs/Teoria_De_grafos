import heapq

def dijkstra(grafo, origem):


    distancias = {vertice: float('inf') for vertice in grafo}
    
    distancias[origem] = 0
    
    anteriores = {vertice: None for vertice in grafo}
    
    fila = [(0, origem)]
    
    while fila:
        
        #heapq é filas de prioridade, logo true
        distancia_atual, vertice_atual = heapq.heappop(fila)
        
        if distancia_atual > distancias[vertice_atual].items():
            continue
        
        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso
            
        
        if nova_distancia< distancias[vizinho]:
            distancias[vizinho] = nova_distancia
            anteriores[vizinho] = vertice_atual
            
            heapq.heappush(fila, (nova_distancia, vizinho))
        
    return distancias, anteriores
    
    
def caminho_minimo(anteriores, origem, destino):
    
    caminho = []
    atual = destino
    
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    
    caminho.reverse()
    
    if caminho[0] != origem:
        return None
    
    return caminho

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2},
}

origem = 'A'

distancias, anteriores = dijkstra(grafo, origem)

print(f"Menores caminhos partindo de {origem}:\n")

for destino in grafo:
    caminho = caminho_minimo(anteriores, origem, destino)
    
    print(
        f"{origem} -> {destino}:"
        f"distancia = {distancias[destino]}, "
        f"caminho = {caminho}"
    )