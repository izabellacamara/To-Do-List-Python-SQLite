import sqlite3


# Conectar ao banco de dados
conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()


# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT NOT NULL,
    concluida INTEGER DEFAULT 0
)
""")

conexao.commit()


def criar_tarefa():
    tarefa = input("Digite a tarefa: ")

    cursor.execute(
        "INSERT INTO tarefas (tarefa) VALUES (?)",
        (tarefa,)
    )

    conexao.commit()

    print("Tarefa criada com sucesso!")


def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for id, tarefa, concluida in tarefas:
        status = "Concluída" if concluida else "Pendente"

        print(f"{id} - {tarefa} - {status}")


def editar_tarefa():
    listar_tarefas()

    id_tarefa = input("Digite o ID da tarefa que deseja editar: ")
    nova_tarefa = input("Digite o novo nome da tarefa: ")

    cursor.execute(
        "UPDATE tarefas SET tarefa = ? WHERE id = ?",
        (nova_tarefa, id_tarefa)
    )

    conexao.commit()

    print("Tarefa editada com sucesso!")


def concluir_tarefa():
    listar_tarefas()

    id_tarefa = input("Digite o ID da tarefa concluída: ")

    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()

    print("Tarefa concluída!")


def excluir_tarefa():
    listar_tarefas()

    id_tarefa = input("Digite o ID da tarefa que deseja excluir: ")

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()

    print("Tarefa excluída com sucesso!")


def filtrar_tarefas():
    print("\n1 - Pendentes")
    print("2 - Concluídas")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cursor.execute(
            "SELECT * FROM tarefas WHERE concluida = 0"
        )

    elif opcao == "2":
        cursor.execute(
            "SELECT * FROM tarefas WHERE concluida = 1"
        )

    else:
        print("Opção inválida.")
        return

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for id, tarefa, concluida in tarefas:
        status = "Concluída" if concluida else "Pendente"

        print(f"{id} - {tarefa} - {status}")


# Menu principal
while True:

    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Concluir tarefa")
    print("5 - Excluir tarefa")
    print("6 - Filtrar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        editar_tarefa()

    elif opcao == "4":
        concluir_tarefa()

    elif opcao == "5":
        excluir_tarefa()

    elif opcao == "6":
        filtrar_tarefas()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")


conexao.close()