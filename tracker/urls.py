"""tracker URL Configuration

The `urlpatterns` list routes URLs to user_view. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function user_view
    1. Add an import:  from my_app import user_view
    2. Add a URL to urlpatterns:  path('', user_view.home, name='home')
Class-based user_view
    1. Add an import:  from other_app.user_view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]
