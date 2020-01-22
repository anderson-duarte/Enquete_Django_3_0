from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Opcao, Questao
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request):
# FUNCIONA LEGAL O CODIGO COMENTADO
    lista_ultimas_questoes = Questao.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('polls/index.html')
    context = {'questoes': lista_ultimas_questoes}
#    return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, questao_id):
    try:
        questao = Questao.objects.get(pk=questao_id)
    except Questao.DoesNotExist:
        raise Http404('Questão encontrada!')
    context = {'questao' : questao}
    return render(request, 'polls/detail.html', context)


def results(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'polls/results.html', {'questao': questao})


def vote(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        seleciona_opcao = questao.opcao_set.get(pk = request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'polls/detail.html', {'questao' : questao,
                                                    'error_message': 'Você não selecionou uma opção'})
    else:
        seleciona_opcao.votos += 1
        seleciona_opcao.save()
    return HttpResponseRedirect(reverse('polls:results', args=(questao.id,)))