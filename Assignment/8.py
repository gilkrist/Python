#4. Movie Ticket Booking System Check showtimes, book tickets, select
# seats, and print confirmation.
class Movie:
    def __init__(self, name, showtime, seats):
        self.name = name
        self.showtime = showtime
        self.available_seats = seats

    def book_ticket(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print("Booking confirmed for", seats, "seats")
        else:
            print("Not enough seats available")

    def show_details(self):
        print("Movie:", self.name)
        print("Showtime:", self.showtime)
        print("Available seats:", self.available_seats)