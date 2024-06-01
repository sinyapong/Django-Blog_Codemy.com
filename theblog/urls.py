from django.urls import path
from . import views
from .views import Homeview,ArticleDetailView,AddPostview,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Homeview.as_view(),name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(),name="article-detail"),
    path('add_post/', AddPostview.as_view(),name="add_post"),
    path('add_category/', AddCategoryView.as_view(),name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
]