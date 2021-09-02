
class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate


    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, numberOfMeals):
        if numberOfMeals == 3:
            self.healthRate = '100%'
        elif numberOfMeals == 2:
            self.healthRate = '75%'
        elif numberOfMeals == 1:
            self.healthRate = '50%'
        else:
            self.healthRate = 'HERO'

    
    def buy(self, numberOfItems):
        self.money -= numberOfItems * 10

    def __str__(self):
        return f"Name: {self.name} Mood {self.mood}"



class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name 
        self.fuelRate = fuelRate
        self.velocity = velocity

    
    def stop(self, distance):
        self.velocity = 0
        print(f"The Remaining Distance is {distance}")
    
    def run(self, velocity, distance):
        if self.fuelRate <= 0:
            self.fuelRate = 0
        else:
            self.fuelRate -= 1 
         
        if velocity > 200:
            self.velocity = 200
        else:
            self.velocity = velocity
        # calling stop method     
        self.stop(distance)

    def __str__(self):
        return f'car name : {self.name}'




idd = carr = emaill = salaryy = distanceToWorkk = [] 
class Employee():
    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        # save date 
        idd.append(id); carr.append(car); emaill.append(email)
        salaryy.append(salary); distanceToWorkk.append(distanceToWork)

    # def drive(self, distance):
    #     self.run(distance, self.velocity)

    # def refuel(self, gasAmount):
    #     self.fuelRate += 1 

namee = [] 
class Office():
    def __init__(self, name, empoyees):
        self.name = name 
        self.employees = empoyees
        # save data
        namee.append(name)

    # all methods depends on Employee class
    def get_all_employees (self):
        j = 1
        for i in namee:
            print(f'Office number{j} is ' , end='')
            print(i)
            j += 1

    def __str__(self):
        return f'Office name: {self.name}'


    # def get_employee(self, empid):
    #     idx = 0
    #     for i in idd:
    #         if i == self.empid:
    #             idx = i

    #     print(f'{namee[idx]}')

    # def fire(self, empid):
    #     idx = 0
    #     for i in idd:
    #         if i == empid:
    #             idx = i

    #     self.idd[idx] = 0
    #     self.carr[idx] = 0
    #     self.emaill[idx] = 0
    #     self.salaryy[idx] = 0
    #     self.distanceToWorkk[idx] = 0 









