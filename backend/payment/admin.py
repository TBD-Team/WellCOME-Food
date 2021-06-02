from django.contrib import admin


from .models import Account, GRU, Credit, Purchase

admin.site.register(Account)
admin.site.register(GRU)
admin.site.register(Credit)
admin.site.register(Purchase)
