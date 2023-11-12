#EX1
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Shape: {self.name}."

    def perimeter(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = self._validate_positive_dimension(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def _validate_positive_dimension(self, value):
        if value < 0:
            return f"Dimensions must be non-negative."
        return value

    def __str__(self):
        return f"{super().__str__()} The radius is {self.radius} units."

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = self._validate_positive_dimension(length)
        self.width = self._validate_positive_dimension(width)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return  2 * (self.length + self.width)

    def _validate_positive_dimension(self, value):
        if value < 0:
            return f"Dimensions must be non-negative."
        return value

    def __str__(self):
        return f"{super().__str__()} The length is {self.length} units, and the width is {self.width} units."

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = self._validate_positive_dimension(side1)
        self.side2 = self._validate_positive_dimension(side2)
        self.side3 = self._validate_positive_dimension(side3)

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def _validate_positive_dimension(self, value):
        if value < 0:
            return f"Dimensions must be non-negative."
        return value

    def __str__(self):
        return f"{super().__str__()} The sides are {self.side1}, {self.side2}, and {self.side3} units."

print("Ex 1: ")
circle = Circle(4)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(shape)
    print(f"Area: {shape.area():.2f} square units")
    print(f"Perimeter: {shape.perimeter():.2f} units")
    print()

#EX2
class Account():
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def __str__(self):
        return f"Account {self.account_number} balance: ${self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01, account_holder=""):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        self.account_holder = account_holder

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest calculated: ${interest}")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} to {target_account.account_number}.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def __str__(self):
        return f"Savings Account {self.account_number} balance: ${self.balance} (Holder: {self.account_holder}) with interest rate {self.interest_rate * 100}%"

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100, account_holder=""):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.account_holder = account_holder

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit reached.")

    def transfer(self, amount, target_account):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} to {target_account.account_number}.")
        else:
            print("Invalid transfer amount or overdraft limit reached.")

    def __str__(self):
        return f"Checking Account {self.account_number} balance: ${self.balance} (Holder: {self.account_holder}) with overdraft limit ${self.overdraft_limit}"


print("Ex 2: ")
savings_account1 = SavingsAccount(account_number="SA123", balance=1000, interest_rate=0.02, account_holder="Claudiu")
checking_account = CheckingAccount(account_number="CA456", balance=500, overdraft_limit=200, account_holder="Adrian")
savings_account2 = SavingsAccount(account_number="SA789", balance=1500, interest_rate=0.02, account_holder="Roxana")

print(str(savings_account1))
print(str(checking_account))
print(str(savings_account2))

savings_account1.deposit(200)
checking_account.withdraw(100)
savings_account2.calculate_interest()

print(str(savings_account1))
print(str(checking_account))
print(str(savings_account2))

