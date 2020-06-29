python test project

1. Set up development environment
pull this repo and create a new virtual environment like this

$ python -m venv venv-python-test
$ virtualenv venv-python-test

then from within the virtual environment

$pip install -r requirements.txt

set the right database URI in appconfig.py (instructions in the file)

2. Set up containerized environment
 
If you like to run this project in a docker/kubernetes environment, follow the instructions below:
- set the database URI in the appconfig.py to the mysql URI if you like to use a mysql database
- to make a docker image use the following command
        docker build -f Dockerfile -t python_test_project:latest .
- to deploy in kubernetes apply de yamls contained in de k8s directory
-  to access the kubernetes services run the portforward scripts in the project root


to make use of the kubernetes mysql in dev mode, add an entry in your host file:
127.0.0.1  mysql


