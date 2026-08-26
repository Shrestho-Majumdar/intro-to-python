EMP = {
    "E1": {
        "Name": "David Beckham",
        "Designation": "Manager",
        "Department": "Software Engineering",
        "Salary": 80000
    },
    "E2": {
        "Name": "Cristiano Ronaldo",
        "Designation": "Officer",
        "Department": "Artificial Intelligence",
        "Salary": 77000
    },
    "E3": {
        "Name": "Masha Messi",
        "Designation": "Intern",
        "Department": "Software Engineering",
        "Salary": 22000
    },
    "E4": {
        "Name": "Erling Haaland",
        "Designation": "Officer",
        "Department": "Machine Learning",
        "Salary": 80000
    },
    "E5": {
        "Name": "Neymar Jr.",
        "Designation": "Officer",
        "Department": "Software Engineering",
        "Salary": 80000
    }
}
print(EMP.get("E1"))#details of E1

print(EMP.get("E4").get("Department")) #department of E4

max_emp = max(EMP, key=lambda x: EMP[x]["Salary"])#employee who got maximum salary
print(max_emp)

EMP.update({#add new record
    "E6": {
        "Name": "Nahuel Mollina",
        "Designation": "Intern",
        "Department": "Software Engineering",
        "Salary": 25000
    }
})
