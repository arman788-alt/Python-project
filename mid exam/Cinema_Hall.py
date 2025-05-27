
# from chatgpt
class Star_Cinema:
    __hall_list = []  # private class attribute

    @classmethod
    def entry_hall(cls, hall_obj):
        cls.__hall_list.append(hall_obj)

    @classmethod
    def get_halls(cls):
        return cls.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)  # insert hall into Star_Cinema's hall list
        self.__seats = {}  # private
        self.__show_list = []  # private
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Invalid seat position ({row}, {col})!")
            elif self.__seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) already booked!")
            else:
                self.__seats[show_id][row][col] = 1
                print(f" Seat ({row}, {col}) booked successfully!")

    def view_show_list(self):
        print("\nRunning Shows:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        print(f"\nAvailable seats for show ID {show_id}:")
        for i in range(self.__rows):  
            for j in range(self.__cols):
                if self.__seats[show_id][i][j] == 0:
                    

                    print(f"({i},{j})", end=" ")
            print()


# Sample usage
# if __name__ == '__main__':
hall1 = Hall(5, 5, 101)
hall1.entry_show("111", "Avengers", "12:00 PM")
hall1.entry_show("222", "Inception", "3:00 PM")

while True:
        
        print("\nStar Cinema System")
        print("1. View all shows")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            hall1.view_show_list()

        elif choice == '2':
            show_id = input("Enter show ID: ")
            hall1.view_available_seats(show_id)

        elif choice == '3':
            show_id = input("Enter show ID: ")
            n = int(input("How many seats to book? "))
            seats_to_book = []
            for _ in range(n):
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")




