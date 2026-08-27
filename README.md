# Django Journey 🚀

My Django classwork and learning journey.

## Day 01 – Django Basics

### Topics Covered

- Django project and app setup
- Django views
- `HttpResponse`
- URL routing using `path()`
- Static URL paths
- Dynamic URL parameters
- `<str>` URL converter
- `<int>` URL converter
- Multiple URL parameters
- Calculator using Django views
- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Regular expressions using `re_path()`
- Named regex parameters
- Customer URL
- User URL
- Item URL
- Archive URL with year, month and day
- Optional URL parameter
- Menu URL with optional subcategory
- Regex for letters and numbers
- Debugging Django URL and view errors

### URLs Practiced

```python
path('welcome/', views.welcome)
path('details/', views.details)
path('table/', views.table)
path('marks/', views.marks)
path('food/', views.food)
path('studentdetails/', views.studentdetails)
path('studentinfo/', views.studentinfo)
path('studentdetails3/', views.studentdetails3)

path('greeting/<str:name>/', views.greeting)
path('addition/<int:num1>/<int:num2>/', views.addition)
path('foodie/<str:foodvalue>/', views.foodie)

path(
    'calculator/<str:operation>/<int:num1>/<int:num2>/',
    views.calculator
)

re_path(
    r'^customer/(?P<customer_name>[a-zA-Z]+)/$',
    views.customer
)

re_path(
    r'^user/(?P<username>[a-zA-Z]*)/$',
    views.user
)

re_path(
    r'^item/(?P<item_name>\d+)/$',
    views.item
)

re_path(
    r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
    views.archive
)

re_path(
    r'^menu/(?P<category>[a-zA-Z0-9 ]+)(?:/(?P<subcategory>[a-zA-Z0-9 ]+))?/$',
    views.menu
)