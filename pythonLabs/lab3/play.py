from lab3 import Employee, Person,Office, Car 
# test class Person
def play():
    person1 = Person('Mohamed Abdelhamid', 100, 'happy', '100%')
    print(person1.name)
    print(person1.money)
    print(person1.mood)
    print(person1.healthRate)

    (person1.sleep(3))
    (person1.sleep(7))
    (person1.sleep(10))

    (person1.eat(3))
    (person1.eat(2))
    (person1.eat(1))
    (person1.eat(5))

    print(person1.buy(3))

    # test class car 
    car = Car('Toyota', 100, 200)
    print(car.name)
    print(car.fuelRate)
    print(car.velocity)

    print(car.run(80, 90))
    print(car.stop(20))

    # test class Office 
    of = Office('iti', 'noha')
    print(of.name)
    print(of.employees)


if __name__ == '__main__':
    play()



