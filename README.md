
## BLO - Buduj, Licz, Oszczędzaj
Web application for creating cost estimates, managing
construction of e.g. a house, allows to count and control
construction costs

web version avaiable on: https://blo-dev.herokuapp.com/

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

The application code is written in English, but the web project itself is in Polish.

#### The project allows you to add an unlimited number of builds:
![](https://github.com/aemiks/blo/blob/main/static/assets/img/addbuild.png)

#### And for each construction site, the ability to add stages composed of any elements or services:
![](https://github.com/aemiks/blo/blob/main/static/assets/img/addstage.png)

![](https://github.com/aemiks/blo/blob/main/static/assets/img/addelement.png)

####  In addition, any of the elements or stages, can be edited or deleted at any time.
![](https://github.com/aemiks/blo/blob/main/static/assets/img/editelement.png)

#### The application in real time recalculates the current used budget of the entire construction, and the costs of individual stages.
![](https://github.com/aemiks/blo/blob/main/static/assets/img/budget.png)

## Technologies
Project is created with:
* ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)
* ![](https://img.shields.io/badge/django%20version-3.2.2-blue)

	
## Setup

Please download the appropriate environment and read the instructions for installing it
* [Python](https://www.python.org/downloads/)
* [Django](https://docs.djangoproject.com/en/3.2/topics/install/)

Install Git
* [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To clone respiratory from github:
```
$ git clone https://github.com/aemiks/blo.git

```
When the cloning is successful, and if you are in the project main folder:
```
$ pip install -r requirements.txt

```

Now try to launch the project:
```
$ python manage.py runserver

```

enjoy.
