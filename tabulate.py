from tabulate import tabulate
title=["name","age","department"]
data=[["mahi",21,"CSE"],
     ["sunny",60,"MECH"],
     ["arjun",55,"CIVIL"],
     ["sathish",43,"IT"]]
res=tabulate(data,headers=title,tablefmt="preety")
print(res)
