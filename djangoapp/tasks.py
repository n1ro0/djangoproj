from celery import shared_task
from . import models
from django.shortcuts import get_object_or_404



@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@shared_task
def create_preview(book_id):
    book = get_object_or_404(models.Book, id=book_id)
    book.preview = book.picture
    book.save()



@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)