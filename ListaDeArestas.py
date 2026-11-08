def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas
   
pass


def inserir_vertice(vertices, vertice):
  
    if vertice not in vertices:
        vertices.append(vertice)


pass

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, arestas, origem)
    if destino not in vertices:
        inserir_vertice(vertices, arestas, destino)
    arestas.append([origem, destino])


    if nao_direcionado:
        arestas.append([destino, origem])
pass

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem,destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino,origem])
pass

def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
            vertices.remove(vertice)
    for aresta in arestas.copy():
        if vertice in aresta:
         arestas.remove(aresta)

pass

def existe_aresta(arestas, origem, destino):
    for aresta in arestas:
        if aresta == [origem,destino]:
            return True
    return False

pass


def vizinhos(vertices, arestas, vertice):    
    if vertice not in vertices:
        return []
    
    vizinhos = []
    for origem, destino in arestas: 
        if origem == vertice:
            listar_vizinhos.append(destino)
    return listar_vizinhos
pass


def grau_vertices(vertices, arestas):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Percorrer todas as arestas [origem, destino]:
        I. Se o grafo for não direcionado:
            - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
        II. Se o grafo for direcionado
            - Se o vértice for origem Incrementar grau de saída do vértice origem
            - Se o vértice for destino incrementar grau de entrada do vértice destino.
            - Calcular o grau total (entrada + saída).
    4. Retornar o dicionário 'graus' para cada vértice.
    """
    pass


def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
        - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    pass


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    pass


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    pass


def main():
    pass


if __name__ == "__main__":
    main()
