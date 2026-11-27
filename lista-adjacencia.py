def dijkstra(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        return [], float("inf")
    processados = []

    distancias = {vertice: float("inf") for vertice in grafo}
    anteriores = {vertice: None for vertice in grafo}
    distancias[inicio] = 0

    while len(processados) < len(grafo):
        vertice_atual = None
        menor_distancia = float("inf")

        for vertice in grafo:
            if vertice not in processados and distancias[vertice] < menor_distancia:
                menor_distancia = distancias[vertice]
                vertice_atual = vertice

        if vertice_atual is None or menor_distancia == float("inf"):
            break

        if vertice_atual == destino:
            break

        lista_vizinhos = vizinhos(grafo, vertice_atual)

        for item in lista_vizinhos:
            vizinho, peso = item if isinstance(item, tuple) else (item, 1)

            if vizinho not in processados:
                nova_distancia = distancias[vertice_atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = vertice_atual

        processados.append(vertice_atual)

    if distancias[destino] == float("inf"):
        return [], float("inf")

    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = anteriores[atual]

    return caminho, distancias[destino]


def bfs(grafo, vertice_inicial):
    if vertice_inicial not in grafo:
        return []
    fila = [vertice_inicial]
    visitados = []

    while len(fila) > 0:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)

        for item in grafo.get(vertice, []):
            vizinho = item[0] if isinstance(item, tuple) else item
            if vizinho not in fila and vizinho not in visitados:
                fila.append(vizinho)
    return visitados


def menor_caminho_bfs(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        return []

    fila = [(inicio, [inicio])]
    visitados = []

    while len(fila) > 0:
        vertice, caminho = fila.pop(0)

        if vertice == destino:
            return caminho

        if vertice not in visitados:
            visitados.append(vertice)

            for item in grafo.get(vertice, []):
                vizinho = item[0] if isinstance(item, tuple) else item
                if vizinho not in visitados:
                    novo_caminho = caminho + [vizinho]
                    fila.append((vizinho, novo_caminho))

    return []


def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, peso=1, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    grafo[origem].append((destino, peso))

    if nao_direcionado:
        grafo[destino].append((origem, peso))


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return []


def listar_vizinhos(grafo, vertice):
    vizinho = vizinhos(grafo, vertice)
    print(vizinho)


def exibir_grafo(grafo):
    lista = grafo.items()

    for vertice, lista_vizinhos in lista:
        print(f"{vertice} -> {lista_vizinhos}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        return f"A {origem} não existe no grafo"

    grafo[origem] = [
        item for item in grafo[origem]
        if (item[0] if isinstance(item, tuple) else item) != destino
    ]

    if nao_direcionado and destino in grafo:
        grafo[destino] = [
            item for item in grafo[destino]
            if (item[0] if isinstance(item, tuple) else item) != origem
        ]


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        return f"O vértice {vertice} não existe no grafo"

    for outro_vertice in grafo:
        grafo[outro_vertice] = [
            item for item in grafo[outro_vertice]
            if (item[0] if isinstance(item, tuple) else item) != vertice
        ]

    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    if origem in grafo:
        for item in grafo[origem]:
            vizinho = item[0] if isinstance(item, tuple) else item
            if vizinho == destino:
                return True
    return False


def grau_vertices(grafo):
    graus = {}

    for j in grafo:
        graus[j] = {'in': 0, 'out': len(grafo[j]), 'total': 0}

    for j in grafo:
        for v in grafo:
            for item in grafo[v]:
                vizinho = item[0] if isinstance(item, tuple) else item
                if vizinho == j:
                    graus[j]['in'] += 1

    for j in grafo:
        graus[j]['total'] = graus[j]['in'] + graus[j]['out']

    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        if not existe_aresta(grafo, origem, destino):
            return False

    return True


def main():
    grafo = criar_grafo()

    while True:
        print("\n" + "=" * 30)
        print("       MENU DO GRAFO")
        print("=" * 15)
        print("1 - Mostrar o grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos de um vértice")
        print("7 - Verificar se aresta existe")
        print("8 - Mostrar grau dos vértices")
        print("9 - Verificar percurso")
        print("10 - Busca em Largura (BFS)")
        print("11 - Menor caminho com BFS")
        print("12 - Algoritmo de Dijkstra")
        print("0 - Sair")
        print("=" * 15)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_grafo(grafo)

        elif opcao == '2':
            vertice = input("Digite o nome do vértice: ")
            inserir_vertice(grafo, vertice)
            print(f"Vértice '{vertice}' inserido.")

        elif opcao == '3':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            peso_str = input("Peso da aresta (Enter para padrão 1): ").strip()
            try:
                peso = float(peso_str) if '.' in peso_str else int(peso_str)
            except ValueError:
                peso = 1
            direcionado = input("A ligação é de sentido duplo (não-direcionada)? (s/n): ").strip().lower() == 's'
            inserir_aresta(grafo, origem, destino, peso, direcionado)
            print("Aresta inserida.")

        elif opcao == '4':
            vertice = input("Digite o nome do vértice a remover: ")
            remover_vertice(grafo, vertice)
            print(f"Vértice '{vertice}' e as suas ligações foram removidos.")

        elif opcao == '5':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            direcionado = input("A ligação era de sentido duplo (não-direcionada)? (s/n): ").strip().lower() == 's'
            remover_aresta(grafo, origem, destino, direcionado)
            print("Aresta removida.")

        elif opcao == '6':
            vertice = input("Digite o nome do vértice: ")
            listar_vizinhos(grafo, vertice)

        elif opcao == '7':
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            existe = existe_aresta(grafo, origem, destino)
            if existe:
                print(f"Sim, existe uma aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta direta de {origem} para {destino}.")

        elif opcao == '8':
            graus = grau_vertices(grafo)
            print("\nGraus dos vértices:")
            for v, g in graus.items():
                print(f"Vértice {v} -> Entrada: {g['in']} | Saída: {g['out']} | Total: {g['total']}")

        elif opcao == '9':
            entrada = input("Introduza o percurso separando os vértices por espaço (ex: A B C D): ")
            caminho = entrada.split()
            if percurso_valido(grafo, caminho):
                print("O percurso é VÁLIDO.")
            else:
                print("O percurso é INVÁLIDO.")

        elif opcao == '10':
            inicio = input("Digite o vértice inicial para iniciar o BFS: ")
            if inicio not in grafo:
                print(f"O vértice '{inicio}' não existe no grafo.")
            else:
                resultado = bfs(grafo, inicio)
                print(f"Ordem de visitação (BFS): {' -> '.join(resultado)}")

        elif opcao == '11':
            inicio = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")

            if inicio not in grafo or destino not in grafo:
                print("Um ou ambos os vértices não existem no grafo.")
            else:
                caminho = menor_caminho_bfs(grafo, inicio, destino)
                if caminho:
                    print(f"Menor caminho de {inicio} até {destino}: {' -> '.join(caminho)}")
                else:
                    print(f"Não existe caminho entre '{inicio}' e '{destino}'.")

        elif opcao == '12':
            inicio = input("Digite o vértice inicial: ")
            destino = input("Digite o vértice de destino: ")

            if inicio not in grafo or destino not in grafo:
                print("Vértice inicial ou de destino não existe no grafo.")
            else:
                caminho, distancia = dijkstra(grafo, inicio, destino)
                if distancia == float("inf"):
                    print(f"Não existe caminho entre {inicio} e {destino}.")
                else:
                    print(f"Caminho: {' -> '.join(caminho)}")
                    print(f"Distância total: {distancia}")

        elif opcao == '0':
            print("A encerrar o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()