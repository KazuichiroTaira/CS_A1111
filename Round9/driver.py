class Driver:

    NUMBER_OF_LAPS = 5
    LAPS_NOT_YET_DRIVEN = 10000000

    def __init__(self, driver_name, team_name):
        self.__name = driver_name
        self.__team = team_name
        self.__lap_times = []

    def get_name(self):
        return self.__name

    def get_team(self):
        return self.__team

    def time_string_to_centiseconds(self, time_string):
        minutes, seconds, hundredths = time_string.split(":")
        total = int(hundredths) \
            + int(seconds) * 100 \
            + int(minutes) * 60 * 100
        return total

    def centiseconds_to_time_string(self, time_in_centiseconds):
        minutes = time_in_centiseconds // (60*100)
        remaining = time_in_centiseconds - minutes*(60*100)
        seconds = remaining // 100
        remaining -= seconds*100
        hundredths = remaining
        return f"{minutes}:{seconds:02d}:{hundredths:02d}"

    def record_lap_time(self, lap_time):
        if len(self.__lap_times) >= self.NUMBER_OF_LAPS:
            return False

        lap_time = self.time_string_to_centiseconds(lap_time)
        self.__lap_times.append(lap_time)
        return True

    def overwrite_lap_time(self, lap_number, new_lap_time):
        try:
            self.__lap_times[lap_number-1] = \
                self.time_string_to_centiseconds(new_lap_time)
            return True
        except IndexError:
            return False

    def get_best_lap_time(self):
        try:
            return min(self.__lap_times)
        except ValueError:
            return Driver.LAPS_NOT_YET_DRIVEN

    def compare_best_lap_time(self, other_driver):
        best_other = other_driver.get_best_lap_time()
        best_self = self.get_best_lap_time()
        if best_self < best_other:
            return 1
        elif best_self > best_other:
            return -1
        else:
            return 0

    def __str__(self):
        info = f"{self.__name: <20} {self.__team: <15} "
        for lp in self.__lap_times:
            info += self.centiseconds_to_time_string(lp) + " "
        return info
