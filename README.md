# Deployment of Health Risk Prediction on Heroku! 

References and resources gathered from:

* Flask Documentation for HTML/Bootstrap: 	https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
* Flask Cheat Sheet: https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf
* Youtube Tutorial on Deployment: https://www.youtube.com/watch?v=mrExsjcvF4o

## Dockerize and Deploy!
1. git clone [project_url]
2. docker build . -t [Image Name] #-- Provide an image name of choice.
3. docker run -p 5000:5000 [Image Name]

* Check the host IP and browse using a browser with exposed port mapping.
