from django.urls import path
from main.views import show_main, show_json, show_json_byId, show_xml, show_xml_byId, add_product, show_product, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name = 'show_xml'),
    path('json/', show_json, name = 'show_json'),
    path('xml/<str:productId>/', show_xml_byId, name = 'show_xml_byId'),
    path('json/<str:productId>/', show_json_byId, name = 'show_json_byId'),
    path('add-product/', add_product, name = 'add_product'),
    path('product/<str:productId>/', show_product, name = 'show_product'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name='logout')
]