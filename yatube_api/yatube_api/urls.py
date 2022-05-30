from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

# Создаётся роутер
router = routers.DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
