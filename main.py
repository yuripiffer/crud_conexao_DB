import MySQLdb
import pandas as pd

"""
1.	Criar uma classe para o banco de dados
2.	Criar funções para todas as operações de CRUD
3.	Deve ser possível executar as funções com e sem WHERE
4.	A listagem (em print()) deve ser feita em formato de tabela
•	Ex: 
•	Nome – Cpf – Idade – Altura
•	Gustavo – 000 – 100 – 1.8
•	Amanda – 154 – 45 – 1.64

5.	Deve ser feito o tratamento de erro para caso o usuário faça 
besteira (exceto em coisas sem controle do programador. 
Ex: problema interno do banco)
"""


class ConnectDB():
    def __init__(self, db_name: str, user="root", host="localhost", port=3306):
        self.db_name = db_name
        self.user = user
        self.host = host
        self.port = port
        self.conexao = MySQLdb.connect(db=self.db_name, user=self.user, host=self.host, port=self.port)
        self.cursor = self.conexao.cursor()

    def executa_e_persiste(self, comando:str):
        self.cursor.execute(comando)
        self.conexao.commit()

    def crud_create(self, tabela: str, nome: str, cpf: str, idade:int, altura:float):
        # try:
        #     if nome
        # except:
        #
        #     pass
        # else:
        comando = f"INSERT INTO {tabela} VALUES ('{nome}', DEFAULT, '{cpf}', '{idade}','{altura}' )"
        self.executa_e_persiste(comando)

    def crud_read(self, tabela: str):
        self.cursor.execute(f"select * from {tabela}")
        lista_nomes_colunas=[]
        for col in self.cursor.description:
            lista_nomes_colunas.append(col[0])
        print(pd.DataFrame(self.cursor.fetchall(), columns=lista_nomes_colunas))

    def crud_update(self, tabela: str, id: int, nome=None, cpf=None, idade=None, altura=None):

        #validação de try / except (sem while)
        lista = [nome, cpf, idade, altura]
        if any(lista):
            frase_set = "SET "
            if nome is not None:
                frase_set += f" nome = '{nome}' ,"
            if cpf is not None:
                frase_set += f" cpf = '{cpf}' ,"
            if idade is not None:
                frase_set += f" idade = '{idade}' ,"
            if altura is not None:
                frase_set += f" altura = '{altura}' ,"
            frase_set = frase_set[:-2]  # exclui vírgula e espaço

            comando = f"UPDATE {tabela} " + frase_set + f" WHERE id = {id}"
            self.executa_e_persiste(comando)

    def crud_delete(self, tabela: str, nome=None, id=None, cpf=None, idade=None, altura=None):
        lista = [nome, id, cpf, idade, altura]
        if any(lista):
            frase_where = "WHERE "
            if nome is not None:
                frase_where += f"nome = '{nome}' and "
            if id is not None:
                frase_where += f"id = {id} and "
            if cpf is not None:
                frase_where += f"cpf = '{cpf}' and "
            if idade is not None:
                frase_where += f"cpf = '{idade}' and "
            if altura is not None:
                frase_where += f"cpf = '{altura}' and "
            frase_where = frase_where[:-4]  # exlcui o 'and '
            comando = f"DELETE FROM {tabela} " + frase_where
            self.executa_e_persiste(comando)
        else:
            #Delete all
            comando = f"DELETE FROM {tabela}"
            self.executa_e_persiste(comando)







testeDB = ConnectDB(db_name="Llama")
#testeDB.crud_create("tabela_teste","Lara", "02000", 29, 1.89)
#testeDB.crud_update("tabela_teste",id=16, nome="NomePorUpdate", cpf="111111")
testeDB.crud_read("tabela_teste")
#esteDB.crud_delete("tabela_teste", nome="Maria")


# testeDB.crud_create("tabela_teste","Ana", "01000", 29, 1.89)
# testeDB.crud_create("tabela_teste","Yuri", "02000", 65, 1.69)
# testeDB.crud_create("tabela_teste","Flavia", "03000", 22, 1.76)
# testeDB.crud_create("tabela_teste","Maria", "04000", 29, 1.66)
# testeDB.crud_create("tabela_teste","Naiane", "05000", 86, 1.67)


