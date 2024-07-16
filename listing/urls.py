from django.urls import path, include
from .views import get_wishlist, listing, add_prop, detail, addPics, index,del_wishlist, add_wishlist, contact_prop, get_contacts, mark_done
urlpatterns = [
    path('listing/', listing, name='listing'),
    path('add/', add_prop, name='add'),
    path('', index, name='add'),
    path('details/<uuid:prop_id>', detail, name='detail'),
    path('add_pics/<uuid:prop_id>', addPics, name='addImages'),
    path('wishlist', add_wishlist, name='wishlist'),
    path('del_wishlist', del_wishlist, name="del_wishlist"),
    path('get_wishlist', get_wishlist, name="get_wishlist"),
    path('contact', contact_prop, name='contact'),
    path('viewcontact', get_contacts, name='getcontact'),
    path('mark_done', mark_done, name='mark_done'),
]
