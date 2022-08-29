import json
a={"Name": "Abhishek",
"Designation": "CEO of navgurukul",
"Gender":"male",
"Age": "29"
}
with open("file_txt.json","w") as file:
    json.dump(a,file,indent=4)