class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        s = self.second + other.second
        m = self.minute + other.minute
        h = self.hour + other.hour

        # Adjust seconds
        if s >= 60:
            m += s // 60
            s = s % 60

        # Adjust minutes
        if m >= 60:
            h += m // 60
            m = m % 60

        return Time(h, m, s)

    def display(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")


t1 = Time(2, 45, 50)
t2 = Time(1, 30, 30)

t3 = t1 + t2
t3.display()
