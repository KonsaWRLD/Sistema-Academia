import calculos
import utils

alunos = [
    {"nome": "CARLOS", "altura": 1.80, "peso": 80.0, "imc": 24.69, "status": "Normal"},
    {"nome": "ANA", "altura": 1.65, "peso": 60.0, "imc": 22.04, "status": "Normal"},
]


def ver_alunos():
    if not alunos:
        print("Ops! Sem alunos cadastrados no momento.\n")
        utils.pausar()
        return
    for aluno in alunos:
        print(
            f"NOME: {aluno['nome']}\nALTURA: {aluno['altura']}\nPESO: {aluno['peso']}\nIMC: {aluno['imc']:.2f}\nSTATUS: {aluno['status']}\n"
        )
    input("Pressione qualquer tecla para voltar...")


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
    print(f"{nome} foi adicionado(a) com sucesso!\n")
    utils.pausar()
    input("Pressione qualquer tecla para voltar...")


def pesquisar_aluno(nome_aluno):
    encontrado = False
    for aluno in alunos:
        if nome_aluno == aluno["nome"]:
            print(
                f"NOME: {aluno['nome']}\nALTURA: {aluno['altura']}\nPESO: {aluno['peso']}\nIMC: {aluno['imc']:.2f}\nSTATUS: {aluno['status']}\n"
            )
            input("Pressione qualquer tecla para voltar...")
            encontrado = True
            break
    if encontrado == False:
        print(f"{nome_aluno} não encontrado!\n")
        utils.pausar()


def remover_aluno(nome_aluno):
    encontrado = False
    for aluno in alunos:
        if nome_aluno == aluno["nome"]:
            alunos.remove(aluno)
            print(f"{aluno['nome']} removido com sucesso!\n")
            utils.pausar()
            input("Pressione qualquer tecla para voltar...")
            encontrado = True
    if not encontrado:
        print(f"{nome_aluno} não encontrado!\n")
        utils.pausar()


def media_pesos():
    if not alunos:
        print("Não há alunos para calcular a média.\n")
        utils.pausar()
        return

    pesos = [aluno["peso"] for aluno in alunos]
    media = sum(pesos) / len(pesos)
    print(f"Peso médio dos alunos: {media:.2f}\n")
    utils.pausar()
    input("Pressione qualquer tecla para voltar...")
