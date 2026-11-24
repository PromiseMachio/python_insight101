# Django Framework
---
Django framework is used in response and request handling in websites created using python.
It uses http as a JSON joint handler which fetches data from the backend and send to the frontend and vice verse.
It has status which shows if the requests and the responses are successful or not.
The status include 200, 404, 500 etc...

---
## Installation and starting the project
---
Since django framework has dependencies that can conflict with the global dependencies of python we create a virtual environment 
where the project stays. 
Installing Django
-Install python3 first
-Install pip
-Install django:
                pip install django
creating a vitual environment:
    cd/path/<projectDirectorate>
    python3 -m venv <name_of_the_virtual_env(DesiredName)>
    Example
    python3 -m venv venv

Activating the virtual enviroment
    In the directorate where you created the virtual env
    command:
    source /venv/bin/activate

=> Process to follow for the installations not to conflict each other
    First Have you python3 installed 
     python --version
        Python 3.10.12
    Then secondly pip installed 
     pip --version
        pip 22.0.2 from /home/master-dev/user/scripting/Geeks4Geeks/DSA_Fullcourse/day4/venv/lib/python3.10/site-packages/pip (python 3.10)

    create a directorate:
        cd inside it
    create a virtual env :
        inside it install django framework 
            pip install django
---
## Django project 
---
 To start a django project is simple 
    django-admin startproject <nameOfTheproject>
     
    python3 manage.py runserver
    
 Think of the projects a google server and then inside it, it has the search and the google lenses and the google widgets.
 This are achieved by python start app under django framework
    inside the directorate but not the project run
    python manage.py startapp <nameOfTheAPP>
 Move to settings under the main project and add the name of the app <nameOfTheApp> in installed apps.
---
## Django app
---
Django app is where most of the building happens from working with backend to connecting with frontend.
For now you have seen quite a number of folders in the newly created app 
### views.py
This is what the users sees and is mostly created using functions 
### urls.py
For now you will only see the urls.py folder in the main project but one can add it in the app using the 
    /touch urls.p
What is it used for? This file is used for creating responses and request displayed on the browser for your app. 
Why not cluster all of them just in the server main project urls.py? Think of it like amazon shopping app with all those activities to be
displayed. So if an app created for maybe searching and adding items to cart has it's urls added to main project's urls.py then have also urls for user profile add their. This will bring about clustering and hard to maintain code 
---
## Template Folder
---
Under views.py 'frontend' for django framework. You can as well render a .html template and create it in the template folder.
So thats how we start to connect the frontend  view to our app.
### Creating a template
 Inside your app.
 create a new folder called template
 command in terminal
 ```
 bash:
  :~ mkdir template
  :~ cd template
  /template/:~ touch file.html
 ```

 ### How to run a .html file in views.py
 Here we are basically rendering it not resquesting a display in the text 
 ```
  python
   from django.shortcuts import render

   # create a function
   def example_func(request):
        return render(request, '/file.html')
 ```
---
## Static files in django 
---
Unlike in the normal htmls here first configure the settings by creating a static files detector in just under STATIC_URL
```
settings.py

    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
```
NOTE: our STATIC_FILE ='/static/'  
    -> This implies that we create a folder called statics to hold our images and vedios 

After that inside our .html where we want to add the image 
```
.html
-> On top just above <!DOCTYPE>
add 
{%load static%}

inside our body where there is image tag 
<img src="{% static 'image.jpg'%}" alt='image'>
```
---

## Templete inheritance
---
This is a .html file where other child .html files copy to and from. For instance in a task app we have main .html file where all our tasks are displayed but we have to add tasks, or edit , or delete tasks from the templete this can be achieved by having other .html files inheriting from it.
### How to achieve the template .html inheritance 
```
For instance we are having two files and the two are related in some ways like main page and edit. 
we will have an additional file called layout.html(one can have their desired name) for creating the interconnection between the pages/files. Where they will be inheriting the layout feature for code reusability and maintainability 
NOTE: We will only be having the .html <!DOCTYPE> (Boilerplate code) layout in the layout.html while the rest only have a feature called extend and main content 
Example:  (a) layout.html 
            {% load static %}
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>task_layout</title>
                <link rel="stylesheet" href="{% static 'styles/styles.css'%}">
            </head>
            <body>
                {% block body%}
                {% endblock %}
                
            </body>
            </html>
        
        (b) add.html
        {% extends 'tasks/layout.html'%}

        {% block body %}
        <main class="main">
            <form class="card" method="post" action="{% url 'add' %}">
                {% csrf_token %}
                <label style="display: block; margin: 10px;" for="add">Add a task to your Checklist</label>
                <input type="text"
                    style="display: block; padding: 10px; border-radius: 5px; background-color:antiquewhite ; color: black; width: 300px;">
                <div class="buttons">
                    <button type="submit" class="add" style="margin: 10px;">Add</button>
                    <a class="exit" style="margin: 10px;" href="{% url 'tasks' %}">Back</a>
                </div>
            </form>
        </main>
        {% endblock %}

    (c) index.html
        {% extends 'tasks/layout.html'%}

        {% block body %}
            <main class="main">
                <div class="card">
                    <p>
                        Passenger:
                        <span class="passenger-name">Machio Promise</span>
                    </p>

                    <p>Phone Number: 0714916372</p>

                    <ul>
                        <p>CheckList</p>
                        {% for task in tasks %}
                            <li class="task">
                                <input type="checkbox" {% if task.completed %}checked{% endif %}>
                                {{ task.title }}
                            </li>
                        {% empty %}
                            <li>No tasks added yet.</li>
                        {% endfor %}
                    </ul>
                    <div class="buttons">
                        <a class="add" href="{% url 'add'%}">Add Task</a>
                        <a class="edit" href="#">Edit Task</a>
                    </div>
                </div>
            </main>

        {% endblock %}

```
---
### Sessions in django
---
    For instance in a banking app every user will have their own differnt and secure accounts with details know to them alone. This happens but at the same time we have so many users connected in that bank server. So what happens is that a dictionaty-like object attached to every HttpRequest when SessionMiddleware is active(it is by default). So this lets store and retrieves per-user-data across multiple requests(eg user logs in, deposited money, transfered money, etc)
---