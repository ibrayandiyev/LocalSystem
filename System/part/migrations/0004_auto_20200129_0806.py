# Generated by Django 2.1.5 on 2020-01-29 05:06

import System.part.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0003_supplier_vat_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repeats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=System.part.models.invoice_file)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('period', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.Category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.Company')),
                ('iva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.IVA')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.Supplier')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='spenses',
            name='repeat_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]