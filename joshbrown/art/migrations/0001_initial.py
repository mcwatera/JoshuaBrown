# Generated by Django 3.0.3 on 2020-02-14 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coll_title', models.CharField(max_length=300)),
                ('coll_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Collection')),
            ],
        ),
    ]
