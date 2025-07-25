# Write a class Train which has methods to book a ticket, get status 
# (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNO):
        self.trainNo = trainNO

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"Train no: {self.trainNo} is on time")

    def get_fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(999,5555)}")


t = Train(123)
t.book("Pune","Banglore")
t.status()
t.get_fare("Pune","Banglore")