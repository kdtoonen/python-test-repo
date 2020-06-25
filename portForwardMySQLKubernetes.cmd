@ECHO OFF
:RUN
kubectl port-forward service/mysql 3306:3306
GOTO RUN
:END