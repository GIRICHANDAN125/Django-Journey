from django.shortcuts import render
from django.http import HttpResponse



def welcome(request):
    return HttpResponse("welcome user myapp")

def details(request):
    name = "navneet"
    program = "btech cse"
    return HttpResponse(
        "the name of the student is " + name + " and the program is " + program
    )


def table(request):
    number =5
    table = "<h1> table of 5</h1>"
    for i in range(1, 11):
        table += f"{number} x {i} = {number * i}<br>"
    return HttpResponse(table)


def marks(request):
    mark = 85

    if 80 < mark <= 100:
        return HttpResponse('<h1 style="color: green;">Grade A</h1>')

    elif 60 < mark <= 80:
        return HttpResponse('<h1 style="color: blue;">Grade B</h1>')

    elif 40 < mark <= 60:
        return HttpResponse('<h1 style="color: orange;">Grade C</h1>')

    else:
        return HttpResponse('<h1 style="color: red;">Grade D</h1>')



def food(request):
    food_items = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
    itemcontain = "<h1>the food items available are: </h1>"
    for item in food_items:
        itemcontain += f"<p>{item}</p>"
    return HttpResponse(itemcontain)


def studentdetails(request):
    student = [
        ["navneet", 67],
        ["sachin", 89],
        ["rahul", 45],
        ["rohit", 78],
        ["virat", 90],
    ]

    content = """<table border="1">
    <tr>
        <th>name</th>
        <th>marks</th>
    </tr>
    """

    for i in student:
        content += f"""
        <tr>
            <td>{i[0]}</td>
            <td>{i[1]}</td>
        </tr>
        """

    content += "</table>"

    return HttpResponse(content)




