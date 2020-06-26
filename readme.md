python test project

pull this repo and create a new virtual environment like this

$ python -m venv venv-python-test
$ virtualenv venv-python-test

then from within the virtual environment

$pip install -r requirements.txt


to make a docker image use the following command
docker build -f Dockerfile -t python_test_project:latest .
to deploy in kubernetes apply de yamls contained in de k8s directory
to access the kubernetes services run the portforward scripts in the project root


to make use of the kubernetes mysql, add an entry in your host file:
127.0.0.1  mysql


