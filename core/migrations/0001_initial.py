# Generated by Django 2.2.1 on 2019-06-07 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30)),
                ('telefone', models.CharField(blank=True, max_length=30)),
                ('tipo_servico', models.CharField(blank=True, choices=[('VE', 'Venda'), ('AL', 'Alugel'), ('VA', 'Venda e Aluguel')], default='VA', max_length=2)),
                ('finalidade', models.CharField(blank=True, choices=[('RE', 'Residencial'), ('CO', 'Comercial')], default='RE', max_length=2)),
                ('endereco', models.CharField(blank=True, max_length=100)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=50)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('metro', models.CharField(blank=True, max_length=50)),
                ('valor_aluguel', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('qtd_comodo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('rg', models.CharField(max_length=30, unique=True)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('uf', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('pessoa_juridica', models.BooleanField(default=False)),
                ('inquilino', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=30)),
                ('mensagem', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('rg', models.CharField(max_length=30, unique=True)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('uf', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('creci', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'corretor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('rg', models.CharField(max_length=30, unique=True)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('uf', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('pessoa_juridica', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'proprietario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30)),
                ('residencial', models.BooleanField(default=False)),
                ('qtd_comodo', models.IntegerField(blank=True, null=True)),
                ('n_sabesp', models.CharField(max_length=30)),
                ('n_eletropaulo', models.CharField(max_length=30)),
                ('valor_aluguel', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('valor_venda', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('iptu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metragem', models.IntegerField()),
                ('tipo_servico', models.CharField(choices=[('VE', 'Venda'), ('AL', 'Alugel'), ('VA', 'Venda e Aluguel')], default='VA', max_length=2)),
                ('status_imovel', models.CharField(choices=[('AL', 'Alugado'), ('DI', 'Disponivel'), ('IN', 'Indisponivel')], default='DI', max_length=2)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('descricao', models.TextField()),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('uf', models.CharField(max_length=100)),
                ('imagem_1', models.CharField(blank=True, max_length=100, null=True)),
                ('imagem_2', models.CharField(blank=True, max_length=100, null=True)),
                ('imagem_3', models.CharField(blank=True, max_length=100, null=True)),
                ('imagem_4', models.CharField(blank=True, max_length=100, null=True)),
                ('imagem_5', models.CharField(blank=True, max_length=100, null=True)),
                ('id_corretor', models.ForeignKey(blank=True, db_column='id_corretor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Corretor')),
                ('id_proprietario', models.ForeignKey(db_column='id_proprietario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Proprietario')),
            ],
            options={
                'db_table': 'imovel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servico', models.CharField(choices=[('VE', 'Venda'), ('AL', 'Alugel'), ('VA', 'Venda e Aluguel')], default='VA', max_length=2)),
                ('periodo_contrato', models.IntegerField(db_column='periodo_contrato')),
                ('observacao', models.CharField(blank=True, max_length=200, null=True)),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Cliente')),
                ('id_imovel', models.ForeignKey(db_column='id_imovel', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcela', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.CharField(choices=[('PG', 'PAGO'), ('AB', 'EM ABERTO')], default='AB', max_length=2)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Contrato')),
            ],
            options={
                'db_table': 'boleto',
                'managed': True,
            },
        ),
    ]
