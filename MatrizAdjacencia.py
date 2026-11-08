def criar_grafo():
   matriz = []
   vertices = []
   return matriz, vertices
pass

def inserir_vertice(matriz, vertices, vertice):
  if vertice not in vertices:
      vertices.append(vertice)
  for linha in matriz:
    linha.append(0)
  nova_linha = [0] * len(vertices)
  matriz.append(nova_linha)
 
pass

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index (origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz [j][i] = 1
pass

def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        indice = vertices.index(vertice)
        vertices.pop(indice)
        matriz.pop(indice)
        for linha in matriz:
            linha.pop(indice)
pass

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
   
     i = vertices.index (origem)
     j = vertices.index(destino)
   
     matriz[i][j] = 0
     if nao_direcionado:
            matriz [j][i] = 0
pass

def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return(False)
    i = vertices.index(origem)
    j = vertices.index(destino)




    if matriz[i][j] == 1:
        return True
    else:
        return False
   
pass

def vizinhos(matriz, vertices, vertice):
   
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)

    lista_vizinhos = []

    for j, valor in enumerate(matriz[i]):
        if valor == 1:
            lista_vizinhos.append(vertices[j])




    return lista_vizinhos
       
pass


def grau_vertices(matriz, vertices):
    graus = {}
   
   
    for i, vertice in enumerate(vertices):
       
       
        grau_saida = sum(matriz[i])
       
       
        grau_entrada = sum(linha[i] for linha in matriz)
       
       
        grau_total = grau_saida + grau_entrada
       
       
        graus[vertice] = {
            "saida": grau_saida,
            "entrada": grau_entrada,
            "total": grau_total
        }
   
    return graus
   
   
pass

def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
       
        u = caminho[i]
        v = caminho[i+1]
       
        if not existe_aresta(matriz, vertices, u, v):
           
            return False
           
    return True
pass


def listar_vizinhos(matriz, vertices, vertice):
   if vertice not in vertices:
       print("Vértice não encontrado")
       return
   lista = vizinhos(matriz, vertices, vertice)
   print(f"Viinhos de {vertice}: {lista}")
       
pass

def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio")
        return
    cabecalho = " " + " ".join(vertices)
    print (cabecalho)
   
    for i, linha in enumerate(matriz):
        valores_linha = " ".join(map(str, linha))
        print(f"{vertices[i]}  {valores_linha}")
pass

def main():
    matriz, vertices = criar_grafo()


    while True:
        print("\n--- MENU GRAFO (MATRIZ DE ADJACÊNCIA) ---")
        print("1 - Inserir vértice")
        print("2 - Inserir aresta")
        print("3 - Remover vértice")
        print("4 - Remover aresta")
        print("5 - Verificar se existe aresta")
        print("6 - Listar vizinhos de um vértice")
        print("7 - Exibir graus dos vértices")
        print("8 - Verificar percurso")
        print("9 - Exibir matriz do grafo")
        print("0 - Sair")


        opcao = input("Escolha uma opção: ").strip()


        match opcao:
            case "1":
                v = input("Nome do vértice: ").strip()
                inserir_vertice(matriz, vertices, v)
                print(f"Vértice '{v}' adicionado com sucesso.")


            case "2":
                origem = input("Vértice de origem: ").strip()
                destino = input("Vértice de destino: ").strip()
                tipo = input("Grafo não direcionado (mão dupla)? (s/n): ").strip().lower()
                nao_dir = tipo == "s"
                inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=nao_dir)
                print(f"Aresta entre '{origem}' e '{destino}' criada com sucesso.")


            case "3":
                v = input("Vértice a remover: ").strip()
                remover_vertice(matriz, vertices, v)
                print(f"Vértice '{v}' (e as suas ligações) removido.")


            case "4":
                origem = input("Vértice de origem: ").strip()
                destino = input("Vértice de destino: ").strip()
                tipo = input("Remover em ambos os sentidos? (s/n): ").strip().lower()
                nao_dir = tipo == "s"
                remover_aresta(matriz, vertices, origem, destino, nao_direcionado=nao_dir)
                print(f"Aresta entre '{origem}' e '{destino}' removida.")


            case "5":
                origem = input("Vértice de origem: ").strip()
                destino = input("Vértice de destino: ").strip()
                existe = existe_aresta(matriz, vertices, origem, destino)
                if existe:
                    print(f"Sim, existe aresta direta de '{origem}' para '{destino}'.")
                else:
                    print(f"Não existe aresta de '{origem}' para '{destino}'.")


            case "6":
                v = input("Vértice para listar vizinhos: ").strip()
                listar_vizinhos(matriz, vertices, v)


            case "7":
                graus = grau_vertices(matriz, vertices)
                print("\nGraus dos vértices:")
                for v, g in graus.items():
                    print(f"Vértice {v}: Saída = {g['saida']} | Entrada = {g['entrada']} | Total = {g['total']}")


            case "8":
                caminho_str = input("Introduza o percurso separado por vírgulas (ex: A,B,C): ")
                caminho = [vertice.strip() for vertice in caminho_str.split(",") if vertice.strip()]
                if not caminho:
                    print("Percurso vazio inválido.")
                else:
                    valido = percurso_valido(matriz, vertices, caminho)
                    if valido:
                        print(f"O percurso {' -> '.join(caminho)} é válido!")
                    else:
                        print(f"O percurso {' -> '.join(caminho)} NÃO é possível no grafo.")


            case "9":
                print("\nEstado atual da matriz de adjacência:")
                exibir_grafo(matriz, vertices)


            case "0":
                print("A encerrar o programa...")
                break


            case _:
                print("Opção inválida! Tente novamente.")




if __name__ == "__main__":
    main()









