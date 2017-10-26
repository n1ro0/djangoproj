from django.contrib import admin
from . import models


admin.site.register((models.Author, models.Category, models.Book, models.Comment))
