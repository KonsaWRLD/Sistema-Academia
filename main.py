import os
import dados


def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print(dados.menu())
            opcao = int(input("> "))
            if opcao == 1:
                nome = input("> NOME: ").upper()
                altura = float(input("> ALTURA: "))
                peso = float(input("> PESO: "))
                dados.criar_aluno(nome, altura, peso)
            elif opcao == 2:
                dados.ver_alunos()
            elif opcao == 3:
                pesquisa = input("Informe o nome do aluno: ").upper()
                dados.pesquisar_aluno(pesquisa)
            elif opcao == 4:
                pesquisa = input("Informe o nome do aluno: ").upper()
                dados.remover_aluno(pesquisa)
            elif opcao == 5:
                dados.media_pesos()
            elif opcao == 0:
                print("Saindo...")
                break
        except Exception as erro:
            print(erro)
            input("Pressione qualquer tecla para voltar...")


if __name__ == "__main__":
    main()
