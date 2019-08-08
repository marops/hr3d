"""hr3d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('issues/', include('issues.urls')),
    path('sensors/',include('sensors.urls')),
    path('doc/',include('documents.urls')),
    path('eng/',include('support.urls')),
    path('admin/', admin.site.urls),
    #path('change_password',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',form_class=auth_forms.AdminPasswordChangeForm, success_url='/accounts/password_change/done/')),
    path('signup/',views.signup, name='signup'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('cms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
