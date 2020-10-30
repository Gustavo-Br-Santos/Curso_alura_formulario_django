from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label="Ida", widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices= tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)



    """
    Serão mantidas para estudo, embora não vai mais ser usado mai no programa,
    visto que irei criar um arquivo novo responsável pela validação do formulário.    
    """

    # def clean_origem(self):
    #     """
    #     Método para validar o campo origem do formulário formulário
    #     Esse método pode ser ideal para testar um campo do formulário,
    #     porém, não é o mais indicado para fazer validação de vários campos, 
    #     visto que seria necessário um método para cada atributo da classe.
    #     """
    #     # origem = self.cleaned_data['origem']  # Retorna um erro caso o campo esteja vazio
    #     origem = self.cleaned_data.get('origem')  # retorna None caso o campo esteja vazio
    #     if any(char.isdigit() for char in origem):
    #         raise forms.ValidationError('Origem inválida. Não inclua números!')
    #     else:
    #         return origem

    
    def clean(self):
        """
        O método clean pode ser usado para uma validação generica para
        todos os atributos do formulário. Com isso, tanto as validações feitas 
        com a classe clean origem também poderiam ser feitas dentro desse método.
        """
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}

        campo_tem_caractere_numerico(origem, 'origem', lista_erros)
        campo_tem_caractere_numerico(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_erros)
        data_ida_maenor_data_de_hoje(data_ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data


