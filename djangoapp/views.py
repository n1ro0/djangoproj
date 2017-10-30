from django.shortcuts import render
from django.views import generic

from djangoapp import tasks
from . import forms
from . import models


#Book model------------------------------------------------------
class BookListView(generic.ListView):
    template_name = 'books.html'
    model = models.Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    template_name = 'book.html'
    model = models.Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['book'] = models.Book.objects.filter(id = self.kwargs['pk']).first()
        context['comments'] = models.Comment.objects.filter(book_id = self.kwargs['pk'])
        return context


class BookCreateView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_success_url(self):
        return self.success_url


class BookUpdateView(generic.UpdateView):
    template_name = 'create_book.html'
    model = models.Book
    form_class = forms.BookForm
    success_url = '/books/'

    def get_success_url(self):
        pk = self.kwargs['pk']
        tasks.create_preview(pk)
        return self.success_url


class BookDeleteView(generic.DeleteView):
    template_name = 'delete_conformation.html'
    success_message = "Deleted Successfully"
    model = models.Book
    success_url = '/books/'


#Category model------------------------------------------------------
class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = models.Category
    context_object_name = 'categories'


class CategoryDetailView(generic.ListView):
    template_name = 'category.html'
    model = models.Category
    context_object_name = 'category'


class CategoryCreateView(generic.CreateView):
    template_name = 'create_category.html'
    form_class = forms.CategoryForm
    success_url = "/categories/"


class CategoryUpdateView(generic.UpdateView):
    template_name = 'create_category.html'
    model = models.Category
    form_class = forms.CategoryForm
    success_url = '/books/'


class CategoryDeleteView(generic.DeleteView):
    template_name = 'delete_conformation.html'
    success_message = "Deleted Successfully"
    model = models.Category
    success_url = '/categories/'



#Author model------------------------------------------------------
class AuthorListView(generic.ListView):
    template_name = 'authors.html'
    model = models.Author
    context_object_name = 'authors'


class AuthorUpdateView(generic.UpdateView):
    template_name = 'base_create.html'
    model = models.Author
    form_class = forms.AuthorForm
    success_url = '/authors/'


#Comment model-------------------------------------------------------------
class CommentCreateView(generic.CreateView):
    template_name = 'base_create.html'
    form_class = forms.CommentForm
    success_url = "/books/"


def index(request):
    return render(request, "index.html")


def categories(request):
    categories = models.Category.objects.all()
    return render(request, "categories.html", context={"categories": categories})


def authors(request):
    authors = models.Author.objects.all()
    return render(request, "authors.html", context={"authors": authors})


def books(request):
    books = models.Book.objects.all()
    return render(request, "books.html", context={"books": books})

def create_book(request):
    #if request.method == "POST":
        #models.Book.objects.create(title=request.POST["title"], year=int(request.POST["year"]),
            #                           description=request.POST["description"], category_id=int(request.POST["category_id"]),
        #       picture=request.FILES["picture"])
        #return books(request)
    if request.method == "GET":
        return render(request, "create_book.html")

def create_cat(request):
    if request.method == "POST":
        models.Category.objects.create(title=request.POST["title"])
        return categories(request)
    if request.method == "GET":
        return render(request, "create_category.html")