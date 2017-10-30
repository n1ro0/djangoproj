from celery import shared_task
from djangoapp import models
from django.shortcuts import get_object_or_404
from PIL import Image, ImageFile
from django.conf import settings
import os
import random



@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@shared_task
def create_preview(book_id):
    book = get_object_or_404(models.Book, id=book_id)
    book.preview = book.picture
    image_hold = Image.open(book.picture.path)
    filename = 'preview' + os.path.basename(book.picture.path)
    image = image_hold.resize((300, 300), Image.ANTIALIAS)

    temp_loc = "%s/tmp" % (settings.MEDIA_ROOT)

    if not os.path.exists(temp_loc):
        os.makedirs(temp_loc)

    temp_file_path = os.path.join(temp_loc, filename)


    temp_image = open(temp_file_path, "wb")

    image.save(temp_image, quality=80)

    temp_data = open(temp_file_path, "rb")

    #image_file = File(temp_data)
    book.preview.save(filename, temp_data)
    book.save()



@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)