from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Expert(models.Model):
	CHAPTER_CHOICES = (
		('Бизнес', 'Бизнес'), 
		('Право', 'Право'),
		('Творчество', 'Творчество'),
		('Волонтерство', 'Волонтерство'),
		('Наука', 'Наука'), 
	)


	expert_FIO = models.CharField('ФИО', max_length = 100)
	expert_company = models.CharField('Организация', max_length = 100)
	expert_direction = models.CharField('Направление', max_length = 100)
	expert_country = models.CharField('Страна', max_length = 60)
	expert_phone = models.CharField('Телефон', max_length = 30)
	expert_email = models.CharField('Почта', max_length = 30)
	expert_about = models.TextField('О себе')
	expert_photo = models.ImageField('Фото', upload_to='images/experts', blank=True)
	expert_chapter = models.CharField('Раздел', max_length=50, null = True, choices=CHAPTER_CHOICES)

	class Meta:
		verbose_name = 'Эксперт'
		verbose_name_plural = 'Эксперты'

def __str__(self):
 return f"{self.expert_FIO}"



class News(models.Model):

	CHAPTER_CHOICES = (
		('Бизнес', 'Бизнес'), 
		('Право', 'Право'),
		('Творчество', 'Творчество'),
		('Волонтерство', 'Волонтерство'),
		('Наука', 'Наука'), 
	)


	news_heading = models.CharField('Заголовок', max_length = 200)
	news_content = models.TextField('Содержание')
	news_photo = models.ImageField('Фото', upload_to='images/News', blank=True)

	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'

def __str__(self):
 return f"{self.news_heading}"


class ExpertsMean(models.Model):
	CHAPTER_CHOICES = (
		('Бизнес', 'Бизнес'), 
		('Право', 'Право'),
		('Творчество', 'Творчество'),
		('Волонтерство', 'Волонтерство'),
		('Наука', 'Наука'), 
	)

	expert_fio = models.ForeignKey('Expert', on_delete=models.PROTECT)
	mean_heading = models.CharField('Заголовок', max_length = 150)
	mean_content = models.TextField('Содержание')
	mean_photo = models.ImageField('Фото', upload_to='images/ExpertMean', blank=True)
	mean_video = models.FileField('Видео', upload_to='images/video')
	

	class Meta:
		verbose_name = 'Мнение эксперта'
		verbose_name_plural = 'Мнения экспертов'

def __str__(self):
 return f"{self.expert_fio}"



class State(models.Model):

	CHAPTER_CHOICES = (
		('Бизнес', 'Бизнес'), 
		('Право', 'Право'),
		('Творчество', 'Творчество'),
		('Волонтерство', 'Волонтерство'),
		('Наука', 'Наука'), 
	)


	state_chapter = models.CharField('Раздел', max_length=50, null = True, choices=CHAPTER_CHOICES)
	state_heading = models.CharField('Заголовок', max_length = 200)
	state_short_description = models.CharField('Краткое описание', max_length = 200)
	state_content = models.TextField('Содержание')
	state_photo = models.ImageField('Фото', upload_to='images/State', blank=True)

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

def __str__(self):
 return f"{self.news_heading}"



class ProjecPar(models.Model):

 		project_name = models.CharField('Наименование', max_length = 100, null = True)
 		project_photo = models.ImageField('Логотип', upload_to='images/Project', blank=True)
 		project_text = models.TextField('Содержание')

 		class Meta:
 			verbose_name = 'Проект'
 			verbose_name_plural = 'Проекты'

def __str__(self):
 return f"{self.project_name}"

