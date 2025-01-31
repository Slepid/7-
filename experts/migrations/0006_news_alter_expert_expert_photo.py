# Generated by Django 5.0.6 on 2024-08-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0005_alter_expert_expert_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_chapter', models.CharField(max_length=50, verbose_name='Раздел')),
                ('news_heading', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('news_short_description', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('news_content', models.TextField(verbose_name='Содержание')),
                ('news_photo', models.ImageField(blank=True, upload_to='images/News', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterField(
            model_name='expert',
            name='expert_photo',
            field=models.ImageField(blank=True, upload_to='images/experts', verbose_name='Фото'),
        ),
    ]
