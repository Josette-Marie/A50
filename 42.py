# Intersecting the raduis of two circles

import math

def circles_intersect(c1_x, c1_y, c1_radius, c2_x, c2_y, c2_radius):
  # Calculate the distance between the centers
  center_distance = math.sqrt((c2_x - c1_x)**2 + (c2_y - c1_y)**2)

  # Check for intersection conditions based on distance and radii
  if center_distance <= abs(c1_radius - c2_radius):
    # One circle is entirely within the other
    return True
  elif center_distance <= c1_radius + c2_radius:
    # Circles overlap
    return True
  else:
    # Circles are separate
    return False

# Sample Examle 
circle1 = (1, 2, 3)
circle2 = (4, 5, 2)

intersection_result = circles_intersect(*circle1, *circle2)  # Unpack coordinates

print(f"Circles intersect? {intersection_result}")
