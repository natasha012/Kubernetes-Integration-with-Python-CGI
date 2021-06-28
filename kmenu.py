#!/usr/bin/python3

import cgi
import subprocess

print("context-type:text/html")
print()

f=cgi.FieldStorage()
x=f.getvalue("x")
words = x.split()
if words[0]== "launch":
  cmd="kubectl create deployement "+words[1]+ " --image="+words[3]
if words[0]== "run":
  cmd="kubectl run "+words[1]+ " --image="+words[3]
elif words[0]== "expose":
  cmd="kubectl expose deployment "+words[1]+  " --port="+words[3]+" --type"+words[3]
elif words[0]== "scale":
  cmd="kubectl scale deployment "+words[1]+ " --replicas="+words[3]
elif words[0]== "delete":
  if words[1]=="everything":
    cmd="kubectl delete all --all"
  elif words[1]=="pod":
    cmd="kubectl delete pod "+words[2]
  elif words[1]=="deployment":
    cmd="kubectl delete deployment "+words[2]
elif words[0]== "tell":
  if words[4]=="pods" or words[4]=="pod" :
    cmd="kubectl get pods"
  elif words[4]=="deployments" or words[4]=="deployment":
    cmd="kubectl get deployments"
  elif words[4]=="services" or words[4]=="service":
    cmd="kubectl get svc "    
else:
  cmd="echo Please refer to menu!!!"

o=subprocess.getoutput("sudo "+cmd+" --kubeconfig /root/k8s/admin.conf")
print(o)
