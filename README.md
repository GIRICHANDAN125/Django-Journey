# Django Learning Journey

This repository contains my Django classwork and practice project. This README
records what I have learned day by day and the features currently implemented
in `myapp`.

## Day 01 - Django Basics and Views

### What I learned

- Created a Django project and a Django app.
- Connected app URLs to project URLs with `include()`.
- Created function-based views.
- Returned text and HTML using `HttpResponse`.
- Used variables, strings, lists, dictionaries, loops, and conditions in views.
- Generated a multiplication table and student tables from Python data.
- Used conditional logic to display marks and grades.

### Practice URLs

```text
/welcome/
/details/
/table/
/marks/
/food/
/studentdetails/
/studentinfo/
/studentdetails3/
```

## Day 02 - Dynamic URLs and Calculations

### What I learned

- Passed values through URLs with Django converters.
- Used `<str:name>` for text values.
- Used `<int:num1>` and `<int:num2>` for numbers.
- Built a greeting view and an addition view.
- Created a food lookup view using a dictionary.
- Handled unavailable food items with an error message.
- Built one calculator view for addition, subtraction, multiplication, and division.
- Added division-by-zero and invalid-operation handling.

### Practice URLs

```text
/greeting/<name>/
/addition/<num1>/<num2>/
/foodie/<foodvalue>/
/calculator/<operation>/<num1>/<num2>/
```

## Day 03 - Regular Expression URLs

### What I learned

- Used `re_path()` for more specific URL patterns.
- Created named regular-expression parameters.
- Matched letters with `[a-zA-Z]+`.
- Matched numbers with `\d+`.
- Matched fixed-length date values for year, month, and day.
- Created an optional URL parameter for a menu subcategory.
- Added a custom error page route.
- Practiced debugging URL and view errors.

### Practice URLs

```text
/customer/<customer_name>/
/user/<username>/
/item/<item_name>/
/archive/<year>/<month>/<day>/
/menu/<category>/
/menu/<category>/<subcategory>/
/error/
```

## Day 04 - Templates and Context Data

### What I learned

- Rendered HTML files with Django's `render()` function.
- Passed data from a view to a template through a context dictionary.
- Displayed context values with `{{ variable }}`.
- Used `{% for %}` loops to display lists of food and products.
- Used `{% if %}` conditions in templates.
- Created reusable food data in a Python helper function.
- Built menu pages from a list of dictionaries.

### Practice URLs

```text
/test_template/
/menu_template/
/menu1/<item_name>/
```

## Day 05 - Static Files, Product Pages, and Template Inheritance

### What I learned

- Loaded static files with `{% load static %}` and `{% static %}`.
- Displayed product images from the static folder.
- Created a product-list page with name, brand, price, and image data.
- Created a shopping-list page with links to product details.
- Used named URLs with `{% url %}`.
- Passed a selected product through a dynamic URL.
- Used `next()` to find one item in a list.
- Displayed a fallback message when a product is not found.
- Created a shared `base.html` layout.
- Reused common navigation with `{% include 'header.html' %}`.
- Used `{% extends %}` and `{% block %}` for template inheritance.
- Created Home, About, and Food pages.
- Practiced HTML and CSS styling in templates and `style.css`.

### Practice URLs

```text
/testimg/
/products/
/shoppinglist/
/shoppingdetails/<shoppingitem>/
/home/
/about/
/food/
/htmlcss/
```

## Current Project Structure

```text
myproject/
|-- manage.py
|-- db.sqlite3
|-- myproject/
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- asgi.py
|   `-- wsgi.py
`-- myapp/
    |-- urls.py
    |-- views.py
    |-- models.py
    |-- templates/
    |-- static/
    `-- migrations/
```

## Django Concepts Practiced So Far

- Project and app creation
- URL routing with `path()` and `re_path()`
- Function-based views
- `HttpResponse` and `render()`
- URL parameters and named URLs
- Template variables, loops, conditions, includes, and inheritance
- Static files and images
- Lists and dictionaries as temporary view data
- Basic error handling
- SQLite database configuration

## Next Learning Goals

- Create models in `models.py`.
- Run migrations and save data in the database.
- Use the Django admin panel.
- Replace hard-coded product data with database queries.
- Add forms and user input.
- Improve validation and error handling.
- Add tests for views and URLs.