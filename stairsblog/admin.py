from django.contrib import admin
from .models import Post 

#---- admin evolue ---

#nous creons une nouvelle classe pour chaque modele (ici Post).
#Notre classe heritere de admin.ModelAdmin et a principalement 5 attributs
class PostAdmin(admin.ModelAdmin):
   list_display   = ('title', 'author', 'created_date', 'published_date')
   list_filter    = ('author','title',)
   date_hierarchy = 'created_date'
   ordering       = ('published_date',)
   search_fields  = ('title', 'text')

#---- admin evolue ---


admin.site.register(Post, PostAdmin)
#DjangoAdmin prendra en compte les regles qui ont ete specifiees dans la classe PostAdmin

