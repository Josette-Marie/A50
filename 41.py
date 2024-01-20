# Find distance between two points (x,y)
import math

def distance(x1, y1, x2, y2):
  # Calculate the difference in coordinates
  dx = x2 - x1
  dy = y2 - y1

  # Apply the Pythagorean theorem to find the distance
  distance = math.sqrt(dx**2 + dy**2)

  return distance


# Sample Example
point1 = (1, 2)
point2 = (4, 5)

distance_result = distance(*point1, *point2)  # Unpack the coordinates from the tuples

print(f"The distance between points {point1} and {point2} is: {distance_result}")
