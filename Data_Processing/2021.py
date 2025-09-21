



def getCar(driver):
    if driver == "HAM" or driver == "BOT":
        return "W12 - 2021"
    elif driver == "LEC" or driver == "SAI":
        return "SF21 - 2021"
    elif driver == "VER" or driver == "PER":
        return "RB16B - 2021"
    elif driver == "RUS" or driver == "LAT":
        return "FW43B - 2021"
    elif driver == "NOR" or driver == "RIC":
        return "MCL35M - 2021"
    elif driver == "TSU" or driver == "GAS":
        return "AT02 - 2021"
    elif driver == "STR" or driver == "VET":
        return "AMR21 - 2021"
    elif driver == "RAI":
        return "C41 - 2021"
    elif driver == "SCH":
        return "VF-21 - 2021"
    elif driver == "ALO" or driver == "OCO":
        return "A521 - 2021"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"


races = [['HAM', 'VER', 'BOT', 'NOR', 'PER', 'LEC', 'RIC', 'SAI', 'TSU', 'STR', 'RAI', 'OCO', 'RUS', 'VET', 'SCH', 'GAS', 'LAT', 'ALO'], # Bahrain
         ['VER', 'HAM', 'NOR', 'LEC', 'SAI', 'RIC', 'GAS', 'STR', 'OCO', 'ALO', 'PER', 'TSU', 'RAI', 'VET', 'SCH', 'BOT', 'RUS', 'LAT'], # Imola
         ['HAM', 'VER', 'BOT', 'PER', 'NOR', 'LEC', 'OCO', 'ALO', 'RIC', 'GAS', 'SAI', 'VET', 'STR', 'TSU', 'RUS', 'SCH', 'LAT', 'RAI'], # Portugal
         ['HAM', 'VER', 'BOT', 'LEC', 'PER', 'RIC', 'SAI', 'NOR', 'OCO', 'GAS', 'STR', 'RAI', 'VET', 'RUS', 'LAT', 'ALO', 'SCH', 'TSU'], # Spain
         ['VER', 'SAI', 'NOR', 'PER', 'VET', 'GAS', 'HAM', 'STR', 'OCO', 'RAI', 'RIC', 'ALO', 'RUS', 'LAT', 'TSU', 'SCH', 'BOT', 'LEC'], # Monaco
         ['PER', 'VET', 'GAS', 'LEC', 'NOR', 'ALO', 'TSU', 'SAI', 'RIC', 'RAI', 'BOT', 'SCH', 'HAM', 'LAT', 'RUS', 'VER', 'STR', 'OCO'], # Baku
         ['VER', 'HAM', 'PER', 'BOT', 'NOR', 'RIC', 'GAS', 'ALO', 'VET', 'STR', 'SAI', 'RUS', 'TSU', 'OCO', 'LEC', 'RAI', 'SCH', 'LAT'], # France
         ['VER', 'HAM', 'BOT', 'PER', 'NOR', 'SAI', 'LEC', 'STR', 'ALO', 'TSU', 'RAI', 'VET', 'RIC', 'OCO', 'SCH', 'LAT', 'RUS', 'GAS'], # Styrian Austria GP
         ['VER', 'BOT', 'NOR', 'HAM', 'SAI', 'PER', 'RIC', 'LEC', 'GAS', 'ALO', 'RUS', 'TSU', 'STR', 'RAI', 'LAT', 'VET', 'SCH', 'OCO'], # Austrian GP
         ['HAM', 'LEC', 'BOT', 'NOR', 'RIC', 'SAI', 'ALO', 'STR', 'OCO', 'TSU', 'GAS', 'RUS', 'LAT', 'RAI', 'PER', 'SCH', 'VET', 'VER'], # Silverstone
         ['OCO', 'HAM', 'SAI', 'ALO', 'GAS', 'TSU', 'LAT', 'RUS', 'VER', 'RAI', 'RIC', 'SCH', 'NOR', 'BOT', 'PER', 'LEC', 'STR', 'VET'], # Hungaroring
         ['VER', 'RUS', 'HAM', 'RIC', 'VET', 'GAS', 'OCO', 'LEC', 'LAT', 'SAI', 'ALO', 'BOT', 'NOR', 'TSU', 'SCH', 'RAI', 'PER', 'STR'], # Spa
         ['VER', 'HAM', 'BOT', 'GAS', 'LEC', 'ALO', 'SAI', 'PER', 'OCO', 'NOR', 'RIC', 'STR', 'VET', 'LAT', 'RUS', 'SCH', 'TSU'], # Zandvoort
         ['RIC', 'NOR', 'BOT', 'LEC', 'PER', 'SAI', 'STR', 'ALO', 'RUS', 'OCO', 'LAT', 'VET', 'SCH', 'HAM', 'VER', 'GAS', 'TSU'], # Monza
         ['HAM', 'VER', 'SAI', 'RIC', 'BOT', 'ALO', 'NOR', 'RAI', 'PER', 'RUS', 'STR', 'VET', 'GAS', 'OCO', 'LEC', 'TSU', 'LAT', 'SCH'], # Sochi
         ['BOT', 'VER', 'PER', 'LEC', 'HAM', 'GAS', 'NOR', 'SAI', 'STR', 'OCO', 'RAI', 'RIC', 'TSU', 'RUS', 'ALO', 'LAT', 'SCH', 'VET'], # Turkey
         ['VER', 'HAM', 'PER', 'LEC', 'RIC', 'BOT', 'SAI', 'NOR', 'TSU', 'VET', 'STR', 'RAI', 'RUS', 'LAT', 'SCH', 'ALO', 'OCO', 'GAS'], # Austin
         ['VER', 'HAM', 'PER', 'GAS', 'LEC', 'SAI', 'VET', 'RAI', 'ALO', 'NOR', 'RIC', 'OCO', 'STR', 'BOT', 'RUS', 'LAT', 'SCH', 'TSU'], # Mexico
         ['HAM', 'VER', 'BOT', 'PER', 'LEC', 'SAI', 'GAS', 'OCO', 'ALO', 'NOR', 'VET', 'RAI', 'RUS', 'TSU', 'LAT', 'SCH', 'RIC', 'STR'], # Brazil
         ['HAM', 'VER', 'ALO', 'PER', 'OCO', 'STR', 'SAI', 'LEC', 'NOR', 'VET', 'GAS', 'RIC', 'TSU', 'RAI', 'SCH', 'RUS', 'LAT', 'BOT'], # Qatar
         ['HAM', 'VER', 'BOT', 'OCO', 'RIC', 'GAS', 'LEC', 'SAI', 'NOR', 'STR', 'LAT', 'ALO', 'TSU', 'RAI', 'VET', 'PER', 'RUS', 'SCH'], # Jeddah
         ['VER', 'HAM', 'SAI', 'TSU', 'GAS', 'BOT', 'NOR', 'ALO', 'OCO', 'LEC', 'VET', 'RIC', 'STR', 'SCH', 'PER', 'LAT', 'RUS', 'RAI'], # Yas Marina
          ]


tracks = ["sakhir", "Imola", "Portugal", "Spain", "Monaco", "Baku", "France", "Austria", "Austria", "Silverstone", "Hungaroring", "Belgium", "Zandvoort", "Monza",
          "Sochi", "Turkey", "Austin", "Mexico", "brazil", "Qatar", "Jeddah", "Yas Marina"]

weather_conditions = [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1]
