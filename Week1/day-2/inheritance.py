class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}, salary: Rp.{self.salary:,}"
    
    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name} got a raise! New salary: Rp{self.salary:,}"
    
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        self.projects = []
        
    def add_project(self, project_name):
        self.projects.append(project_name)
        return f"Project '{project_name}' added!"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Language: {self.programming_language} | Project: {len(self.projects)}"
    
    
class Manager(Employee):
    def __init__(self, name, salary, departement):
        super().__init__(name, salary)
        self.departement = departement
        self.team = []
        
    def add_team(self, employee):
        self.team.append(employee)
        return f"{employee.name} added to {self.departement} team!"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Departement: {self.departement} | Team size: {len(self.team)}" 
        
    
# Test
dev = Developer("Nova", 8000000, "Python")
dev.add_project("E-commerce Website")
dev.add_project("ML Model")
print(dev.get_info())

manager = Manager("Chelsea", 15000000, "Engineering")
manager.add_team(dev)
print(manager.get_info())
    
        
    
    