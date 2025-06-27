# Criando um codigo para verificar se o usuario esta inativo
# Se o usuario não usa o programa a mais de uma semana ele vai ser considerado inativo
# O programa vai ficar verificando se o usuario esta ativo ou inativo de acordo com o tempo que ele esta sem usar o programa
# Se o usuario estiver inativo ele vai ser deslogado automaticamente

import datetime

# Criando uma funcao para verificar se o usuario esta ativo ou inativo:
def verifica_inativos():
    # Pegando a data atual
    data_atual = datetime.datetime.now()

    # Verificando se o usuario esta ativo ou inativo
    if data_atual - data_ultimo_acesso > datetime.timedelta(days=7):
        print('Usuario inativo')
    else:
        print('Usuario ativo')

    # Atualizando a data do ultimo acesso
    data_ultimo_acesso = data_atual

     # Retornando a data do ultimo acesso
    return data_ultimo_acesso

# Vinculando a variavel data_ultimo_acesso a funcao verifica_inativos
data_ultimo_acesso = verifica_inativos()

# Exemplo de uso
if __name__ == "__main__":
    verifica_inativos()
    
