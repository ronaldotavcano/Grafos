def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):

    if vertice not in grafo:
        grafo[vertice] = []
   
def inserir_aresta(grafo, origem, destino, nao_direcionado=False):

    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    grafo[origem].append(destino)

    if nao_direcionado:
        grafo[destino].append(origem)

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

    for vertice, vizinhos in lista:
        print(f"{vertice} -> {vizinhos}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem not in grafo:
     return f"A {origem} não existe no grafo"

    if destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado:
        if destino in grafo:
            grafo[destino].remove(origem)
 
def remover_vertice(grafo, vertice, nao_direcionado=True):

    if vertice not in grafo:
        return f"O vértice {vertice} não existe no grafo"

    for outro_vertice in grafo:
        if vertice in grafo[outro_vertice]:
            grafo[outro_vertice].remove(vertice)

    del grafo[vertice]
   
def existe_aresta(grafo, origem, destino):

    if origem in grafo:
        if destino in grafo[origem]:
            return True
        else:
            return False
    return False

def grau_vertices(grafo):

    graus = {}

    for j in grafo:
        graus[j] = {'in': 0, 'out': len(grafo[j]), 'total': 0}

    for j in grafo:
        for v in grafo:
            if j in grafo[v]:
                graus[j]['in'] += 1

    for j in grafo:
        graus[j]['total'] = graus[j]['in'] + graus[j]['out']

    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range( len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]

        if not existe_aresta(grafo, origem, destino):
            return False

    return True

def main():
    grafo = criar_grafo()
    
    while True:
        print("\n" + "="*30)
        print("       MENU DO GRAFO")
        print("="*15)
        print("1 - Mostrar o grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos de um vértice")
        print("7 - Verificar se aresta existe")
        print("8 - Mostrar grau dos vértices")
        print("9 - Verificar percurso")
        print("0 - Sair")
        print("="*15)
        
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
            direcionado = input("A ligação é de sentido duplo (não-direcionada)? (s/n): ").strip().lower() == 's'
            inserir_aresta(grafo, origem, destino, direcionado)
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
                
        elif opcao == '0':
            print("A encerrar o programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
