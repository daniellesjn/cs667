What is a class object?
    A class defines properties (attributes) and methods (functions) that objects created from the class will have. A class object is an instance of a class that contains its own atrributes to make it unique. In our example, URLValidator is our clas object that contains different methods and API calls. 

What is docstring?
    A docstring is a special kind of comment used to describe the purpose and functionality of a function, method, class, or module.

How to define init of a class object? 
    'def__init__(self):'

What is a method?
    A method is a function that is tied to a class and can access and manipulate the data of that class,its instances, or input data. For example, fetch_page_content(self,url: str) -> str: 

How do you let functions fail gracefully?
    The easiest way is to use a "try:" statement using except. So in our except statement, if something goes wrong in our API calls we let it fail but won't fail the entire script. 

What's a standard practice of a return statement?
    Returning a JSON makes the return value something that is in nature of natural language for everyone to understand and is readable. 