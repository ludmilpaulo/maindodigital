from django.contrib import admin

from .models import Carousel, AboutUs , Why_Choose_Us , Chef, Contact, Post, Document

admin.site.register(Carousel)
admin.site.register(AboutUs)
admin.site.register(Why_Choose_Us)
admin.site.register(Chef)

admin.site.register(Post)

admin.site.register(Contact)

admin.site.register(Document)