import json

emp1={"name":"neelam","Designation":"programer","Age":"24","Salary":"2400"}
emp2={"name":"komal","Designation":"trainer","Age":"24","salary":"20000"}
emp3={"name":"anuradha","Designation":"HR","Age":"25","salary":"40000"}
emp4={"name":"Abhishek","Designation":"manager","Age":"29","salary":"63000"}

d=[]
d.append(emp1)
d.append(emp2)
d.append(emp3)
d.append(emp4)

with open("file2_txt.json","w") as file:
    json.dump(d,file,indent=4)







