from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *
from passagens.models import Passagem, Pessoa, ClasseViagem

class PassagemForms(forms.ModelForm):
    """ 
    Agora vamos usar ModelForm, que indica que iremos usar os formulários
    com base nos nossos modelos.
    """
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())

    class Meta:

        """
        Quando trabalhamos com ModelForms, a classe Meta permite fazer a manipulação
        das informações que estão no nosso modelo para gerar o nosso formulário.
        Nela, nós passamos o modelo base que vamos utilizar e os campos desse
        modelo que iremos utilizar.

        Obs.1 O campo fiels irá exibir no formulário as labels da mesma forma
        que estão no modelo. Para melhorarmos o UX, podemos usar o atributo labels:

        Obs.2 Para alterar os campos, podemos usar a propriedade widgets.

        Obs.3 Perceba que, como o campo data_pesquisa possue várias alterações diferentes
        dos outros campos, podemos trazer apenas esse campo a parte com as características 
        desejadas. No nosso caso, importamos esse campo antes da classe Meta.
        """
        model = Passagem
        # fields = ['origem', 'destino'] - Podemos usar dessa forma para trazer apenas alguns campos desejados
        fields = '__all__'  # Ou dessa forma para trazer todos os campos
        labels = {
            'data_ida':'Data de ida',
            'data_volta':'Data de volta',
            'informacoes':'Informações',
            'classe_viagem':'Classe da viagem'
            }
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker(),
        }
        
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

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] # Tem a função oposta do fields. Em vez de trazer os campos entre colchetes, ele traz todos os campos, menos os que estão entre colchetes
        
