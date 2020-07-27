from django.contrib import admin

# Register your models here.


from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    fieldsets = (
        (('message'), {
            # 'classes': ('collapse',),
            'fields': (('first_name', 'last_name',), ('email', 'phone'), ('message', ),
            ), 
        }),
    )
    list_display = ['first_name', 'last_name', 'email', 'created']
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'message')
    list_filter = ['first_name', 'last_name', 'created', ]

admin.site.register(Contact, ContactAdmin)


