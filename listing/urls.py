from django.urls import path, include
from .views import get_wishlist, listing, add_prop, detail, addPics, index,del_wishlist, add_wishlist
urlpatterns = [
    path('listing/', listing, name='listing'),
    path('add/', add_prop, name='add'),
    path('', index, name='add'),
    path('details/<uuid:prop_id>', detail, name='detail'),
    path('add_pics/<uuid:prop_id>', addPics, name='addImages'),
    path('wishlist', add_wishlist, name='wishlist'),
    path('del_wishlist', del_wishlist, name="del_wishlist"),
    path('get_wishlist', get_wishlist, name="get_wishlist")
]
