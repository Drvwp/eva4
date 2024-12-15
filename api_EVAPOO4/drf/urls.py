from django.urls import path
from API.views import get_items, create_item, update_item, delete_item

urlpatterns = [
    path('get_items/', get_items, name='get_items'),
    path('create_item/', create_item, name='create_item'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
]