#EX 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def calculate_mileage(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency, fuel_capacity, num_doors):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency
        self.num_doors = num_doors
        self.fuel_capacity = fuel_capacity
        self.current_fuel = 0
        self.total_distance = 0
        self.total_fuel_consumed = 0

    def calculate_mileage(self):
        if self.total_fuel_consumed > 0:
            return self.total_distance / self.total_fuel_consumed
        else:
            return 0

    def additional_info(self):
        return f"{self.display_info()} has {self.num_doors} doors."

    def calculate_usage_cost(self, distance, fuel_price_per_liter):
        fuel_needed = distance / self.calculate_mileage()
        cost = fuel_needed * fuel_price_per_liter
        return f"{self.display_info()} will cost ${cost:.2f} for {distance} km at ${fuel_price_per_liter:.2f} per liter."

    def add_fuel(self, liters):
        if self.current_fuel + liters <= self.fuel_capacity:
            self.current_fuel += liters
            return f"Added {liters} liters of fuel. Current fuel level: {self.current_fuel} liters."
        else:
            return f"Cannot add {liters} liters of fuel. Exceeds fuel capacity."

    def drive(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        if fuel_needed <= self.current_fuel:
            self.current_fuel -= fuel_needed
            self.total_distance += distance
            self.total_fuel_consumed += fuel_needed
            return f"Traveled {distance} km. Current fuel level: {self.current_fuel} liters."
        else:
            return f"Not enough fuel to travel {distance} km. Refuel needed."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency, has_sidecar=False):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency
        self.has_sidecar = has_sidecar
        self.total_distance = 0
        self.total_fuel_consumed = 0

    def calculate_mileage(self):
        if self.total_fuel_consumed > 0:
            return self.total_distance / self.total_fuel_consumed
        else:
            return 0

    def add_fuel(self, liters):
        self.total_fuel_consumed += liters
        return f"Added {liters} liters of fuel. Total fuel consumed: {self.total_fuel_consumed} liters."

    def drive(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        self.total_distance += distance
        self.total_fuel_consumed += fuel_needed
        return f"Traveled {distance} km. Total fuel consumed: {self.total_fuel_consumed} liters."

    def additional_info(self):
        if self.has_sidecar:
            return f"The motorcycle {self.display_info()} has a sidecar."
        else:
            return f"The motorcycle{self.display_info()} doesn't have a sidecar."

    def calculate_maintenance_cost(self, distance, maintenance_cost_per_mile):
        return f"{self.display_info()} maintenance cost is ${distance * maintenance_cost_per_mile:.2f} for {distance} miles at ${maintenance_cost_per_mile:.2f} per mile."

class Truck(Vehicle):
    def __init__(self, make, model, year, gcwr):
        super().__init__(make, model, year)
        self.gcwr = gcwr
        self.payload_weight = 0
        self.calculate_towing_capacity()

    def add_fuel(self, liters):
        return f"Added {liters} liters of fuel."

    def drive(self, distance):
        return f"Traveled {distance} km."

    def load_payload(self, payload_weight):
        self.payload_weight += payload_weight
        self.calculate_towing_capacity()
        return f"Loaded {payload_weight} tons of payload. New payload weight: {self.payload_weight} tons. Updated towing capacity."

    def calculate_towing_capacity(self):
        self.remaining_towing_capacity = self.gcwr - self.payload_weight

    def tow(self, weight):
        if weight <= self.remaining_towing_capacity:
            self.remaining_towing_capacity -= weight
            return f"Towed {weight} tons. Remaining towing capacity: {self.remaining_towing_capacity} tons."
        else:
            return f"Cannot tow {weight} tons. Exceeds remaining towing capacity."

    def additional_info(self):
        return f"Truck: {self.display_info()} "



print("Ex 3: ")
car = Car(make="Toyota", model="Camry", year=2022, fuel_efficiency=15, fuel_capacity=50, num_doors=4)
print(car.additional_info())
print(car.add_fuel(30))
print(car.drive(200))
print(car.drive(100))
current_mileage = car.calculate_mileage()
print(f"Current mileage: {current_mileage:.2f} km per liter")
print()

motorcycle = Motorcycle(make="Ducati", model="Monster", year=2023, fuel_efficiency=18, has_sidecar=False)
print(motorcycle.additional_info())
print(motorcycle.add_fuel(15))
print(motorcycle.drive(120))
print(motorcycle.drive(80))
current_mileage_another = motorcycle.calculate_mileage()
print(f"Current mileage for the motorcycle: {current_mileage_another:.2f} km per liter")
print()

truck = Truck(make="Ford", model="F-150", year=2022, gcwr=10)
print(truck.additional_info())
print(truck.add_fuel(50))
print(truck.drive(300))
print(truck.load_payload(3))
print(truck.tow(5))
print(truck.tow(4))
print()


#EX4
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        pass

    def display_info(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nSalary: {self.calculate_salary()}"

class Manager(Employee):
    def __init__(self, name, employee_id, bonus, team_size):
        super().__init__(name, employee_id)
        self.bonus = bonus
        self.team_size = team_size

    def calculate_salary(self):
        base_salary = 50000
        return base_salary + self.bonus + self.team_size * 1000

    def manage_team(self):
        return f"{self.name} is managing a team of {self.team_size} people."

    def calculate_team_productivity(self):
        return f"Team productivity score: {self.team_size * 10}."


class Engineer(Employee):
    def __init__(self, name, employee_id, technical_skills, lines_of_code_written):
        super().__init__(name, employee_id)
        self.technical_skills = technical_skills
        self.lines_of_code_written = lines_of_code_written

    def calculate_salary(self):
        base_salary = 50000
        return base_salary + len(self.technical_skills) * 1000 + self.lines_of_code_written * 0.1

    def review_code(self, lines_reviewed):
        return f"{self.name} reviewed {lines_reviewed} lines of code."

    def calculate_code_quality(self):
        return f"{self.name}'s code quality score: {self.lines_of_code_written / 100}."
    def code(self):
        return f"{self.name} is writing code."

class Salesperson(Employee):
    def __init__(self, name, employee_id, sales_target, commission_rate, deals_closed):
        super().__init__(name, employee_id)
        self.sales_target = sales_target
        self.commission_rate = commission_rate
        self.deals_closed = deals_closed

    def calculate_salary(self):
        base_salary = 40000
        commission = min(self.sales_target * self.commission_rate, 20000)
        return base_salary + commission + self.deals_closed * 500

    def calculate_sales_performance(self):
        return f"{self.name}'s sales performance score: {self.deals_closed * 100}."
    def make_sale(self):
        return f"{self.name} made a sale."


manager = Manager(name="Corneliu Adrian", employee_id=1451, bonus=10000, team_size=8)
engineer = Engineer(name="Andrei Alexandru", employee_id=2987, technical_skills=["Python", "Java", "SQL"], lines_of_code_written=5000)
salesperson = Salesperson(name="Carp Oana", employee_id=3341, sales_target=50000, commission_rate=0.05, deals_closed=15)

employees = [manager, engineer, salesperson]
print("Ex 4: ")
for employee in employees:
    print(employee.display_info())
    if isinstance(employee, Manager):
        print(employee.manage_team())
        print(employee.calculate_team_productivity())
    elif isinstance(employee, Engineer):
        print(employee.code())
        print(employee.review_code(lines_reviewed=200))
        print(employee.calculate_code_quality())
    elif isinstance(employee, Salesperson):
        print(employee.make_sale())
        print(employee.calculate_sales_performance())
    print("\n")


#Ex 5
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        return f"{self.name} is an animal that lives in {self.habitat}."

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color, num_legs, weight):
        super().__init__(name, habitat)
        self.fur_color = fur_color
        self.num_legs = num_legs
        self.weight = weight

    def fur(self):
        return f"{self.name} has {self.fur_color} fur and {self.num_legs} legs."

    def give_birth(self):
        return f"{self.name} is a mammal and gives birth to live young."

    def run(self, speed):
        return f"{self.name} is running at a speed of {speed} km/h"

    def calculate_food_cost(self, daily_food_intake_cost):
        monthly_food_cost = self.weight * daily_food_intake_cost * 30
        return f"The estimated monthly food cost for {self.name} is ${monthly_food_cost:.2f}"

class Bird(Animal):
    def __init__(self, name, habitat, feather_color, wingspan, can_fly):
        super().__init__(name, habitat)
        self.feather_color = feather_color
        self.wingspan = wingspan
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying with a wingspan of {self.wingspan} units"
        else:
            return f"{self.name} cannot fly"

    def migrate(self, distance):
        return f"{self.name} is migrating a distance of {distance} km"

    def calculate_flight_time(self, speed, distance):
        time = distance / speed
        return f"{self.name} would take approximately {time} hours to fly {distance} km at {speed} km/h"


class Fish(Animal):
    def __init__(self, name, habitat, scale_color, water_type):
        super().__init__(name, habitat)
        self.scale_color = scale_color
        self.water_type = water_type

    def swim(self):
        return f"{self.name} is swimming with {self.scale_color} scales in {self.water_type} water"

    def calculate_pressure_at_depth(self, depth):
        water_density = 1000
        gravity = 9.8
        pressure = water_density * gravity * depth
        return f"The pressure at a depth of {depth} meters for {self.name} is approximately {pressure} Pascals"


print("Ex 5: ")
lion = Mammal(name="Lion", habitat="Grasslands", fur_color="Golden", num_legs=4, weight=200)
swan = Bird(name="Swan", habitat="Lakes", feather_color="White", wingspan=150, can_fly=True)
salmon = Fish(name="Salmon", habitat="Rivers", scale_color="Silver", water_type="Freshwater")

print(lion.display_info())
print(lion.fur())
print(lion.give_birth())
print(lion.run(speed=50))
print(lion.calculate_food_cost(daily_food_intake_cost=2.5))
print()

print(swan.display_info())
print(swan.fly())
print(swan.migrate(distance=200))
print(swan.calculate_flight_time(speed=30, distance=200))
print()

print(salmon.display_info())
print(salmon.swim())
print(salmon.calculate_pressure_at_depth(depth=10))
print()

#EX6
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} by {self.author} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"Thank you for returning {self.title}."
        else:
            return f"{self.title} is not currently checked out."

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nItem ID: {self.item_id}\nStatus: {'Checked out' if self.checked_out else 'Available'}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages, publication_year):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages
        self.publication_year = publication_year

    def calculate_overdue_fee(self, days):
        overdue_fee = 0.10 * days
        return f"The overdue fee for {self.title} is ${overdue_fee:.2f}"

    def display_info(self):
        return f"{super().display_info()}\nNumber of Pages: {self.num_pages}\nPublication Year: {self.publication_year}"

    def calculate_reading_time(self, average_reading_speed):
        reading_time = self.num_pages / average_reading_speed
        return f"The estimated reading time for {self.title} is {reading_time:.2f} minutes."


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration_minutes, release_year):
        super().__init__(title, director, item_id)
        self.duration_minutes = duration_minutes
        self.release_year = release_year

    def display_info(self):
        return f"{super().display_info()}\nDuration: {self.duration_minutes} minutes\nRelease Year: {self.release_year}"

    def calculate_storage_size(self):
        storage_size = self.duration_minutes ** 0.5
        return f"The estimated storage size for {self.title} is {storage_size:.2f} GB."


