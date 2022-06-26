from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.cache import cache_page


router = routers.DefaultRouter()
router.register(r'news', NewsViewset, basename='news')
router.register(r'articles', ArticlesViewset, basename='//articles')


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('i18n/', include('django.conf.urls.i18n')),
    path('index', index),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('news/create/', PostCreateNews.as_view(), name='news_create'),
    path('articles/create/', PostCreateArticle.as_view(), name='articles_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('user/<int:pk>/edit/', ProfileUpdate.as_view(), name='user_edit'),
    path('user/<int:pk>/', ProfileDetail.as_view(), name='user_profile'),
    path('upgrade/', get_author, name='upgrade'),
    path('subscribe/<int:pk>/', get_subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>/', del_subscribe, name='unsubscribe'),
    path('categorys/', CategoryList.as_view(), name='category_list'),
    path('user/', set_timezone, name='set_timezone'),
    path('api/v1/', include(router.urls), name='api'),
    path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
