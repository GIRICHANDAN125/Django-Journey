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

fooddetails = {
    "name": "Pizza",
    "price": 200,
    "size":"reqular",
    "topping":"olive"
}

print(fooddetails.items())
for key, value in fooddetails.items():
    print(f"{key}: {value}")
    
    

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



def studentinfo(request):
    student = [
        {"Name": "navneet", "Marks": 67, "Course": "Django"},
        {"Name": "sachin", "Marks": 89, "Course": "Python"},
        {"Name": "rahul", "Marks": 45, "Course": "Java"},
        {"Name": "rohit", "Marks": 78, "Course": "C++"},
        {"Name": "virat", "Marks": 90, "Course": "JavaScript"},
    ]

    content = '<table border="1"><tr>'

    # Create table headings
    for column in student[0].keys():
        content += f"<th>{column}</th>"

    content += "</tr>"

    # Create table rows
    for i in student:
        content += "<tr>"

        for value in i.values():
            content += f"<td>{value}</td>"

        content += "</tr>"

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