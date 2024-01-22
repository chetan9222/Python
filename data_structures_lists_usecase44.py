#####V44####### Map of Lists usecase
students = {'Chetan':['python','Django','RHCSA'],'Prashant':['react','node','js'],'Vijay':['js','CCNA']}
keys = students.keys()

for eachkey in keys:
    print("courses is taken by",eachkey,"are : ")
    for eachcourse in students[eachkey]:
        print(eachcourse)
