# prg 1 airport check in management

class Passenger:
    def __init__(self, name):
        self.passenger_name = name
class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number
class BoardingPass:
    def __init__(self, passenger, flight, seat_number):
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number
        self.status = "CHECK-IN COMPLETE"
    def generate_boarding_pass(self):
        print("=" * 50)
        print("               BOARDING PASS")
        print("=" * 50)
        print()
        print(f"Passenger Name : {self.passenger.passenger_name}")
        print(f"Flight Number  : {self.flight.flight_number}")
        print(f"Seat Number    : {self.seat_number}")
        print()
        print(f"Status         : {self.status}")
        print()
        print("=" * 50)
class Airport:
    def __init__(self):
        self.passengers = []
        self.occupied_seats = set()
    def register_passenger(self, passenger):
        self.passengers.append(passenger)
    def assign_seat(self, seat_number):
        if seat_number in self.occupied_seats:
            return False
        self.occupied_seats.add(seat_number)
        return True
    def generate_boarding_pass(self, passenger, flight, seat_number):
        if self.assign_seat(seat_number):
            boarding_pass = BoardingPass(passenger, flight, seat_number)
            boarding_pass.generate_boarding_pass()
        else:
            print("Seat already occupied!")
airport = Airport()
passenger = Passenger("Mason")
flight = Flight("AI202")
airport.register_passenger(passenger)
airport.generate_boarding_pass(passenger, flight, "12A")

# prg 2 Smart Parking Management System
class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
class ParkingSlot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.is_occupied = False
class ParkingManager:
    def __init__(self, rate_per_hour):
        self.rate_per_hour = rate_per_hour
        self.vehicles = []
    def park_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def calculate_fee(self, hours_parked):
        return hours_parked * self.rate_per_hour
    def generate_receipt(self, vehicle, hours_parked):
        fee = self.calculate_fee(hours_parked)
        print("=" * 50)
        print("              PARKING RECEIPT")
        print("=" * 50)
        print()
        print(f"Vehicle Number : {vehicle.vehicle_number}")
        print(f"Hours Parked   : {hours_parked}")
        print()
        print(f"Parking Fee    : rs{fee}")
        print()
        print("=" * 50)
vehicle = Vehicle("AP39AB1234")
manager = ParkingManager(30)
manager.park_vehicle(vehicle)
manager.generate_receipt(vehicle, 5)

# prg 3 Cricket Tournament Score Tracker
class Player:
    def __init__(self, player_name):
        self.player_name = player_name
class Match:
    def __init__(self, runs):
        self.runs = runs
class Tournament:
    def __init__(self, player):
        self.player = player
        self.matches = []
    def add_match(self, match):
        self.matches.append(match)
    def calculate_total_runs(self):
        return sum(match.runs for match in self.matches)
    def calculate_average_runs(self):
        if len(self.matches) == 0:
            return 0
        return self.calculate_total_runs() / len(self.matches)
    def generate_report(self):
        total_runs = self.calculate_total_runs()
        matches_played = len(self.matches)
        average_runs = self.calculate_average_runs()
        print("=" * 50)
        print("             PLAYER PERFORMANCE REPORT")
        print("=" * 50)
        print()
        print(f"Player Name    : {self.player.player_name}")
        print()
        print(f"Total Runs     : {total_runs}")
        print(f"Matches Played : {matches_played}")
        print(f"Average Runs   : {average_runs}")
        print()
        print("=" * 50)
player = Player("Arjun")
tournament = Tournament(player)
tournament.add_match(Match(50))
tournament.add_match(Match(75))
tournament.add_match(Match(100))
tournament.generate_report()

# prg 4 Hotel Room Reservation System
class Guest:
    def __init__(self, guest_name):
        self.guest_name = guest_name
class Room:
    def __init__(self, room_type, room_rate):
        self.room_type = room_type
        self.room_rate = room_rate
class Reservation:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.nights = nights
        self.room = room
    def calculate_amount(self):
        return self.room.room_rate * self.nights
    def generate_invoice(self):
        print("=" * 50)
        print("              HOTEL INVOICE")
        print("=" * 50)
        print()
        print(f"Guest Name     : {self.guest.guest_name}")
        print(f"Room Type      : {self.room.room_type}")
        print()
        print(f"Nights Stayed  : {self.nights}")
        print()
        print(f"Total Amount   : rs{self.calculate_amount()}")
        print()
        print("=" * 50)
guest = Guest("Sophia")
room = Room("Deluxe", 3500)
reservation = Reservation(guest, room, 3)
reservation.generate_invoice()

# prg 5 Mobile Recharge Management System
class Customer:
    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
class RechargePlan:
    def __init__(self, plan_name, amount):
        self.plan_name = plan_name
        self.amount = amount
class Recharge:
    def __init__(self, customer):
        self.customer = customer
        self.selected_plan = None
    def select_plan(self, plan):
        self.selected_plan = plan
    def generate_receipt(self):
        print("=" * 50)
        print("             RECHARGE RECEIPT")
        print("=" * 50)
        print()
        print(f"Customer Name : {self.customer.customer_name}")
        print()
        print(f"Plan Selected : {self.selected_plan.plan_name}")
        print()
        print(f"Amount Paid   : rs{self.selected_plan.amount}")
        print()
        print("Status        : SUCCESSFUL")
        print()
        print("=" * 50)
