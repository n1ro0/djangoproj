"""second_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from djangoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^categories/$', views.CategoryListView.as_view(), name="CategoryListView"),
    url(r'^books/$', views.BookListView.as_view(), name="BookListView"),
    url(r'^books/detail/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name="BookDetailView"),
    url(r'^books/(?P<pk>\d+)/$', views.BookUpdateView.as_view(), name="BookUpdateView"),
    url(r'^books/delete/(?P<pk>\d+)/$', views.BookDeleteView.as_view(), name="BookDeleteView"),
    url(r'^books/create/$', views.BookCreateView.as_view(), name="create_book"),
    url(r'^authors/$', views.AuthorListView.as_view(), name="AuthorListView"),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorUpdateView.as_view(), name="AuthorUpdateView"),
    url(r'^categories/create/$', views.CategoryCreateView.as_view(), name="create_category"),
    url(r'^comments/create/$', views.CategoryCreateView.as_view(), name="create_comment")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

