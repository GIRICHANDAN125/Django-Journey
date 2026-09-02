from django.urls import path,re_path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('details/', views.details),
    path('table/', views.table),
    path('marks/', views.marks),
    path('food/', views.food),
    path('studentdetails/', views.studentdetails),
    path('studentinfo/', views.studentinfo),
    path('studentdetails3/', views.studentdetails3),
    path('greeting/<str:name>/', views.greeting),
    path('addition/<int:num1>/<int:num2>/', views.addition),
    path('foodie/<str:foodvalue>/', views.foodie),
    path('calculator/<str:operation>/<int:num1>/<int:num2>/', views.calculator),
    # matches urls like customer/alice/ or /customer/bob  and here ited of a-zA-Z we can use \w for all spcase _ space and also char
re_path( r'^customer/(?P<customer_name>[a-zA-Z]+)/$',views.customer),

# matches urls like user/john/ or /user/jane
re_path(r'^user/(?P<username>[a-zA-Z]*)/$',views.user),

# matches URLs like item/123/
re_path(r'^item/(?P<item_name>\d+)/$',views.item),


re_path(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})$',views.archive),

# create a path 'menu/' use regex to pass two patameters category and subcategory  subcatgory is optiobal parameter 
# both can acceptdigits and alphabets and space
# example 
# c1: if you specigy subcatin url 
# localhost: 8000/menu/chinese/nodlrs 
# you have chosen catgory:chines
#  you hace chosen subcategory:nodels 

#  c1: if u do not specify subcatgory in url 
#  ou have chosen catgory:chines
#  you hace chosen subcategory:nnod specitef


    re_path(
        r'^menu/(?P<category>[a-zA-Z0-9 ]+)(?:/(?P<subcategory>[a-zA-Z0-9 ]+))?/$',
        views.menu
    ),


    
]