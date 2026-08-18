def encontrar_caminhos(grafo, origem, destino):

    caminhos = []

    def dfs(atual, caminho):

        if atual == destino:
            caminhos.append(caminho.copy())
            return

        for vizinho in grafo[atual]:

            # não repetir vértices
            if vizinho not in caminho:
                caminho.append(vizinho)

                dfs(
                    vizinho,
                    caminho
                )

                # Backtracking
                caminho.pop()

    dfs(origem, [origem])

    return caminhos


def encontrar_trilhas(grafo, origem, destino):

    trilhas = []

    def dfs(atual, trilha, arestas_usadas):

        if atual == destino:
            trilhas.append(trilha.copy())
            return

        for vizinho in grafo[atual]:

            # A-B e B-A representam a mesma aresta
            aresta = tuple(sorted((atual, vizinho)))

            if aresta not in arestas_usadas:
                arestas_usadas.add(aresta)

                trilha.append(vizinho)

                dfs(
                    vizinho,
                    trilha,
                    arestas_usadas
                )

                # Backtracking
                trilha.pop()
                arestas_usadas.remove(aresta)

    dfs(
        origem,
        [origem],
        set()
    )

    return trilhas


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}


# Origem e destino

origem = 'A'
destino = 'D'


# Caminhos

caminhos = encontrar_caminhos(
    grafo,
    origem,
    destino
)

print("Caminhos:")
print("-" * 40)

for i, caminho in enumerate(caminhos, start=1):
    print(
        f"Caminho {i}: "
        + "->".join(caminho)
    )


# Trilhas

trilhas = encontrar_trilhas(
    grafo,
    origem,
    destino
)

print("\nTrilhas:")
print("-" * 40)

for i, trilha in enumerate(trilhas, start=1):
    print(
        f"Trilha {i}: "
        + "->".join(trilha)
    )