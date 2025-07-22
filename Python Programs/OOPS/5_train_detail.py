import random
class Train:
    
    def book_train(self, trainno, frm, to):
        print("Ticket is booked. Train no. :", trainno, ",from :", frm, ",to :", to)

    def get_status(self, trainno):
        print("Train number", trainno, "is running on time.")

    def get_fare(self, trainno, frm, to):
        print("Ticket fare of train no.",trainno, "from", frm, "to", to, "is", random.randint(333,4444))
    
t=Train()
t.book_train(14569, "Delhi", "Pune")
t.get_status(14569)
t.get_fare(14569, "Delhi", "Pune")