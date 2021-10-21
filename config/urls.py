"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from rest_framework_jwt.views import obtain_jwt_token
from apps.products.urls import routes as products_routes
from apps.users.urls import routes as users_routes
from rest_framework.routers import DefaultRouter

api_routes=[]
api_routes.append(products_routes)
api_routes.append(users_routes)

router  =   DefaultRouter()

for routes in api_routes:
    for r in routes:
        router.register(r[0],r[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('token/', obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += [
        *static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT),
    ]