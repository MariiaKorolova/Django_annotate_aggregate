from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
    path('book/create', views.BookCreateView.as_view(), name='book.create'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name='bookupdated'),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name='book.delete'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>', views.author, name='author'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>', views.publisher, name='publisher'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/<int:pk>', views.store, name='store'),

]