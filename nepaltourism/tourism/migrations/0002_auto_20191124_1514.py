# Generated by Django 2.2.3 on 2019-11-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='locationimages')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='toppicture',
            name='image',
            field=models.ImageField(upload_to='topimages'),
        ),
    ]
