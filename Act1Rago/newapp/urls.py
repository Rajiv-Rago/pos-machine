from django.urls import path
from . import views


urlpatterns = [
   path('', views.openpos, name = "openpos"),
   path('item_list/', views.item_list, name = "item_list"),
   path('add_item/', views.add_item, name="add_item"),
   path('edit_item/<int:pk>', views.edit_item, name="edit_item"),
   path('confirm_order', views.confirm_order, name="confirm_order"),
]
