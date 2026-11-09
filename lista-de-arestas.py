def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas

def inserir_vertice(vertices, vertice):
  
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)

    arestas.append([origem, destino])

    if nao_direcionado:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem,destino])

    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino,origem])

def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
            vertices.remove(vertice)
    for aresta in arestas.copy():
        if vertice in aresta:
         arestas.remove(aresta)

def existe_aresta(arestas, origem, destino):
    for aresta in arestas:
        if aresta == [origem,destino]:
            return True
    return False

def vizinhos(vertices, arestas, vertice):    
    if vertice not in vertices:
        return []
    
    lista_de_vizinhos = []
    for origem, destino in arestas: 
        if origem == vertice:
            lista_de_vizinhos.append(destino)
    return lista_de_vizinhos

def grau_vertices(vertices, arestas):

    graus = {}

    for v in vertices:
        graus[v] = {'entrada': 0, 'saida': 0, 'total': 0}

    for origem, destino in arestas:
        graus[origem]['saida'] += 1
        graus[destino]['entrada'] += 1
        graus[origem]['total'] += 1
        graus[destino]['total'] += 1

    return graus

def percurso_valido(arestas, caminho):
    if len(caminho) <= 1:
        return True
        
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        
        if not existe_aresta(arestas, origem, destino):
            return False
            
    return True

def listar_vizinhos(vertices, arestas, vertice):

    lista = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {lista}")

def exibir_grafo(vertices, arestas):
    print(f"Vértices: {vertices}")
    print("Arestas:")

    for origem, destino in arestas:
        print(f"({origem} -> {destino})")


def main():
    vertices, arestas = criar_grafo()
    
    while True:
        print("\n--- MENU DO GRAFO ---")
        print("1 - Inserir Vértice")
        print("2 - Inserir Aresta")
        print("3 - Remover Vértice")
        print("4 - Remover Aresta")
        print("5 - Listar Vizinhos de um Vértice")
        print("6 - Ver Graus dos Vértices")
        print("7 - Verificar Percurso Válido")
        print("8 - Exibir Grafo")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        print("-" * 21)
        
        match opcao:
            case "1":
                v = input("Digite o nome do vértice: ")
                inserir_vertice(vertices, v)
                print("Vértice inserido.")
                
            case "2":
                origem = input("Vértice de origem: ")
                destino = input("Vértice de destino: ")
                nd = input("Aresta não direcionada? (s/n): ").strip().lower()
                nao_dir = (nd == 's')
                inserir_aresta(vertices, arestas, origem, destino, nao_dir)
                print("Aresta inserida.")
                
            case "3":
                v = input("Digite o nome do vértice a ser removido: ")
                remover_vertice(vertices, arestas, v)
                print("Vértice removido (se existia).")
                
            case "4":
                origem = input("Vértice de origem: ")
                destino = input("Vértice de destino: ")
                nd = input("Aresta não direcionada? (s/n): ").strip().lower()
                nao_dir = (nd == 's')
                remover_aresta(arestas, origem, destino, nao_dir)
                print("Aresta removida (se existia).")
                
            case "5":
                v = input("Digite o nome do vértice: ")
                listar_vizinhos(vertices, arestas, v)
                
            case "6":
                graus = grau_vertices(vertices, arestas)
                for v, infos in graus.items():
                    print(f"Vértice {v}: {infos}")
                    
            case "7":
                caminho_str = input("Digite o caminho separado por vírgulas (ex: a, b, d): ")
                
                caminho = [v.strip() for v in caminho_str.split(',')]
                
                if percurso_valido(arestas, caminho):
                    print("O percurso é válido.")
                else:
                    print("O percurso NÃO é válido.")
                    
            case "8":
                exibir_grafo(vertices, arestas)
                
            case "0":
                print("Saindo do programa...")
                break
                
            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
