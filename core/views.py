from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core.mail import send_mail_template
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
import time
from core.models.Contrato import Contrato
from core.models.Imovel import Imovel
from core.models.Cliente import Cliente
from core.models.Boleto import Boleto
from core.models.contato2 import Contato
from .forms import ContatoForm,AnuncieForm


def home(request):
    form = ContatoForm(request.POST, request.FILES or None)
    

    if form.is_valid():
        form.save()
        return redirect('conf')
    return render(request, 'index.html', {'form': form})


def conf(request):
    return render(request, 'confirma.html')


def catalogo(request):
    url = settings.URL_API + "imovel/"
    todos_imoveis = requests.api.get(url).json() 
    
    contexto = {

        'imoveis': todos_imoveis
    }

    return render(request, 'catalogo.html', contexto)


def anuncie(request):
    form = AnuncieForm(request.POST, request.FILES or None)
    

    if form.is_valid():
        form.save()
        return redirect('conf')
    return render(request, 'anuncie.html', {'form': form})


def servicos(request):
    return render(request, 'servicos.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    form = ContatoForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('conf')
    return render(request, 'contato.html', {'form': form})



def financiamento(request):
    return render(request, 'financiamento.html')


def corretores(request):
    url = settings.URL_API + "corretor/"
    todos_corretores = requests.api.get(url).json()

    print(todos_corretores)
    context = {
        'corretores': todos_corretores
    }
    return render(request, 'corretores.html', context)


def trabalhe(request):
    return render(request, 'trabalhe.html')


def sair(request):
    logout(request)
    return redirect('/')


def registrar(request):
    return redirect('/')


def home_sistema(request):
    url = settings.URL_API + "imovel/"
    todos_imoveis = requests.api.get(url).json()
    boletos = Boleto.objects.all()

    contexto = {
        'imoveis': todos_imoveis,
        'boletos': boletos
    }

    return render(request, 'sistema/index.html', contexto)


def cadastro(request):
    return render(request, 'sistema/cadastro.html')


def login_page(request):
    context = {
        'error_msg': ''
    }

    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_URL_REDIRECT)
        else:
            context = {
                'error_msg': 'Senha e/ou usuário inválido.'
            }
            return render(request, 'sistema/login.html', context)

    return render(request, 'sistema/login.html', context)


def atualizar_view_cliente(request, pk):
    url_cliente = settings.URL_API + f"cliente/{pk}"
    cliente = requests.api.get(url_cliente).json()

    return JsonResponse(cliente)


def atualizar_view_imovel(request, pk):
    url_imovel = settings.URL_API + f"imovel/{pk}"
    imovel = requests.api.get(url_imovel).json()

    return JsonResponse(imovel)


def atualizar_view_corretor(request, pk):
    url_corretor = settings.URL_API + f"corretor/{pk}"
    corretor = requests.api.get(url_corretor).json()

    return JsonResponse(corretor)


def atualizar_view_proprietario(request, pk):
    url_proprietario = settings.URL_API + f"proprietario/{pk}"
    proprietario = requests.api.get(url_proprietario).json()

    return JsonResponse(proprietario)


def get_token(request):
    url = settings.URL_API + f"token/"
    response = requests.api.post(url, data={
        'username': settings.LOGIN_API,
        'password': settings.PASSWORD_API
    }).json()

    return {'Authorization': 'Bearer ' + response['access']}


def delete_cliente(request, pk):
    headers = get_token(request)
    url = settings.URL_API + f"cliente/{pk}"
    requests.api.delete(url, headers=headers)

    return redirect('/cadastro/clientes')


def delete_corretor(request, pk):
    headers = get_token(request)
    url = settings.URL_API + f"corretor/{pk}"
    requests.api.delete(url, headers=headers)

    return redirect('/cadastro/corretores')


def delete_imovel(request, pk):
    headers = get_token(request)
    url = settings.URL_API + f"imovel/{pk}"
    requests.api.delete(url, headers=headers)

    return redirect('/cadastro/imoveis')


def delete_proprietario(request, pk):
    headers = get_token(request)
    url = settings.URL_API + f"proprietario/{pk}"
    requests.api.delete(url, headers=headers)

    return redirect('/cadastro/proprietarios')


