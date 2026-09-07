import dados
import utils


def main():
    utils.habilitar_cores()
    while True:
        try:
            utils.limpar()
            print(utils.menu())
            opcao = int(
                input(
                    f"{utils.CYAN}Escolha uma opcao{utils.RESET} {utils.WHITE}> {utils.RESET}"
                )
            )
            if opcao == 1:

                nome = input(
                    f"{utils.CYAN}NOME{utils.RESET} {utils.WHITE}> {utils.RESET}"
                ).upper()
                while not utils.validar_nome(nome):
                    nome = input(
                        f"{utils.CYAN}NOME{utils.RESET} {utils.WHITE}> {utils.RESET}"
                    ).upper()

                altura = input(
                    f"{utils.CYAN}ALTURA (m){utils.RESET} {utils.WHITE}> {utils.RESET}"
                )
                while not utils.validar_numero(altura):
                    altura = input(
                        f"{utils.CYAN}ALTURA (m){utils.RESET} {utils.WHITE}> {utils.RESET}"
                    )
                altura = float(altura)

                peso = input(
                    f"{utils.CYAN}PESO (kg){utils.RESET} {utils.WHITE}> {utils.RESET}"
                )
                while not utils.validar_numero(peso):
                    peso = input(
                        f"{utils.CYAN}PESO (kg){utils.RESET} {utils.WHITE}> {utils.RESET}"
                    )
                peso = float(peso)

                dados.criar_aluno(nome, altura, peso)

            elif opcao == 2:
                dados.ver_alunos()

            elif opcao == 3:
                pesquisa = input(
                    f"{utils.CYAN}Nome do aluno{utils.RESET} {utils.WHITE}> {utils.RESET}"
                ).upper()
                dados.pesquisar_aluno(pesquisa)

            elif opcao == 4:
                pesquisa = input(
                    f"{utils.CYAN}Nome do aluno{utils.RESET} {utils.WHITE}> {utils.RESET}"
                ).upper()
                dados.remover_aluno(pesquisa)

            elif opcao == 5:
                dados.media_pesos()

            elif opcao == 0:
                print(utils.aviso("Saindo..."))
                utils.pausar()
                break

        except Exception as erro:
            print(utils.erro(str(erro)))
            utils.pausar()
            utils.pausar_com_mensagem()


if __name__ == "__main__":
    main()
