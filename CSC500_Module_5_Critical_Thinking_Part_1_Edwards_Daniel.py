rain_fall = [] # Empty list to store the amount of rain fall for each month of the year
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] # List of months

# Create a dictionary to store the amount of rain fall for each month of the year
for annual in range(1, 6):
    annual_rain_fall = {}
    for month in months:
        percipitation = float(input(f"How much rain was there for {month}? "))
        annual_rain_fall[month] = percipitation
    rain_fall.append(annual_rain_fall)

# Create a dictionary to store the amount of rain fall for each month of the year    
for key, value in annual_rain_fall.items():
    if value <= 1:
        print(f"{key}: {value} inch")
    else:
        print(f"{key}: {value} inches")

# Calculate the total and average rain fall for the year
total_rain_fall = sum(annual_rain_fall.values())
average_rain_fall = total_rain_fall / len(annual_rain_fall)

# Format the total and average rain fall to two decimal places
formatted_total_rain_fall = "{:.2f}".format(total_rain_fall)
formatted_average_rain_fall = "{:.2f}".format(average_rain_fall)

# If "value" is less then or equal to 1 print formatted total & average rain fall in inches / inch
if value <= 1:
    print(f"\nThe total rain fall for the year was {formatted_total_rain_fall} inches")
    print(f"The average rain fall for the year was {formatted_average_rain_fall} inch")
else:
    print(f"\nThe total rain fall for the year was {formatted_total_rain_fall} inches")
    print(f"The average rain fall for the year was {formatted_average_rain_fall} inches")