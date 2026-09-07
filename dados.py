import calculos
import utils

alunos = [
    {"nome": "CARLOS", "altura": 1.80, "peso": 80.0, "imc": 24.69, "status": "Normal"},
    {"nome": "ANA", "altura": 1.65, "peso": 60.0, "imc": 22.04, "status": "Normal"},
]


def ver_alunos():
    if not alunos:
        print(utils.aviso("Nenhum aluno cadastrado no momento.\n"))
        utils.pausar()
        return
    for aluno in alunos:
        print(
            f"{utils.titulo('Dados do aluno')}\n"
            f"  Nome   : {aluno['nome']}\n"
            f"  Altura : {aluno['altura']:.2f} m\n"
            f"  Peso   : {aluno['peso']:.2f} kg\n"
            f"  IMC    : {aluno['imc']:.2f}\n"
            f"  Status : {aluno['status']}\n"
        )
    utils.pausar_com_mensagem()


def criar_aluno(nome, altura, peso):
    imc = calculos.calcular_imc(peso, altura)
    nivel = utils.status(imc)
    novo_aluno = {
        "nome": nome,
        "altura": altura,
        "peso": peso,
        "imc": imc,
        "status": nivel,
    }
    alunos.append(novo_aluno)
    print(utils.sucesso(f"{nome} foi adicionado(a) com sucesso.\n"))
    utils.pausar()
    utils.pausar_com_mensagem()


def pesquisar_aluno(nome_aluno):
    encontrado = False
    for aluno in alunos:
        if nome_aluno == aluno["nome"]:
            print(
                f"{utils.titulo('Aluno encontrado')}\n"
                f"  Nome   : {aluno['nome']}\n"
                f"  Altura : {aluno['altura']:.2f} m\n"
                f"  Peso   : {aluno['peso']:.2f} kg\n"
                f"  IMC    : {aluno['imc']:.2f}\n"
                f"  Status : {aluno['status']}\n"
            )
            utils.pausar_com_mensagem()
            encontrado = True
            break
    if encontrado == False:
        print(utils.aviso(f"{nome_aluno} nao encontrado.\n"))
        utils.pausar()


def remover_aluno(nome_aluno):
    encontrado = False
    for aluno in alunos:
        if nome_aluno == aluno["nome"]:
            alunos.remove(aluno)
            print(utils.sucesso(f"{aluno['nome']} removido com sucesso.\n"))
            utils.pausar()
            utils.pausar_com_mensagem()
            encontrado = True
    if not encontrado:
        print(utils.aviso(f"{nome_aluno} nao encontrado.\n"))
        utils.pausar()


def media_pesos():
    if not alunos:
        print("Não há alunos para calcular a média.\n")
        utils.pausar()
        return

    pesos = [aluno["peso"] for aluno in alunos]
    media = sum(pesos) / len(pesos)
    print(utils.sucesso(f"Peso medio dos alunos: {media:.2f} kg\n"))
    utils.pausar()
    utils.pausar_com_mensagem()
