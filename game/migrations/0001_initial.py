# Generated by Django 2.2.4 on 2019-08-15 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_nbr', models.AutoField(primary_key=True, serialize=False)),
                ('next_dialog', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
                ('action_result', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Narration',
            fields=[
                ('narration', models.AutoField(primary_key=True, serialize=False)),
                ('friendly_name', models.CharField(blank=True, max_length=300)),
                ('text', models.CharField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('dialogue', models.AutoField(primary_key=True, serialize=False)),
                ('access_lvl', models.IntegerField(default=0)),
                ('friendly_name', models.CharField(max_length=200)),
                ('answer_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Answer')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Character')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Location')),
                ('narration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Narration')),
            ],
        ),
    ]
