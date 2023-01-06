# Generated by Django 3.1.5 on 2021-07-05 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_auto_20210705_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='warning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('status', models.CharField(max_length=45)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warning_agent', to='Home.agent')),
            ],
        ),
    ]