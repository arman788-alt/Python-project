class star_cinema:
    hall_list = []


    def entry_hall(self,row,col,hall_no):
        hall = Hall(row,col,hall_no)
        self.hall_list.append(hall)
        print(f"{hall_no} Hall No successfully added in start_cinema")




class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self,id, movie_name, time):
        show_info = (id,movie_name,time)
        self.show_list.append(show_info)
        seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]   
        self.seats[id] = seat
        print(f"{movie_name} movie is added in this hall")



    def book_seats(self,id,seat_list):
     
     if id not in self.seats:
         print(f"Sorry {id} id is wrong")
         return
     else:
         for row,col in seat_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print("Invalid seat position")
                return
            elif self.seats[id][row][col] == 1:
                print(f"({row}{col})seat already booked!!")
                return
            elif self.seats[id][row][col] == 0:
                self.seats[id][row][col] = 1
                print(f"this seat {row}{col} booked successfully!!")


    def view_show_list(self):

        if not self.show_list:
            print("No show available rigit now")
            return
        else:
             print("Running show")
             print(f"ID\tMovie_Name\tTime")
             for show in self.show_list:
                print(f"{show[0]}\t{show[1]}\t{show[2]}")

    

    def  view_available_seats(self,id):
         if id not in self.seats:
             print("Invalid Id")
             return
         
         print(f"Available seat for show Id{id}")
         for row in range(self.rows):
             for col in range(self.cols):
                 if self.seats[id][row][col] == 0:
                     print(f"({row}{col}) is Available")
   


    
        
Cineplax = star_cinema()
Cineplax.entry_hall(1,2,100)
hall1 = Hall(2,3,100)



while True:
    print("Star Cinema System!!")
    print("1.View All shows")
    print("2.Entry show in the Hall")
    print("3.View available seats")
    print("4.Booking seat")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hall1.view_show_list()

    
    elif choice == 2:
        id = (input("Enter show ID: "))
        movie_name = input("Enter movie name: ")
        time = input("Enter Time: ")
        hall1.entry_show(id,movie_name,time)

    elif choice == 3:
        id = (input("Enter show ID: "))
        hall1.view_available_seats(id)
    
    elif choice == 4:
        id = (input("Enter show ID: "))
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        seat_list = []
        seat_list = [(row,col)]
        hall1.book_seats(id,seat_list)
    

    elif choice == 5:
        print("Thank you for using Star Cinema System!")
        break

    else:
        print("Invalid choice!")






    