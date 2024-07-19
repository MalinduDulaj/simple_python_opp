class Duration:
    def __init__(self, hours, minutes):
      self.hours = hours
      self.minutes = minutes

    def __add__(self,other):
      if isinstance(other, Duration):
          total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
          new_hours = total_minutes // 60
          new_minutes = total_minutes % 60
          return Duration(new_hours,new_minutes)
      else:
        raise ValueError("Unsuppored operand type for +. You can only add two Duration objects. ")
      
    def __It__(self, other):
      if isinstance(other, Duration):
        return self.hours > other.hours
      else:
        raise ValueError("Can't compare")
      

    def __str__(self):
      return f"{self.hours} hours, {self.minutes} minutes"

# Creating Duration Instances
duration1 = Duration(2,30)
duration2 = Duration(1,45)

# Adding Durations using the + operator
total_duration = duration1 + duration2

# Displaying the result
print("Duration 1:",duration1)
print("Duration 2:",duration2)

print("Total Duration:",total_duration)
