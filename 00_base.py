import pandas
from datetime import date

race = 0

# Assign points for top 3 placements
POINTS_PER_PLACEMENT = {
    1:5,
    2:3,
    3:1,
}

# Calculate points based on the rider's placement
def calc_points(placing, POINTS_PER_PLACEMENT):
    if placing in POINTS_PER_PLACEMENT:
        return POINTS_PER_PLACEMENT[placing]
    return 0

# Gets user input and checks it is a listed answer
def valid_input(inp):
    while True:
        try:
            response = input(inp).lower()
            if response in POINTS_PER_PLACEMENT:
                return response
        except:
            print(
                f"Please enter a valid response, such as 1, 2 etc."
            )

# Gets valid integer from user
def valid_integer(inp):
    while True:
        try:
            integer = int(input(inp))
            return integer
        except:
            print("Invalid integer entered.")

# Gets valid integer with parameters 0-50
def valid_integer_paramters(inp,min,max):
    while True:
        try:
            integer = int(input(inp))
            return integer
        except:
            print("Invalid integer entered.")

# Gets rider's name, placing and points for each race and returns in dictionary
def get_rider_info(races):

    total_points = 0
    rider_dictionary = {}
    rider_dictionary["Name"] = input("Enter rider name: ")

    # Get race information (placing, points)
    for i_ in range(races):
        placing = valid_integer("Enter race placement, or enter 0 if not applicable: ")
        rider_dictionary["Race"] = placing
        if placing in POINTS_PER_PLACEMENT:
            total_points = POINTS_PER_PLACEMENT[placing]
        break

    # Add point tally to dictionary
    rider_dictionary["Calculated Tally"] = total_points
    
    return rider_dictionary

def printing(team, races):
    
    heading = f"TEAM {team}"
    # Convert to dataframe
    race_data_frame = pandas.DataFrame.from_records(races)
    race_data_frame = race_data_frame.set_index(
        race_data_frame.columns[0]
    )
    # Makes dataframe string for printing
    race_string = race_data_frame.to_string()
    
    return [heading, race_string]

# Get initial data
riders = valid_integer("Enter the number of riders in the team: ")
races = valid_integer("Enter the number of races the team will compete in: ")

# Main loop
while True:
    # Get team name, exit program if 'X' entered
    team = input("Enter team name or 'X' to exit: ")
    if team == "X":
        break
    rider_info = []
    # Get rider information
    for rider_index in range(riders):
        rider_info.append(get_rider_info(races))

    print = printing(team, rider_info)

    # Get date for fomatting
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    # Write to file & print to console
    filename = f"{team}_{day}_{month}_{year}.txt"
    text_file = open(filename, "w")
    for element in printing:
        print(element)
        text_file.write(element)
        text_file.write("\n")
    text_file.close()

print("Text file with information has been created.")