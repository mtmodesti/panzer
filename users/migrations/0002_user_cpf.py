# Generated by Django 4.0.6 on 2022-07-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
