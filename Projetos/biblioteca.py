import psycopg2 #Para instalar > pip install psycopg2 

def createTableLivro(cur,conexao):

    cur.execute('''
    CREATE TABLE "Livros"(
    "ID" serial,
    "Nome" varchar(255),
    "Livro_pagnias" varchar(255),
    "Livro_anolançamento" varchar(255),
    "Livro_autor" varchar(255),
    PRIMARY KEY("ID")
    );
    ''')
    conexao.commit()

def inserirLivro(cur,conexao):
    cur.execute('''
    INSERT INTO "Livros"
    VALUES(default, ' Rei Leão', '200','2002','Albert' default)
    ''')
    conexao.commit()


def removerLivro(cur, conexao):
    idFunc = int(input("Digite o id do Livro que deseja modificar: "))
    cur.execute(f'''
    DELETE FROM "Livros"
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()
    
def listarLivro(cur, conexao):

    cur.execute('''
    SELECT * FROM "Livros"
    ''')
    print(cur.fetchall())


while True:
    try:

        con = psycopg2.connect(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")
        #(database="Empresa",user="postgres", password="postgres", host="localhost", port="5432")

        cursor = con.cursor()
        print("Conectado")

        print('''
        1. Ver Livros
        2. Inserir Livro
        3. Remover Livro
        0. Sair do Programa
        ''')

        opcaoMenu = input("Escolha o que deseja fazer: ")

        match opcaoMenu:
            case "1":
                listarLivro(cursor, con)
            case "2":
                inserirLivro(cursor, con)
            case "3":
                removerLivro(cursor, con)
            case "0":
                print("Você escolheu sair da aplicação. Até mais!")
                break
            case _:
                print("Você inseriu algum valor inválido.")
                
        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)