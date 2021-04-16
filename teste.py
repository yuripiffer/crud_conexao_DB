nome="Ana Maria"
id=None
cpf=80
lista = [nome, id, cpf]
if any(lista):
    frase_where = "WHERE"
    if nome is not None:
        frase_where += f" nome = '{nome}',"
    if id is not None:
        frase_where += f" id = '{id}',"
    if cpf is not None:
        frase_where += f" cpf = '{cpf}',"
    print(frase_where)



# print(any(listao))
# if all[nome, id, cpf] != None:
#     print("Não tem none")