def studentinfo(request):
    student =[
        {"Name": "navneet", "Marks": 67, "Course": "Django"},
        {"Name": "sachin", "Marks": 89, "Course": "Python"},
        {"Name": "rahul", "Marks": 45, "Course": "Java"},
        {"Name": "rohit", "Marks": 78, "Course": "C++"},
        {"Name": "virat", "Marks": 90, "Course": "JavaScript"},
    ]
    content = """<table border="1">
    <tr>
        <th>Name</th>
        <th>Marks</th>
        <th>Course</th>
    </tr>
    """
    for i in student:
        content += f"""
        <tr>
            <td>{i['Name']}</td>
            <td>{i['Marks']}</td>
            <td>{i['Course']}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)



def studentdetails3(request):
    studentinfo = {
        "anuj":{"marks": 67, "course": "Django"},
        "sachin":{"marks": 89, "course": "dsa"}, 
        "rahul":{"marks": 45, "course": "Java"},
        "rohit":{"marks": 78, "course": "C++"},
        "virat":{"marks": 90, "course": "dbms"}
    }

    content = """<table border="1">
    <tr>
        <th>Name</th>
        <th>Marks</th>
        <th>Course</th>
    </tr>
    """
    for name, details in studentinfo.items():
        content += f"""<tr>
            <td>{name}</td>
            <td>{details['marks']}</td>
            <td>{details['course']}</td>
        </tr>"""
    content += "</table>"
    return HttpResponse(content)









# dynamic url


def greeting(request, name):
    return HttpResponse(f"Hello, {name}!")







def addition(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f"The result of {num1} and {num2} is: {result}")




def foodie(request,foodvalue):
    fooditems = {
        "Pizza":"Size is reqular and price is 200",
        "Burger":"Size is large and price is 150",
        "icecream":"Size is small and price is 50",
    }
    if not foodvalue in fooditems:
        return HttpResponse(
            f"<p style='color:red;'>Sorry, we don't have {foodvalue} available.</p>"
        )
    return HttpResponse(f"<p>the {foodvalue} is available and {fooditems[foodvalue]}</p>")


    
def mart(request, item):
    item =request.GET.get('item', None)
    return  HttpResponse(f"<h1>the item is {item}</h1>")


# create your views  for prerfomanece basix calculation add subtract multiply divide and also create a view for area of circle and area of rectangle and area of triangle

def calculator(request, operation, num1, num2):

    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return HttpResponse(
                "<h1 style='color:red;'>Error: Division by zero is not allowed.</h1>"
            )

    else:
        return HttpResponse(
            "<h1 style='color:red;'>Error: Invalid operation.</h1>"
        )

    return HttpResponse(
        f"<h1>The result of {operation} between {num1} and {num2} is: {result}</h1>"
    )







# rematch code




def customer(request, customer_name):
    return HttpResponse(f"<h1>Welcome, {customer_name}!</h1>")

def user(request, username):
    return HttpResponse(f"<h1>Hello, {username}!</h1>")

def item(request, item_name):
    return HttpResponse(f"<h1>The item is: {item_name}</h1>")


def archive(request, year, month, day):
    return HttpResponse(
        f"<h1>Archive for {year}-{month}-{day}</h1>"
    )




def menu(request, category, subcategory=None):

    if subcategory:
        return HttpResponse(
            f"<h1>You have chosen category: {category}</h1>"
            f"<h1>You have chosen subcategory: {subcategory}</h1>"
        )

    return HttpResponse(
        f"<h1>You have chosen category: {category}</h1>"
        f"<h1>You have chosen subcategory: Not specified</h1>"
    )


def error(request):
    return HttpResponse("<h1 style='color:red;'>Error Page</h1>")


def test_template(request):
    data = {'name': "sai"}
    return render(request, 'test.html', data)


def create_food_list():
    return [
        {"name": "Pizza", "price": 200},
        {"name": "Burger", "price": 150},
        {"name": "Pasta", "price": 250},
        {"name": "Salad", "price": 100},
        {"name": "Sushi", "price": 0},
    ]


def fooddata(request):
    return render(request, 'menu.html', {'newmenu': create_food_list()})


def menu1(request, item_name):
    menu = create_food_list()
    return render(request, 'menu1.html', {'menu': menu, 'item_name': item_name})



def testimg(request):
    return render(request, 'testimg.html')


def productlist(request):

    products = [
        {
            "name": "smartphone",
            "brand": "Apple",
            "price": 20000,
            "image": "smartphone.jpg"
        },
        {
            "name": "laptop",
            "brand": "Dell",
            "price": 50000,
            "image": "laptopimage.jpg"
        },
        {
            "name": "headphones",
            "brand": "Sony",
            "price": 3000,
            "image": "eye.jpg"
        },
        {
            "name": "camera",
            "brand": "Canon",
            "price": 40000,
            "image": "cam.jpg"
        },
        {
            "name": "smartwatch",
            "brand": "Samsung",
            "price": 10000,
            "image": "msala.jpg"
        },
    ]

    return render(request, 'productlist.html', {'products': products})



def shoppinglist(request):

    shopping = [
        {"name": "smartphone", "brand": "Apple", "price": 20000, "image": "smartphone.jpg"},
        {"name": "laptop", "brand": "Dell", "price": 50000, "image": "laptopimage.jpg"},
        {"name": "headphones", "brand": "Sony", "price": 3000, "image": "eye.jpg"},
        {"name": "camera", "brand": "Canon", "price": 40000, "image": "cam.jpg"},
        {"name": "smartwatch", "brand": "Samsung", "price": 10000, "image": "msala.jpg"},
    ]

    return render(
        request,
        'shoppinglist.html',
        {'shopping_list': shopping}
    )


def shoppinglist1(request, shoppingitem):

    shopping = [
        {"name": "smartphone", "brand": "Apple", "price": 20000, "image": "smartphone.jpg"},
        {"name": "laptop", "brand": "Dell", "price": 50000, "image": "laptopimage.jpg"},
        {"name": "headphones", "brand": "Sony", "price": 3000, "image": "eye.jpg"},
        {"name": "camera", "brand": "Canon", "price": 40000, "image": "cam.jpg"},
        {"name": "smartwatch", "brand": "Samsung", "price": 10000, "image": "msala.jpg"},
    ]

    item = next(
        (i for i in shopping if i["name"] == shoppingitem),
        None
    )

    return render(
        request,
        'shoppingdetails.html',
        {'item_details': item}
    )





# header and footer template

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def food(request):

    newmenu = [
        {"name": "Pizza","price": 200, "size": "medium","image": "masala.jpg"},
        {"name": "Burger","price": 150,"size": "large","image": "eye.jpg"},
        {"name": "Pasta","price": 250,"size": "small","image": "cam.jpg"},
        {"name": "Salad","price": 100,"size": "medium","image": "laptopimage.jpg"},
        {"name": "Sushi","price": 0,"size": "large","image": "smartphone.jpg"},
    ]

    return render(request,'food.html', {'menu_items': newmenu})



# testing css 

def testcss(request):
    return render(request, 'testcss.html')


 



def items(request):
    items = [
        {"name": "laptop"},{"name": "smartphone"},
        {"name": "headphones"},
        {"name": "camera"},
        {"name": "smartwatch"},
    ]
    

    return render(request, 'items.html', {'items': items})



def itemsdetails(request,name):
    items = {

        'laptop':{ "brand": "Apple", "price": 20000, "image": "smartphone.jpg"},
        'smartphone':{ "brand": "Apple", "price": 20000, "image": "smartphone.jpg"},
        'headphones':{ "brand": "Sony", "price": 3000, "image": "eye.jpg"},
        'camera':{ "brand": "Canon", "price": 40000, "image": "cam.jpg"},
        'smartwatch':{ "brand": "Samsung", "price": 10000, "image": "msala.jpg"},
    }
    item = items.get(name)
    if item:
        return render(request, 'itemsdetails.html', {'name': name,'brand': item['brand'], 'price': item['price'], 'image': item['image']})
    else:
        return render(request, 'itemsdetails.html', {'name': name, 'brand': None, 'price': None, 'image': None})





from django.shortcuts import render


def restaurant(request):
    items = [
        { "item_id": 101,"name": "Paneer Tikka Masala","category": "Main Course","price": 240,"spicy_level": 3},
        { "item_id": 102,"name": "Butter Chicken","category": "Main Course","price": 280,"spicy_level": 2},
        { "item_id": 103,"name": "Veg Biryani","category": "Main Course","price": 200,"spicy_level": 1},
        { "item_id": 104,"name": "Chicken Biryani","category": "Main Course","price": 300,"spicy_level": 2},
        { "item_id": 105,"name": "Paneer Butter Masala","category": "Main Course","price": 260,"spicy_level": 2},
        { "item_id": 106,"name": "Chole Bhature","category": "Main Course","price": 180,"spicy_level": 3},
        { "item_id": 107,"name": "Aloo Paratha","category": "Main Course","price": 150,"spicy_level": 1},
        { "item_id": 108,"name": "Masala Dosa","category": "Main Course","price": 120,"spicy_level": 2},
        { "item_id": 109,"name": "Idli Sambar","category": "Main Course","price": 100,"spicy_level": 1},
        { "item_id": 110,"name": "Vada Pav","category": "Snacks","price": 80,"spicy_level": 3}
    ]

    return render(request, "resturent.html", {"items": items})


   






# test cmnds 
# python manage.py test myapp.tests.urltests.test_students_url



def item_detail(request, item_id):
    items = [
        {"item_id": 101, "name": "Paneer Tikka Masala", "category": "Main Course", "price": 240, "spicy_level": 3},
        {"item_id": 102, "name": "Butter Chicken", "category": "Main Course", "price": 280, "spicy_level": 2},
        {"item_id": 103, "name": "Veg Biryani", "category": "Main Course", "price": 200, "spicy_level": 1},
        {"item_id": 104, "name": "Chicken Biryani", "category": "Main Course", "price": 300, "spicy_level": 2},
        {"item_id": 105, "name": "Paneer Butter Masala", "category": "Main Course", "price": 260, "spicy_level": 2},
        {"item_id": 106, "name": "Chole Bhature", "category": "Main Course", "price": 180, "spicy_level": 3},
        {"item_id": 107, "name": "Aloo Paratha", "category": "Main Course", "price": 150, "spicy_level": 1},
        {"item_id": 108, "name": "Masala Dosa", "category": "Main Course", "price": 120, "spicy_level": 2},
        {"item_id": 109, "name": "Idli Sambar", "category": "Main Course", "price": 100, "spicy_level": 1},
        {"item_id": 110, "name": "Vada Pav", "category": "Snacks", "price": 80, "spicy_level": 3},
    ]
    item = next((entry for entry in items if entry["item_id"] == int(item_id)), None)
    if item is None:
        return HttpResponse("<h1>Item not found</h1>", status=404)
    return render(request, "resturent.html", {"items": [item]})















def sampletest(request):
    return HttpResponse("<h1>this is a simple test</h1>")




def sampletest1(request,id):
    return  HttpResponse(f"the id is{id}")

    

























