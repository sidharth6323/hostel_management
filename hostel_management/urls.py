"""hostel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib import admin
from views import profile, logout, edit_form, mess_bill, hostel_fee_paid, dataset_export,dataset_export_query, signup,student, delete_student
from django.contrib.auth.decorators import user_passes_test

#login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', login,{'template_name': 'index.html'}),
    url(r'^profile/$',profile),
    url(r'^logout/$', logout),
    url(r'^profile/(.+)/$',edit_form),
    url(r'^mess_bill/$',mess_bill),
    url(r'^hostel_fee/$',hostel_fee_paid),
    url(r'^export/$',dataset_export),
    url(r'^export/(.+)/$',dataset_export_query),
    url(r'^signup/$',signup),
    url(r'^student/$',student),
    url(r'^delete/(.+)/$',delete_student),
    

]