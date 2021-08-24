from django.db import models
from django.contrib.auth.models import User

class MyBuildDescription(models.Model):

    COUNTRY = (
        ('Polska','Polska'),
    )

    PROVINCE = (
        ('Dolnośląskie', 'Dolnośląskie'),
        ('Kujawsko-Pomorskie', 'Kujawsko-Pomorskie'),
        ('Lubelskie', 'Lubelskie'),
        ('Lubuskie', 'Lubuskie'),
        ('Łódzkie', 'Łódzkie'),
        ('Małopolskie', 'Małopolskie'),
        ('Mazowieckie', 'Mazowieckie'),
        ('Opolskie', 'Opolskie'),
        ('Podkarpackie', 'Podkarpackie'),
        ('Podlaskie', 'Podlaskie'),
        ('Pomorskie', 'Pomorskie'),
        ('Śląskie', 'Śląskie'),
        ('Świętokrzyskie', 'Świętokrzyskie'),
        ('Warmińsko-Mazurskie', 'Warmińsko-Mazurskie'),
        ('Wielkopolskie', 'Wielkopolskie'),
        ('Zachodniopomorskie', 'Zachodniopomorskie'),
    )

    TYPE = (
        ('Budynek Jednorodzinny', 'Budynek Jednorodzinny'),
        ('Budynek Wielorodzinny', 'Budynek Wielorodzinny'),
        ('Garaż', 'Garaż'),
        ('Inny', 'Inny'),
    )

    type = models.CharField(max_length=50, choices=TYPE)
    province = models.CharField(max_length=20, choices=PROVINCE)
    descriptions = models.TextField(blank=True)
    country = models.CharField(max_length=15, choices=COUNTRY, default='Polska')
    location = models.CharField('Miasto', max_length=30, blank=True)

class MyBuild(models.Model):
    name = models.CharField('Nazwa Budowy', max_length=100, blank=False)
    image = models.ImageField('Poglądowe zdjęcie budowy', upload_to='%Y/%m%d', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.OneToOneField(MyBuildDescription, on_delete=models.CASCADE, blank=True, null=True)
    budget = models.IntegerField('Zakładany koszt budowy', default=0, blank=True, null=True)
    build_cost = models.IntegerField('Rzeczywisty koszt budowy', default=0, blank=True, null=True)
    budget_calculation = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

