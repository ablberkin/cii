"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.urls import url, include
from django.urls import path, include

from rest_framework import routers
import blogapp.views
import img.views
import newsindex.views
import users.views
import emailValidate.views
from django.conf import settings
from django.conf.urls.static import  static
# from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'blog', blogapp.views.BlogViewSet)
router.register(r'newsindex', newsindex.views.newsindexViewSet)
router.register(r'users', users.views.UsersViewSet)
router.register(r'emailValidate', emailValidate.views.EmailViewSet)
router.register(r'img', img.views.ImgViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path(r'userSearch', users.views.userSearch, name='home'),
    # path(r'getList', users.views.getlist),
    path('sendEmail/', emailValidate.views.sendEmail),
    path('sendEmail/emailvalidSearch', emailValidate.views.emailvalidSearch),
    # path('send_message/', emailValidate.views.send_message),
    # path('register_email/', emailValidate.views.register_email),
    # path('send_message/', mailValidate.views.send_message)
    # path(r'email/vary/', users.views.emailvaryView.as_view())
    # path('api-token-auth/', views.obtain_auth_token),
    # path('jwt-auth/', obtain_jwt_token ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
