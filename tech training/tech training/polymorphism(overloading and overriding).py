# prg 1  method overloading using the duck typing 
"""class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)"""

# prg 2 method overriding 
"""class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working...!")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software engineer is working")
e1=Engineer()
e1.work()
s1=SoftwareEngineer()
s1.work()"""


# problem statement 1 using the employee work hours ( method over riding)
"""class Employee:
    def work_hours(self):
        print("Employee works 8 hours a day")

class Intern(Employee):  # inherits Employee
    def work_hours(self):  # overrides method
        print("Intern works 6 hours a day")

# Test case
intern = Intern()
intern.work_hours()"""

# problem statement 2 using the food delivery offers different delivery charges based on the customer type
"""class Customer:
    def delivery_charge(self):
        print("Delivery Charge: 50 rupees")
class PrimeCustomer(Customer):  # inherits Customer
    def delivery_charge(self):  # overrides method
        print("Delivery Charge: 20 rupees")
print("Prime Customer")
p = PrimeCustomer()
p.delivery_charge()
print("\n Regular Customer")
c = Customer()
c.delivery_charge()"""

# problem statement 3 using a multiplex offers different tichet prices based on the ticket category
"""class Ticket:
    def price(self):
        print(" Normal Ticket Price: ₹150")

class VIPTicket(Ticket): 
    def price(self):  
        print(" vIP Ticket Price: ₹500")
vip = VIPTicket()
vip.price()
vip=Ticket()
vip.price()"""

# problem statement 4 bank offer
"""class Bank:
    def interest_rate(self):
        print("Interest Rate: 4%")
class PrivateBank(Bank):
    def interest_rate(self):
        print("Interest Rate: 6%")
print("Test Case 1 - Private Bank")
pb = PrivateBank()
pb.interest_rate()
"""
# problem statement 5
"""class Course:
    def course_fee(self):
        print("Course Fee: ₹5000")
class AdvancedCourse(Course):
    def course_fee(self):
        print("Course Fee: ₹12000")
print("Advanced Course")
ac = AdvancedCourse()
ac.course_fee()
print("\nBasic Course")
bc = Course()
bc.course_fee()"""

# problem statement 6 A ride-booking application offers different fare structures for normal and luxury rides
"""class Ride:
    def fare(self):
        print("Fare: ₹100")

class LuxuryRide(Ride):
    def fare(self):
        print("Fare: ₹300")

print("Luxury Ride")
LuxuryRide().fare()
print("\nNormal Ride")
Ride().fare()"""

# problem statement 7 A video streaming platform offers different viewing experiences based on the subscription plan
"""class Subscription:
    def features(self):
        print("Watch videos with advertisements")
class PremiumSubscription(Subscription):
    def features(self):
        print("Watch videos without advertisements")
print("Premium Plan")
PremiumSubscription().features()
print("\nBasic Plan")
Subscription().features()"""

# problem statement 8 Different vehicles have different maximum speed limits
"""class Vehicle:
    def max_speed(self):
        print("Maximum Speed: 80 km/h")
class SportsCar(Vehicle):
    def max_speed(self):
        print("Maximum Speed: 250 km/h")
print("Sports Car")
SportsCar().max_speed()
print("\nVehicle")
Vehicle().max_speed()"""

# problem statement 9 A company provides different bonus amounts based on employee roles
"""class Employee:
    def bonus(self):
        print("Bonus: ₹5000")
class Manager(Employee):
    def bonus(self):
        print("Bonus: ₹20000")
print("Manager")
Manager().bonus()
print("\nEmployee")
Employee().bonus()"""

# problem statement 10
"""class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")
class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")
print("Advanced Student")
AdvancedStudent().placement_status()
print("\nRegular Student")
Student().placement_status()"""

# problem statement 11 Corporate cafeteria meal management system
"""class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.ordered_items = []
    def add_food_item(self, item):
        self.ordered_items.append(item)
    def calculate_total(self):
        total = 0
        for item in self.ordered_items:
            total += item.price
        return total
    def generate_bill(self, employee):
        print("=" * 50)
        print("            CORPORATE CAFETERIA BILL")
        print("=" * 50)
        print()
        print("Employee ID     :", employee.employee_id)
        print("Employee Name   :", employee.employee_name)
        print()
        print("-" * 50)
        print("{:<25} {}".format("Item", "Price"))
        print("-" * 50)
        for item in self.ordered_items:
            print("{:<25} {}rupees".format(item.item_name, item.price))
        print("-" * 50)
        print("\nTotal Amount                 {}rupees".format(self.calculate_total()))
        print("\nPayment Status               PAID")
        print("\n" + "=" * 50)
# Test Case
employee = Employee("E101", "Ryan")
coffee = FoodItem("Coffee", 40)
sandwich = FoodItem("Sandwich", 80)
brownie = FoodItem("Brownie", 60)
order = Order("O101")
order.add_food_item(coffee)
order.add_food_item(sandwich)
order.add_food_item(brownie)
order.generate_bill(employee)"""

# problem statement 12 A multiplex wants to automate movie ticket booking.Customers can book multiple tickets for a movie,and the system should generate a booking receipt.
"""class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
class Booking:
    def __init__(self, customer, movie, number_of_tickets):
        self.customer = customer
        self.movie = movie
        self.number_of_tickets = number_of_tickets
    def calculate_amount(self):
        return self.movie.ticket_price * self.number_of_tickets
    def generate_receipt(self):
        print("=" * 50)
        print("            MOVIE BOOKING RECEIPT")
        print("=" * 50)
        print()
        print("Customer Name   :", self.customer.customer_name)
        print("Movie Name      :", self.movie.movie_name)
        print()
        print("Ticket Price    : {}rupees".format(self.movie.ticket_price))
        print("Tickets Booked  :", self.number_of_tickets)
        print()
        print("-" * 50)
        print()
        print("Total Amount    : {}rupees".format(self.calculate_amount()))
        print()
        print("Booking Status  : CONFIRMED")
        print()
        print("=" * 49)
# Test Case
customer = Customer("Babu")
movie = Movie("Avengers", 200)

booking = Booking(customer, movie, 4)
booking.generate_receipt()"""

# problem statement 13 A training institute wants to track student performance and determine placement eligibility.
class Student:
    def __init__(self, student_id, student_name, attendance, assessment_score):
        self.student_id = student_id
        self.student_name = student_name
        self.attendance = attendance
        self.assessment_score = assessment_score


class PlacementManager:
    def check_eligibility(self, student):
        return student.attendance >= 75 and student.assessment_score >= 60

    def generate_report(self, student):
        status = "ELIGIBLE" if self.check_eligibility(student) else "NOT ELIGIBLE"

        print("=" * 50)
        print("          PLACEMENT ELIGIBILITY REPORT")
        print("=" * 50)
        print()
        print("Student ID       :", student.student_id)
        print("Student Name     :", student.student_name)
        print()
        print("Attendance       : {}%".format(student.attendance))
        print("Assessment Score : {}".format(student.assessment_score))
        print()
        print("Placement Status :", status)
        print()
        print("=" * 50)


# Test Case
student = Student("S101", "Ava", 85, 78)

manager = PlacementManager()
manager.generate_report(student)