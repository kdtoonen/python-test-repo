@ECHO OFF
:RUN
kubectl port-forward service/python-test-project-service 5002:6000
GOTO RUN
:END