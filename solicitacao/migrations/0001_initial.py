# Generated by Django 4.2.15 on 2024-08-28 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoTransferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('obs', models.TextField(blank=True, null=True)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('entregue', models.BooleanField(default=False)),
                ('data_entrega', models.DateField(blank=True, null=True)),
                ('deposito_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_deposito_destino', to='cadastro.depositodestino')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_funcionario', to='cadastro.funcionario')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_itens', to='cadastro.itenstransferencia')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoRequisicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe_requisicao', models.CharField(choices=[('Req p Consumo', 'Consumo'), ('Req p Produção', 'Produção')], max_length=20)),
                ('quantidade', models.IntegerField()),
                ('obs', models.TextField(blank=True, null=True)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('entregue', models.BooleanField(default=False)),
                ('data_entrega', models.DateField(blank=True, null=True)),
                ('cc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicao_cc', to='cadastro.cc')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicao_funcionario', to='cadastro.funcionario')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicao_itens', to='cadastro.itenssolicitacao')),
            ],
        ),
    ]
