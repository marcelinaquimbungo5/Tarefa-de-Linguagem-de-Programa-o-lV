# Questão 3 - Sistema Integrado de Informação
# Direção Provincial da Saúde do Uíge
#
# O sistema permite:
#   1. Registar unidades de saúde (hospitais, centros de saúde)
#   2. Registar pacientes
#   3. Registar consultas no histórico clínico
#   4. Consultar o histórico de um paciente (partilha de dados
#      entre todas as unidades)
#   5. Coordenar serviços: transferir um paciente para outra unidade
#
# Os dados ficam guardados em dicionários e listas (memória).

unidades = {}    # codigo -> {"nome": ..., "servicos": [...]}
pacientes = {}   # id -> {"nome": ..., "idade": ..., "unidade": codigo}
historico = {}   # id do paciente -> lista de consultas
proximo_id = 1


def registar_unidade():
    print("\n--- Registar unidade de saúde ---")
    codigo = input("Código da unidade (ex: HGU): ").upper()
    if codigo in unidades:
        print("Essa unidade já existe!")
        return
    nome = input("Nome da unidade: ")
    servicos = input("Serviços (separados por vírgula): ").split(",")
    unidades[codigo] = {"nome": nome, "servicos": [s.strip() for s in servicos]}
    print("Unidade registada com sucesso!")


def registar_paciente():
    global proximo_id
    print("\n--- Registar paciente ---")
    if len(unidades) == 0:
        print("Registe primeiro uma unidade de saúde.")
        return
    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    print("Unidades disponíveis:", ", ".join(unidades.keys()))
    unidade = input("Código da unidade de registo: ").upper()
    if unidade not in unidades:
        print("Unidade inexistente!")
        return
    pacientes[proximo_id] = {"nome": nome, "idade": idade, "unidade": unidade}
    historico[proximo_id] = []
    print("Paciente registado com o ID", proximo_id)
    proximo_id += 1


def registar_consulta():
    print("\n--- Registar consulta ---")
    id_pac = int(input("ID do paciente: "))
    if id_pac not in pacientes:
        print("Paciente não encontrado!")
        return
    data = input("Data (dd/mm/aaaa): ")
    unidade = input("Código da unidade onde foi atendido: ").upper()
    if unidade not in unidades:
        print("Unidade inexistente!")
        return
    diagnostico = input("Diagnóstico: ")
    historico[id_pac].append(
        {"data": data, "unidade": unidade, "diagnostico": diagnostico}
    )
    print("Consulta registada!")


def consultar_historico():
    print("\n--- Histórico clínico ---")
    id_pac = int(input("ID do paciente: "))
    if id_pac not in pacientes:
        print("Paciente não encontrado!")
        return
    p = pacientes[id_pac]
    print("Paciente:", p["nome"], "| Idade:", p["idade"])
    print("Unidade actual:", unidades[p["unidade"]]["nome"])
    if len(historico[id_pac]) == 0:
        print("Sem consultas registadas.")
    for c in historico[id_pac]:
        nome_unidade = unidades[c["unidade"]]["nome"]
        print(" -", c["data"], "|", nome_unidade, "|", c["diagnostico"])


def transferir_paciente():
    print("\n--- Transferir paciente ---")
    id_pac = int(input("ID do paciente: "))
    if id_pac not in pacientes:
        print("Paciente não encontrado!")
        return
    destino = input("Código da unidade de destino: ").upper()
    if destino not in unidades:
        print("Unidade inexistente!")
        return
    pacientes[id_pac]["unidade"] = destino
    print("Paciente transferido para", unidades[destino]["nome"])
    print("O histórico clínico acompanha o paciente.")


def listar_unidades():
    print("\n--- Unidades de saúde ---")
    for codigo, dados in unidades.items():
        print(codigo, "-", dados["nome"])
        print("   Serviços:", ", ".join(dados["servicos"]))
        total = 0
        for p in pacientes.values():
            if p["unidade"] == codigo:
                total += 1
        print("   Pacientes registados:", total)


def menu():
    while True:
        print("\n=== SISTEMA INTEGRADO DE INFORMAÇÃO - SAÚDE UÍGE ===")
        print("1 - Registar unidade de saúde")
        print("2 - Registar paciente")
        print("3 - Registar consulta")
        print("4 - Consultar histórico clínico")
        print("5 - Transferir paciente")
        print("6 - Listar unidades")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            registar_unidade()
        elif opcao == "2":
            registar_paciente()
        elif opcao == "3":
            registar_consulta()
        elif opcao == "4":
            consultar_historico()
        elif opcao == "5":
            transferir_paciente()
        elif opcao == "6":
            listar_unidades()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


menu()
