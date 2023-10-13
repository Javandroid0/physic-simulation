import math


def electric_field_of_disk(R, d, sigma, x, y, z):
    epsilon_0 = 8.854e-12  # Vacuum permittivity constant in F/m (farads per meter)

    # Calculate distance from the disk center to the point
    distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)

    # Check if the point is at the disk's location
    if distance == 0:
        return (0, 0, 0)

    # Calculate electric field components due to the disk
    if distance >= d:
        cos_theta = z / distance  # Cosine of the angle between z-axis and the point
        area = math.pi * R ** 2  # Area of the disk
        dQ = sigma * area  # Charge on the disk

        # Electric field components
        E_magnitude = 1 / (4 * math.pi * epsilon_0) * dQ / distance ** 2
        Ex = E_magnitude * cos_theta * x / distance
        Ey = E_magnitude * cos_theta * y / distance
        Ez = E_magnitude * cos_theta * z / distance

        return (Ex, Ey, Ez)
    else:
        # Point is inside the disk, electric field is undefined
        return None


# Example usage
R = 1.0  # Radius of the disk
d = 2.0  # Distance from the point to the center of the disk
sigma = 1.0  # Charge density of the disk in C/m^2

x = 1.0  # x-coordinate of the point
y = 1.0  # y-coordinate of the point
z = 2000.0  # z-coordinate of the point

# Calculate electric field components
result = electric_field_of_disk(R, d, sigma, x, y, z)

# Print the result
if result:
    Ex, Ey, Ez = result
    print(f"Electric Field at point ({x}, {y}, {z}):")
    print(f"Ex = {Ex} N/C")
    print(f"Ey = {Ey} N/C")
    print(f"Ez = {Ez} N/C")
else:
    print("Point is inside the disk. Electric field is undefined.")
