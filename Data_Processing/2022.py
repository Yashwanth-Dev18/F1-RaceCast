


def getCar(driver):
    if driver == "HAM" or driver == "RUS":
        return "W13 - 2022"
    elif driver == "LEC" or driver == "SAI":
        return "SF-75 - 2022"
    elif driver == "VER" or driver == "PER":
        return "RB18 - 2022"
    elif driver == "ALB" or driver == "LAT":
        return "FW44 - 2022"
    elif driver == "NOR" or driver == "RIC":
        return "MCL36 - 2022"
    elif driver == "TSU" or driver == "GAS":
        return "AT03 - 2022"
    elif driver == "HUL" or driver == "STR" or driver == "VET":
        return "AMR22 - 2022"
    elif driver == "BOT" or driver == "ZHO":
        return "C42 - 2022"
    elif driver == "MAG" or driver == "SCH":
        return "VF-22 - 2022"
    elif driver == "ALO" or driver == "OCO":
        return "A522 - 2022"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"


races = [['LEC', 'SAI', 'HAM', 'RUS', 'MAG', 'BOT', 'OCO', 'TSU', 'ALO', 'ZHO', 'SCH', 'STR', 'ALB', 'RIC', 'NOR', 'LAT', 'HUL', 'PER', 'VER', 'GAS'], # Bahrain
         ['VER', 'LEC', 'SAI', 'PER', 'RUS', 'OCO', 'NOR', 'GAS', 'MAG', 'HAM', 'ZHO', 'HUL', 'STR', 'ALB', 'BOT', 'ALO', 'RIC', 'LAT', 'TSU', 'SCH'], # Saudi Arabia
         ['LEC', 'PER', 'RUS', 'HAM', 'NOR', 'RIC', 'OCO', 'BOT', 'GAS', 'ALB', 'ZHO', 'STR', 'SCH', 'MAG', 'TSU', 'LAT', 'ALO', 'VER', 'VET', 'SAI'], # Australia
         ['VER', 'PER', 'NOR', 'RUS', 'BOT', 'LEC', 'TSU', 'VET', 'MAG', 'STR', 'ALB', 'GAS', 'HAM', 'OCO', 'ZHO', 'LAT', 'SCH', 'RIC', 'ALO', 'SAI'], # Imola
         ['VER', 'LEC', 'SAI', 'PER', 'RUS', 'HAM', 'BOT', 'OCO', 'ALB', 'STR', 'ALO', 'TSU', 'RIC', 'LAT', 'SCH', 'MAG', 'VET', 'GAS', 'NOR', 'ZHO'], # Miami
         ['VER', 'PER', 'RUS', 'SAI', 'HAM', 'BOT', 'OCO', 'NOR', 'ALO', 'TSU', 'VET', 'RIC', 'GAS', 'SCH', 'STR', 'LAT', 'MAG', 'ALB', 'ZHO', 'LEC'], # Spain
         ['PER', 'SAI', 'VER', 'LEC', 'RUS', 'NOR', 'ALO', 'HAM', 'BOT', 'VET', 'GAS', 'OCO', 'RIC', 'STR', 'LAT', 'ZHO', 'TSU', 'ALB', 'SCH', 'MAG'], # Monaco
         ['VER', 'PER', 'RUS', 'HAM', 'GAS', 'VET', 'ALO', 'RIC', 'NOR', 'OCO', 'BOT', 'ALB', 'TSU', 'SCH', 'LAT', 'STR', 'MAG', 'ZHO', 'LEC', 'SAI'], # Azerbaijan
         ['VER', 'SAI', 'HAM', 'RUS', 'LEC', 'OCO', 'BOT', 'ZHO', 'ALO', 'STR', 'RIC', 'VET', 'ALB', 'GAS', 'NOR', 'LAT', 'MAG', 'TSU', 'SCH', 'PER'], # Canada
         ['SAI', 'PER', 'HAM', 'LEC', 'ALO', 'NOR', 'VER', 'SCH', 'VET', 'MAG', 'STR', 'LAT', 'RIC', 'TSU', 'OCO', 'GAS', 'BOT', 'RUS', 'ZHO', 'ALB'], # Silverstone
         ['LEC', 'VER', 'HAM', 'RUS', 'OCO', 'SCH', 'NOR', 'MAG', 'RIC', 'ALO', 'BOT', 'ALB', 'STR', 'ZHO', 'GAS', 'TSU', 'VET', 'SAI', 'LAT', 'PER'], # Austria
         ['VER', 'HAM', 'RUS', 'PER', 'SAI', 'ALO', 'NOR', 'OCO', 'RIC', 'STR', 'VET', 'GAS', 'ALB', 'BOT', 'SCH', 'ZHO', 'LAT', 'MAG', 'TSU', 'LEC'], # France
         ['VER', 'HAM', 'RUS', 'SAI', 'PER', 'LEC', 'NOR', 'ALO', 'OCO', 'VET', 'STR', 'GAS', 'ZHO', 'SCH', 'RIC', 'MAG', 'ALB', 'LAT', 'TSU', 'BOT'], # Hungary
         ['VER', 'PER', 'SAI', 'RUS', 'ALO', 'LEC', 'OCO', 'VET', 'GAS', 'ALB', 'STR', 'NOR', 'TSU', 'ZHO', 'RIC', 'MAG', 'SCH', 'LAT', 'BOT', 'HAM'], # Belgium
         ['VER', 'RUS', 'LEC', 'HAM', 'PER', 'ALO', 'NOR', 'SAI', 'OCO', 'STR', 'GAS', 'ALB', 'SCH', 'VET', 'MAG', 'ZHO', 'RIC', 'LAT', 'BOT', 'TSU'], # Netherlands
         ['VER', 'LEC', 'RUS', 'SAI', 'HAM', 'PER', 'NOR', 'GAS', 'ZHO', 'OCO', 'SCH', 'BOT', 'TSU', 'LAT', 'MAG', 'RIC', 'STR', 'ALO', 'VET'],        # Monza
         ['PER', 'LEC', 'SAI', 'NOR', 'RIC', 'STR', 'VER', 'VET', 'HAM', 'GAS', 'BOT', 'MAG', 'SCH', 'RUS', 'TSU', 'OCO', 'ALB', 'ALO', 'LAT', 'ZHO'], # Singapore
         ['VER', 'PER', 'LEC', 'OCO', 'HAM', 'VET', 'ALO', 'RUS', 'LAT', 'NOR', 'RIC', 'STR', 'TSU', 'MAG', 'BOT', 'ZHO', 'GAS', 'SCH', 'SAI', 'ALB'], # Japan
         ['VER', 'HAM', 'LEC', 'PER', 'RUS', 'NOR', 'ALO', 'VET', 'MAG', 'TSU', 'OCO', 'ZHO', 'ALB', 'GAS', 'SCH', 'RIC', 'LAT', 'STR', 'BOT', 'SAI'], # Austin
         ['VER', 'HAM', 'PER', 'RUS', 'SAI', 'LEC', 'RIC', 'OCO', 'NOR', 'BOT', 'GAS', 'ALB', 'ZHO', 'VET', 'STR', 'SCH', 'MAG', 'LAT', 'ALO', 'TSU'], # Mexico
         ['RUS', 'HAM', 'SAI', 'LEC', 'ALO', 'VER', 'PER', 'OCO', 'BOT', 'STR', 'VET', 'ZHO', 'SCH', 'GAS', 'ALB', 'LAT', 'TSU', 'NOR', 'MAG', 'RIC'], # Brazil
         ['VER', 'LEC', 'PER', 'SAI', 'RUS', 'NOR', 'OCO', 'STR', 'RIC', 'VET', 'TSU', 'ZHO', 'ALB', 'GAS', 'BOT', 'SCH', 'MAG', 'HAM', 'LAT', 'ALO'] # Abu Dhabi
          ]


tracks = ["sakhir", "jeddah", "melbourne", "Imola", "Miami", "Barcelona", "Monaco", "Baku", "Canada",
          "Silverstone", "austria", "France", "Hungaroring", "Belgium", "Zandvoort", "Monza", "Singapore", "Suzuka", "Austin",
          "Mexico", "brazil", "Yas Marina"]


weather_conditions = [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1] 