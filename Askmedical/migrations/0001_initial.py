# Generated by Django 2.2.5 on 2021-06-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('abstract', models.TextField(null=True)),
                ('PM_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField()),
                ('sentence', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Askmedical.Article')),
            ],
        ),
    ]
