"""
URL configuration for bissextile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from bissextile.views import is_leap_year, leap_years_in_range , call_history


urlpatterns = [
    path('is_leap_year/<str:year>/', is_leap_year),
    path('leap_years_in_range/<str:start_year>/<str:end_year>/', leap_years_in_range),
    path('history/', call_history),
]