customer = Customer("Logan", "9876543210")
plan = RechargePlan("Unlimited 84 Days", 799)
recharge = Recharge(customer)
recharge.select_plan(plan)
recharge.generate_receipt()

# prg 6 Freelance Project Billing System
class Client:
    def __init__(self, client_name):
        self.client_name = client_name
class Project:
    def __init__(self, project_name, hours_worked, hourly_rate):
        self.project_name = project_name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
class Invoice:
    def __init__(self, client, project):
        self.client = client
        self.project = project
    def calculate_amount(self):
        return self.project.hours_worked * self.project.hourly_rate
    def generate_invoice(self):
        print("=" * 50)
        print("                CLIENT INVOICE")
        print("=" * 50)
        print()
        print(f"Client Name    : {self.client.client_name}")
        print(f"Project Name   : {self.project.project_name}")
        print()
        print(f"Hours Worked   : {self.project.hours_worked}")
        print(f"Hourly Rate    : rs{self.project.hourly_rate}")
        print()
        print(f"Invoice Amount : rs{self.calculate_amount()}")
        print()
        print("=" * 50)
client = Client("Olivia")
project = Project(
    "Portfolio Website",20,1000)
invoice = Invoice(client, project)
invoice.generate_invoice()

# prg 7 Pet Care Center Management System
class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name
class Pet:
    def __init__(self, pet_name):
        self.pet_name = pet_name
class Appointment:
    appointments = []
    def __init__(self, owner, pet, service, charge):
        self.owner = owner
        self.pet = pet
        self.service = service
        self.charge = charge
    def book_appointment(self):
        Appointment.appointments.append(self)
    def generate_receipt(self):
        print("=" * 50)
        print("            SERVICE RECEIPT")
        print("=" * 50)
        print()
        print(f"Owner Name : {self.owner.owner_name}")
        print(f"Pet Name   : {self.pet.pet_name}")
        print()
        print(f"Service    : {self.service}")
        print()
        print(f"Amount     : rs{self.charge}")
        print()
        print("=" * 50)
owner = Owner("Ethan")
pet = Pet("Bruno")
appointment = Appointment(owner, pet, "Grooming", 800)
appointment.book_appointment()
appointment.generate_receipt()

# prg 8 Online Gaming Tournament System
class Player:
    def __init__(self, player_name):
        self.player_name = player_name
class Match:
    def __init__(self, score):
        self.score = score
class Tournament:
    def __init__(self, player):
        self.player = player
        self.matches = []
    def add_match(self, match):
        self.matches.append(match)
    def calculate_final_score(self):
        return sum(match.score for match in self.matches)
    def get_rank_status(self):
        final_score = self.calculate_final_score()
        return "QUALIFIED" if final_score >= 400 else "NOT QUALIFIED"
    def generate_report(self):
        print("=" * 50)
        print("            TOURNAMENT REPORT")
        print("=" * 50)
        print()
        print(f"Player Name : {self.player.player_name}")
        print()
        print(f"Final Score : {self.calculate_final_score()}")
        print()
        print(f"Rank Status : {self.get_rank_status()}")
        print()
        print("=" * 50)
player = Player("Leo")
tournament = Tournament(player)
tournament.add_match(Match(100))
tournament.add_match(Match(150))
tournament.add_match(Match(200))
tournament.generate_report()

# prg 9 Gym Membership Management System
class Member:
    def __init__(self, member_name):
        self.member_name = member_name
class MembershipPlan:
    def __init__(self, plan_name, monthly_fee):
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
class Gym:
    def __init__(self, member, plan, duration):
        self.member = member
        self.plan = plan
        self.duration = duration  
    def calculate_fee(self):
        return self.plan.monthly_fee * self.duration
    def generate_receipt(self):
        print("=" * 50)
        print("             MEMBERSHIP RECEIPT")
        print("=" * 50)
        print()
        print(f"Member Name : {self.member.member_name}")
        print()
        print(f"Plan        : {self.plan.plan_name}")
        print()
        print(f"Duration    : {self.duration} Months")
        print()
        print(f"Total Fee   : rs{self.calculate_fee()}")
        print()
        print("=" * 50)
member = Member("Ava")
plan = MembershipPlan("Premium", 2000)
gym = Gym(member, plan, 6)
gym.generate_receipt()

# prg 10 Digital Wallet Transaction System
class User:
    def __init__(self, user_name):
        self.user_name = user_name
class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
class Wallet:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance
        self.transactions = []  
    def add_money(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("ADD MONEY", amount))
    def transfer_money(self, amount):
        if amount <= self.balance:
            opening_balance = self.balance
            self.balance -= amount
            self.transactions.append(Transaction("TRANSFER", amount))
            return opening_balance, True
        return self.balance, False
    def show_balance(self):
        return self.balance
    def generate_receipt(self, opening_balance, transfer_amount, status):
        print("=" * 50)
        print("          TRANSACTION RECEIPT")
        print("=" * 50)
        print()
        print(f"User Name       : {self.user.user_name}")
        print()
        print(f"Opening Balance : rs{opening_balance}")
        print()
        print(f"Transfer Amount : rs{transfer_amount}")
        print()
        print(f"Current Balance : rs{self.balance}")
        print()
        print(f"Status          : {status}")
        print()
        print("=" * 50)
user = User("Noah")
wallet = Wallet(user, 10000)
opening_balance, success = wallet.transfer_money(2500)
status = "SUCCESSFUL" if success else "FAILED"
wallet.generate_receipt(opening_balance,2500,status)