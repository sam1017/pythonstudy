class seat():
    def __init__(self , x, y):
        self.x = x
        self.y = y

    def is_seat_valid(self):
        if self.x < 9 and self.x > 0 and self.y < 9 and self.y > 0:
            return True
        else:
            return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")

valid_seats = [ seat(1,1),seat(1,2),seat(1,4),seat(1,5),seat(1,6),seat(1,8),
                seat(2,1),seat(2,2),seat(2,4),seat(2,5),seat(2,6),seat(2,8),
                seat(3,1),seat(3,2),seat(3,3),seat(3,4),seat(3,7),seat(3,8),
                seat(4,1),seat(4,5),seat(4,6),seat(4,7),seat(4,8),
                seat(5,1),seat(5,2),seat(5,3),seat(5,5),seat(5,6),seat(5,7),seat(5,8),
                seat(6,1),seat(6,3),seat(6,4),seat(6,5),seat(6,7),seat(6,8),
                seat(7,1),seat(7,5),seat(7,8),
                seat(8,2),seat(8,3),seat(8,4),seat(8,5),seat(8,6),seat(8,7),seat(8,8)]

def check_if_contain(seat_step, valid_seats):
    for valid_seat in valid_seats:
        if seat_step.get_x() == valid_seat.get_x() and seat_step.get_y() == valid_seat.get_y():
            return True
    return False

def seat_add(start, step):
    return seat(start.get_x()+ step.get_x(), start.get_y() + step.get_y())

def new_step_seat(valid_seats, searched_seats, start, seat_steps):
    for seat_step in seat_steps:
        new_seat = seat_add(start, seat_step)
        if check_if_contain(new_seat, valid_seats):
            if check_if_contain(new_seat, searched_seats) == False:
                return new_seat
    return None

def mazepath(valid_seats,start,end):
    solution_path = []
    searched_seats = []
    solution_path.append(start)
    searched_seats.insert(0, start)
    seat_steps = [seat(0,1),seat(1,0),seat(0,-1),seat(-1,0)]
    while check_if_contain(end, solution_path) == False and len(solution_path) > 0:
        start_seat = solution_path[-1]
        #start_seat.show()
        new_start_seat = new_step_seat(valid_seats, searched_seats, start_seat, seat_steps)
        if  new_start_seat!= None:
            print("new_start_seat ( " + str(new_start_seat.get_x())+ "," + str(new_start_seat.get_y())+ ")")
            solution_path.append(new_start_seat)
            searched_seats.insert(0, new_start_seat)
        else:
            seat_pop = solution_path.pop()
            print("solution_path.pop() ( " + str(seat_pop.get_x())+ "," + str(seat_pop.get_y())+ ")")
    return solution_path


start = seat(1,1)
end = seat(8,8)
mazepaths = mazepath(valid_seats, start, end)
for mazepath in mazepaths:
    mazepath.show()
