from django.contrib import admin
from .models import Client,Product,Order



@admin.action(description="Update Descr")
def update_descr(modeladmin, request, queryset):
    queryset.filter(price__gte=1000).update(description="Too expensive")

"""Обновляет описание продуктов именами клиентовю, которые их покупали"""
@admin.action(description="Update Descr with clients")
def update_descr_by_client(modeladmin, request, queryset):
    # orders = Order.objects.filter(products__id = queryset[0].id)
    # print(orders)

    clients = Client.objects.filter(order__products__id=queryset[0].id)
    queryset.update(description=f'{[client for client in clients]}'.replace('[<Client: ','').replace('>, <Client: ',', ').replace('>]',''))

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'registered_date')
    list_per_page = 5
    search_fields = ['name']
    fieldsets = [
        (
            'Имя',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email','phone','address'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дата регистрации',
                'fields': ['registered_date'],
            }
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'quantity', 'added_date','link_photo')
    list_per_page = 5
    search_fields = ['product_name']
    actions = [update_descr_by_client]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_cost', 'date_ordered')
    list_per_page = 5