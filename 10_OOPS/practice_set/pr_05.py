'''
Write a class Train which has a method to book a ticket, get status(no of seats) and 
get fare information of trains running under Indian Railways 
'''

class Train:
    
    def __init__(self, name, fare, seats) :
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("**************************")
        print(f"The name of the train is: {self.name}")
        print(f"The no of seats available are: {self.seats}")
        print("***************************\n")

    def getFare(self):
        print(f"The fare of the train is : {self.fare}\n")

    def bookTicket(self):

        if(self.seats>0):
            print(f"Your seat is confirmed and your seat number is: {self.seats}")
            self.seats= self.seats-1
        else:
            print("Seats are not available, Please try in tatkal")

    def cancelTicket(self, seatNo):
        pass


            
         
intercity=Train("Karnataka Express", 500, 100)
intercity.getStatus()
intercity.getFare()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(99)