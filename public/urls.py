"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 28 November, 2017 @ 12:03 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from django.urls import path

from public import apps, views

app_name = apps.PublicConfig.name

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('about/', views.about, name='about'),
]
