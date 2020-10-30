def origem_destino_iguais(origem, destino, lista_erros):
    """Verifica se a origem e o destino são iguais"""
    if origem == destino:
        # Armazena em destino a mensagem de erro
        lista_erros['destino'] = 'Origem e destino não podem ser iguais!'

def campo_tem_caractere_numerico(valor_campo, nome_campo, lista_erros):
    """Verifica se possue números no campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Origem inválida. Não inclua números!'


def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    """ Verifica se a data de ida é maior que a data de volta """
    if data_ida > data_volta:
        lista_erros['data_volta'] = "Data de volta não pode ser antes da data de ida!"

def data_ida_maenor_data_de_hoje(data_ida, data_pesquisa, lista_erros):
    """ Verifica se a data de ida é maenor que a data de hoje """
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = "Data de ida não pode ser antes de hoje!"