def cadastro_clientes(request):
    url = settings.URL_API + "cliente/"
    todos_clientes = requests.api.get(url).json()

    context = {
        'clientes': todos_clientes
    }

    if request.method == "POST":
        cliente = {}
        cliente['nome'] = request.POST.get("nome")
        cliente['cpf'] = request.POST.get("cpf")
        cliente['rg'] = request.POST.get("rg")
        cliente['cnpj'] = request.POST.get("cnpj")
        cliente['endereco'] = request.POST.get("endereco")
        cliente['bairro'] = request.POST.get("bairro")
        cliente['cep'] = request.POST.get("cep")
        cliente['cidade'] = request.POST.get("cidade")
        cliente['uf'] = request.POST.get("uf")
        cliente['email'] = request.POST.get("email")
        cliente['telefone'] = request.POST.get("telefone")
        cliente['pessoa_juridica'] = True if request.POST.get(
            "pj") == "pj_true" else False
        cliente['inquilino'] = True if request.POST.get(
            "inquilino") == "inquilino_true" else False

        retorno_api = requests.api.post(url, json=cliente)

        if retorno_api.status_code == 201:
            return redirect('cadastro-clientes')
        else:
            HttpResponse("erro cadastramento de cliente")

    return render(request, 'sistema/clientes.html', context)


def cadastro_proprietario(request):
    url = settings.URL_API + "proprietario/"
    todos_proprietarios = requests.api.get(url).json()

    context = {
        'proprietarios': todos_proprietarios
    }

    if request.method == "POST":
        proprietario = {}
        proprietario['nome'] = request.POST.get("nome")
        proprietario['cpf'] = request.POST.get("cpf")
        proprietario['rg'] = request.POST.get("rg")
        proprietario['cnpj'] = request.POST.get("cnpj")
        proprietario['endereco'] = request.POST.get("endereco")
        proprietario['bairro'] = request.POST.get("bairro")
        proprietario['cep'] = request.POST.get("cep")
        proprietario['cidade'] = request.POST.get("cidade")
        proprietario['uf'] = request.POST.get("uf")
        proprietario['email'] = request.POST.get("email")
        proprietario['telefone'] = request.POST.get("telefone")
        proprietario['pessoa_juridica'] = True if request.POST.get(
            "pj") == "pj_true" else False

        url = settings.URL_API + "proprietario/"
        retorno_api = requests.api.post(url, json=proprietario)

        if retorno_api.status_code == 201:
            return redirect('/cadastro/proprietarios')
        else:
            HttpResponse("erro cadastramento de cliente")

    return render(request, 'sistema/proprietarios.html', context)


def cadastro_corretores(request):
    url = settings.URL_API + "corretor/"
    todos_corretores = requests.api.get(url).json()

    context = {
        'corretores': todos_corretores
    }

    if request.method == "POST":
        corretor = {}
        corretor['nome'] = request.POST.get("nome")
        corretor['creci'] = request.POST.get("creci")
        corretor['rg'] = request.POST.get("rg")
        corretor['cpf'] = request.POST.get("cpf")
        corretor['endereco'] = request.POST.get("endereco")
        corretor['bairro'] = request.POST.get("bairro")
        corretor['cep'] = request.POST.get("cep")
        corretor['cidade'] = request.POST.get("cidade")
        corretor['uf'] = request.POST.get("uf")
        corretor['email'] = request.POST.get("email")
        corretor['telefone'] = request.POST.get("telefone")

        url = settings.URL_API + "corretor/"
        retorno_api = requests.api.post(url, json=corretor)

        if retorno_api.status_code == 201:
            return redirect('/cadastro/corretores')
        else:
            HttpResponse("erro cadastramento de corretores")

    return render(request, 'sistema/corretores.html', context)


