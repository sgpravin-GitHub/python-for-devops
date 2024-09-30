#get pull request information on GIT repository(Kubernetes repository) using python

import requests

#/repos/{owner}/{repo}/pulls

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
output = response.json()
# print(type(output)) => list
for i in range(len(output)): #it give the whole list of users in the json file
    print(i , " = ", output[i]["user"]["login"])

#to delete a key from dectionary:
del output[0]["name"]["id"]  # del my_doc["city"]

