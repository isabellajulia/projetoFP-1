from django.shortcuts import render
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
	pessoas = Pessoa.objects.all().order_by('nome')
	return render(request,'fluxo/fluxoListar.html', {'pessoas': pessoas})

def fluxoPesquisar(request):
	if 	request.method =='POST': 
		pessoaBusca = request.POST.get ('pessoaBusca')
		dataBuscaInicio = datetime.strptime(request.POST.get('dataBuscaInicio', ''), '%d/%m/%Y %H:%M:%S')
		dataBuscaFim = datetime.strptime(request.POST.get('dataBuscaFim') , '%d/%m/%Y %H:%M:%S')

		nome = Pessoa.objects.filter(id=pessoaBusca)
		pessoas = Pessoa.objects.all().order_by('nome')

		totalReceber = 0 
		totalPagar = 0

		
		try:
			sql = "select * from caixas_conta where pessoa_id like %s and data >= '%s' and data <= '%s'" % (pessoaBusca, dataBuscaInicio, dataBuscaFim)
			contas = Conta.objects.raw(sql)

			for item in contas:
				if item.tipo == 'E':
					totalReceber = totalReceber + item.valor
				else:
					totalPagar = totalPagar + item.valor
			except:
				contas = [Conta(descricao='erro')]
			return render(request, 'fluxos/fluxoListar.html'), {'contas': contas, 'nome':nome, 'pessoas': pessoas, 'totalReceber': totalReceber, 'totalPagar': totalPagar})

# Create your views here.