class Magazine(LibraryItem):
    def __init__(self, title, issue_date, item_id, publisher):
        super().__init__(title, "N/A", item_id)
        self.issue_date = issue_date
        self.publisher = publisher

    def display_info(self):
        return f"{super().display_info()}\nIssue Date: {self.issue_date}\nPublisher: {self.publisher}"

    def calculate_subscription_cost(self, num_months):
        subscription_cost = 1.50 * num_months
        return f"The subscription cost for {self.title} is ${subscription_cost:.2f}"

    def calculate_advertising_revenue(self, num_ads):
        ad_rate = 50
        advertising_revenue = ad_rate * num_ads
        return f"The estimated advertising revenue for {self.title} is ${advertising_revenue:.2f}"


print("Ex 6: ")
book = Book(title="The Picture of Dorian Gray", author="Oscar Wilde", item_id="A001", num_pages=180, publication_year=1891)
dvd = DVD(title="The Shawshank Redemption", director="Frank Darabont", item_id="D002", duration_minutes=142, release_year=1994)
magazine = Magazine(title="National Geographic", issue_date="October 2023", item_id="S001", publisher="National Geographic Society")

print(book.check_out())
print(book.display_info())
print(book.calculate_reading_time(2))
print(book.calculate_overdue_fee(days=5))
print(book.return_item())
print()

print(dvd.check_out())
print(dvd.display_info())
print(dvd.calculate_storage_size())
print(dvd.return_item())
print()

print(magazine.check_out())
print(magazine.display_info())
print(magazine.calculate_subscription_cost(num_months=12))
print(magazine.calculate_advertising_revenue(num_ads=10))
print(magazine.return_item())
print()
