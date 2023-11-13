from django.contrib import admin
from app.models import User,Product,Cart,Order
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)

