# Generated by Django 2.0 on 2017-12-15 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=250)),
                ('Text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ArticlesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=30)),
                ('CreateDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='ArticleCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArticleBank.ArticlesCategory'),
        ),
    ]