from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms

def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    context = {
        'form': form,
        'pessoa_form': pessoa_form
    }
    return render(request, 'index.html', context)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        # verifica se o formulário é válido:
        if form.is_valid():
            context = {
                'form': form,
                'pessoa_form': pessoa_form
            }
            return render(request, 'minha_consulta.html', context)
        else:
            context = {'form': form }
            return render(request, 'index.html', context)
