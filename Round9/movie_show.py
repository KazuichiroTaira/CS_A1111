class MovieShow:
    MIN = 3
    NOT_AVAILABLE = (-1, -1)

    def __init__(self,  title, showtime, auditorium, rows, seats_in_row):
        self.__movie = title
        self.__time = showtime
        self.__theater = auditorium
        self.__seats = [[False for _ in range(max(3, seats_in_row))]
                        for _ in range(max(3, rows))]

    def get_movie(self):
        return self.__movie

    def get_time(self):
        return self.__time

    def get_theater(self):
        return self.__theater

    def reserve_seat(self, row, seat):

        if 1 <= row <= len(self.__seats) \
                and 1 <= seat <= len(self.__seats[0]):
            pass
        else:
            return False

        row_idx = row - 1
        seat_idx = seat - 1

        if self.__seats[row_idx][seat_idx]:
            return False
        else:
            self.__seats[row_idx][seat_idx] = True
            return True

    def reserve_seats(self, row, first, last):
        error = False
        booked_list = []
        for i in range(first, last+1):
            booked = self.reserve_seat(row, i)
            if not booked:
                error = True
                break
            else:
                booked_list.append((row, i))
        if error is False:
            return True
        else:
            for row, seat in booked_list:
                try:
                    row_idx = row - 1
                    seat_idx = seat - 1
                    self.__seats[row_idx][seat_idx] = False
                except IndexError:
                    pass
            return False

    def find_available_seats(self, number):

        for i in range(len(self.__seats)-1, -1, -1):
            n = 0
            start = -1
            for j in range(len(self.__seats[i])):
                if self.__seats[i][j] is False:
                    if n == 0:
                        start = j
                    n += 1
                    if n == number:
                        row = i + 1
                        seat = start + 1
                        return row, seat
                else:
                    n = 0
        return MovieShow.NOT_AVAILABLE

    def get_reservation_map(self):
        info = ""
        for i in range(len(self.__seats)-1, -1, -1):
            row = i + 1
            info_row = f"{row: >02d}:"
            for j in range(len(self.__seats[i])):
                if self.__seats[i][j] is False:
                    info_row += "-"
                else:
                    info_row += "X"

            if info != "":
                info += "\n"
            info += info_row
        return info

    def seats_total(self):
        return len(self.__seats) * len(self.__seats[0])

    def total_reserved(self):
        n = 0
        for r in self.__seats:
            for s in r:
                n += int(s)
        return n

    def __str__(self):
        return f"{self.__time} {self.__movie} {self.__theater} " \
               f"reserved {self.total_reserved()}/{self.seats_total()}"
