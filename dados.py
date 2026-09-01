import calculos

alunos = [
    {"nome": "CARLOS", "altura": 1.80, "peso": 80.0, "imc": 24.69, "status": "Normal"},
    {"nome": "ANA", "altura": 1.65, "peso": 60.0, "imc": 22.04, "status": "Normal"},
]


def menu():
    return """1. Cadastrar aluno
2. Ver alunos
3. Pesquisar alunos
4. Remover aluno
0. Sair\n"""


def ver_alunos():
    if not alunos:
        print("Ops! Sem alunos cadastrados no momento.")
        return
    for aluno in alunos:
        print(
            f"NOME: {aluno['nome']}\nALTURA: {aluno['altura']}\nPESO: {aluno['peso']}\nIMC: {aluno['imc']:.2f}\nSTATUS: {aluno['status']}\n"
        )
    input("Pressione qualquer tecla para voltar...")


def status(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 39.9:
        return "Obesidade"
    else:
        return "Obesidade Grave"


def criar_aluno(nome, altura, peso):
    imc = calculos.calcular_imc(peso, altura)
    nivel = status(imc)
    novo_aluno = {
        "nome": nome,
        "altura": altura,
        "peso": peso,
        "imc": imc,
        "status": nivel,
    }
    alunos.append(novo_aluno)

    print(f"{nome} foi adicionado(a) com sucesso!")
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
        print(f"{nome_aluno} não encontrado!")


def remover_aluno(nome_aluno):
    encontrado = False
    for aluno in alunos:
        if nome_aluno == aluno["nome"]:
            alunos.remove(aluno)
            print(f"{aluno['nome']} removido com sucesso!")
            input("Pressione qualquer tecla para voltar...")
            encontrado = True
    if not encontrado:
        print(f"{nome_aluno} não encontrado!")
