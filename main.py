import dados
import utils


def main():
    while True:
        try:
            utils.limpar()
            print(utils.menu())
            opcao = int(input("> "))
            if opcao == 1:

                nome = input("> NOME: ").upper()
                while not utils.validar_nome(nome):
                    nome = input("> NOME: ").upper()

                altura = input("> ALTURA: ")
                while not utils.validar_numero(altura):
                    altura = input("> ALTURA: ")
                altura = float(altura)

                peso = input("> PESO: ")
                while not utils.validar_numero(peso):
                    peso = input("> PESO: ")
                peso = float(peso)

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
                utils.pausar()
                break

        except Exception as erro:
            print(f"Erro: {erro}")
            utils.pausar()
            input("Pressione qualquer tecla para voltar...")


if __name__ == "__main__":
    main()
