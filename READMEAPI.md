What is an API call (answer in your own words)?
    An API call is basically a way for one piece of software to request data or perform actions (like display a message) on another software system through an API.

What is an example we discussed to create an API call locally? 
    Go on FastAPI. Install in virtual environment. Write sa python script that defines an endpoint. Run a development server locally using FastAPI or uvicorn. Access the endpoint via a browser or a tool like curl to get JSON responses like "Hello World".

What is an example we discussed to create an API call on the cloud? 
    We used AWS Lambda with API Gateway. A Lambda function was created that returns a response using Python. API Gateway was configured to expose the function as an HTTP endpoint. A test request was sent using Postman, where the payload was passed in JSON format. API keys and usage plans were also set up to control access and throttling.

What is the difference between FastAPI and creating API from AWS Gateway?
    FastAPI is ideal for local dev; AWS Gateway + Lambda is built for production-scale deployment.
In your own words after watching the video, what are the main steps to create an API call on AWS Gateway?
    - Create a Lambda Function 
    - Add an API Gateway Trigger
    - Configure API Gateway
    - Deploy to a Stage 
    - Test the API using tols like Postman 
    - Add Usage Plans 

Professionally in the industry, how does developers ship product from one team to another? What's the usage of API here?
    In the industry, developers ship functionality as APIs so different teams can work independently.The usage of API here can be Encapsulation, Scalability, Modularity, and Security & Governance. 