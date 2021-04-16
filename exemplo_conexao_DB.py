import MySQLdb

# CONECTANDO COM O DB
conexao = MySQLdb.connect(db='Llama', user="root", host="localhost", port=3306)
#Como estou usando o Xammp, uso localhost
cursor = conexao.cursor()



# cursor.execute("select * from tabela_teste")
# cursor.fetchall() #retonra os valores do banco... dar print se quiser
# for col in cursor.description: #PARA TRAZER OS TÍTULOS DA COLUNA
#     print(col[0])

# # Inserir valores
# nome = input("Digite o nome:")
# cpf = input("Digite o CPF:")
# cursor.execute(f"INSERT INTO tabela_teste VALUES ('{nome}', DEFAULT, '{cpf}' )")
# conexao.commit() #vai persistir no banco

# # update de dados
# nome = input("Digite o nome:")
# comando_update = f"""
#     UPDATE tabela_teste
#     SET nome = '{nome}'
#     WHERE cpf = '123123123'
#     """
# cursor.execute(comando_update)
# conexao.commit()


# # Deletar dados
# comando_delete = f"""
#     DELETE FROM tabela_teste
#     WHERE cpf = '080400'
#     """
# cursor.execute(comando_delete)
# conexao.commit()