def cadastro_imoveis(request):
    url = settings.URL_API + "imovel/"
    todos_imoveis = requests.api.get(url).json()
    url_proprietario = settings.URL_API + "proprietario/"
    todos_proprietarios = requests.api.get(url_proprietario).json()
    url_corretor = settings.URL_API + "corretor/"
    todos_corretores = requests.api.get(url_corretor).json()

    contexto = {
        'proprietarios': todos_proprietarios,
        'corretores': todos_corretores,
        'imoveis': todos_imoveis
    }

    if request.method == "POST":
        imovel = {}
        imovel_foto = {}
        imovel['descricao'] = request.POST.get('descricao')
        imovel['id_proprietario'] = request.POST.get('id_proprietario')
        imovel['id_corretor'] = request.POST.get('id_corretor')
        imovel['matricula'] = request.POST.get('matricula')
        imovel['qtd_comodo'] = request.POST.get('comodos')
        imovel['n_sabesp'] = request.POST.get('sabesp')
        imovel['n_eletropaulo'] = request.POST.get('eletropaulo')
        imovel['valor_aluguel'] = request.POST.get('valor_aluguel')
        imovel['valor_venda'] = request.POST.get('valor_venda')
        imovel['iptu'] = request.POST.get('iptu')
        imovel['metragem'] = request.POST.get('metro_quadrado')
        imovel['tipo_servico'] = request.POST.get('servico')
        imovel['status_imovel'] = request.POST.get('status')
        imovel['latitude'] = request.POST.get('latitude')
        imovel['longitude'] = request.POST.get('longitude')
        imovel['endereco'] = request.POST.get('endereco')
        imovel['bairro'] = request.POST.get('bairro')
        imovel['cep'] = request.POST.get('cep')
        imovel['cidade'] = request.POST.get('cidade')
        imovel['uf'] = request.POST.get('uf')
        imovel['imagem_1'] = request.POST.get('photo1')
        imovel['imagem_2'] = request.POST.get('photo2')
        imovel['imagem_3'] = request.POST.get('photo3')
        imovel['imagem_4'] = request.POST.get('photo4')
        imovel['imagem_5'] = request.POST.get('photo5')
        imovel['residencial'] = True if request.POST.get(
            "residencial") == "residencial_true" else False

        url = settings.URL_API + 'imovel/'
        retorno_api = requests.api.post(url, json=imovel)
        if retorno_api.status_code == 400:
            HttpResponse("erro cadastramento de imoveis")
        elif retorno_api.status_code == 201:
            return redirect('cadastro-imoveis')

    return render(request, 'sistema/imoveis.html', contexto)


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        contexto = {
            'name': request.POST.get('name', ''),
            'subject': subject,
            'from_email': from_email,
            'message': message
        }
        if subject and message and from_email:
            template_name = 'contatoEmail.html'
            send_mail_template(subject, template_name, contexto, from_email)
            context = {
                'title': 'SK imobiliaria',
                'email_msg': 'Enviado com sucesso'
            }
            return render(request, 'index.html', context)
        else:
            context = {
                'title': 'SK imobiliaria',
                'email_msg': 'Erro ao enviar email'
            }
            return render(request, 'index.html', context)


def contrato(request):
    contexto = {
        'contratos': Contrato.objects.all(),
        'imoveis': Imovel.objects.filter(status_imovel='DI'),
        'clientes': Cliente.objects.all(),
        'parcela': 0,
    }

    if request.POST:
        try:
            imovel = Imovel.objects.get(id=request.POST.get('id_imovel'))
            cliente = Cliente.objects.get(id=request.POST.get('id_cliente'))

            contrato_novo = Contrato.objects.create(
                id_imovel=imovel,
                id_cliente=cliente,
                tipo_servico=imovel.tipo_servico,
                periodo_contrato=request.POST.get('periodo'),
                observacao=request.POST.get('observacao')
            )
            contrato_novo.save()

            if imovel.tipo_servico == "AL":
                imovel.status_imovel = "AL"
                imovel.save()
            else:
                imovel.status_imovel = 'IN'
                imovel.save()

            id_contrato = contrato_novo.id
            periodo_contrato = int(contrato_novo.periodo_contrato)
            tipo_servico = contrato_novo.tipo_servico

            if tipo_servico == "AL":
                valor_total = (
                    contrato_novo.id_imovel.iptu/12 + contrato_novo.id_imovel.valor_aluguel)
            elif tipo_servico == "VE":
                valor_total = contrato_novo.id_imovel.valor_venda

            while periodo_contrato > 0:
                boleto = Boleto.objects.create(
                    contrato=Contrato.objects.get(id=id_contrato),
                    parcela=periodo_contrato,
                    valor_total=valor_total
                )
                boleto.save()
                periodo_contrato -= 1

            return redirect('contrato-view')
        except Exception as error:
            print(error)
            return redirect('contrato-view')

    return render(request, 'sistema/contrato.html', contexto)


def deletar_contrato(request, pk):
    contrato = Contrato.objects.get(id=pk)
    contrato.delete()

    return redirect('contrato-view')


def boleto(request):
    contexto = {
        'boletos': Boleto.objects.all(),
    }
    return render(request, 'sistema/boleto.html', contexto)


def alterar_boleto(request, pk):
    boleto = Boleto.objects.get(id=pk)
    if boleto.status == "AB":
        boleto.status = "PG"
        boleto.save()
    else:
        boleto.status = "AB"
        boleto.saver()

    return redirect('boleto-view')
