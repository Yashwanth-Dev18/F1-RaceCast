

def getCar(driver):
    if driver == "HAM" or driver == "BOT":
        return "W11 - 2020"
    elif driver == "LEC" or driver == "VET":
        return "SF1000 - 2020"
    elif driver == "VER" or driver == "ALB":
        return "RB16 - 2020"
    elif driver == "RUS" or driver == "LAT":
        return "FW43 - 2020"
    elif driver == "NOR" or driver == "SAI":
        return "MCL35 - 2020"
    elif driver == "KVY" or driver == "GAS":
        return "AT01 - 2020"
    elif driver == "STR" or driver == "PER" or driver == "HUL":
        return "RP20 - 2020"
    elif driver == "RAI":
        return "C39 - 2020"
    elif driver == "MAG" or driver == "GRO":
        return "VF-20 - 2020"
    elif driver == "RIC" or driver == "OCO":
        return "RS20 - 2020"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"


races = [['BOT', 'LEC', 'NOR', 'HAM', 'SAI', 'PER', 'GAS', 'OCO', 'VET', 'LAT', 'KVY', 'ALB', 'RAI', 'RUS', 'GRO', 'MAG', 'STR', 'RIC', 'VER'],	# Austria
         ['HAM', 'BOT', 'VER', 'ALB', 'NOR', 'PER', 'STR', 'RIC', 'SAI', 'KVY', 'RAI', 'MAG', 'GRO', 'GAS', 'RUS', 'LAT', 'OCO', 'LEC', 'VET'],	# Styria
         ['HAM', 'VER', 'BOT', 'STR', 'ALB', 'VET', 'PER', 'RIC', 'SAI', 'MAG', 'LEC', 'KVY', 'NOR', 'OCO', 'RAI', 'GRO', 'RUS', 'LAT', 'GAS'],	# Hungary
         ['HAM', 'VER', 'LEC', 'RIC', 'NOR', 'OCO', 'GAS', 'ALB', 'STR', 'VET', 'BOT', 'RUS', 'SAI', 'LAT', 'GRO', 'RAI', 'KVY', 'MAG', 'HUL'],	# Great Britain
         ['VER', 'HAM', 'BOT', 'LEC', 'ALB', 'STR', 'HUL', 'OCO', 'NOR', 'KVY', 'GAS', 'VET', 'SAI', 'RIC', 'RAI', 'GRO', 'RUS', 'LAT', 'MAG'],	# 70th Anniversary
         ['HAM', 'VER', 'BOT', 'STR', 'PER', 'SAI', 'VET', 'ALB', 'GAS', 'NOR', 'RIC', 'KVY', 'OCO', 'RAI', 'MAG', 'RUS', 'LAT', 'GRO', 'LEC'],	# Spain
         ['HAM', 'BOT', 'VER', 'RIC', 'OCO', 'ALB', 'NOR', 'GAS', 'STR', 'PER', 'KVY', 'RAI', 'VET', 'LEC', 'GRO', 'LAT', 'MAG', 'RUS', 'SAI'],	# Belgium
         ['GAS', 'SAI', 'STR', 'NOR', 'BOT', 'RIC', 'HAM', 'OCO', 'KVY', 'PER', 'LAT', 'GRO', 'RAI', 'RUS', 'ALB', 'VER', 'LEC', 'MAG', 'VET'],	# Italy
         ['HAM', 'BOT', 'ALB', 'RIC', 'PER', 'NOR', 'KVY', 'LEC', 'RAI', 'VET', 'RUS', 'GRO', 'STR', 'OCO', 'LAT', 'MAG', 'SAI', 'VER', 'GAS'],	# Tuscany
         ['BOT', 'VER', 'HAM', 'PER', 'RIC', 'LEC', 'OCO', 'KVY', 'GAS', 'ALB', 'MAG', 'VET', 'RAI', 'NOR', 'LAT', 'GRO', 'RUS', 'SAI', 'STR'],	# Russia
         ['HAM', 'VER', 'RIC', 'PER', 'SAI', 'GAS', 'LEC', 'HUL', 'GRO', 'VET', 'RAI', 'MAG', 'LAT', 'KVY', 'NOR', 'ALB', 'OCO', 'BOT', 'RUS'],	# Eifel
         ['HAM', 'BOT', 'VER', 'LEC', 'GAS', 'SAI', 'PER', 'OCO', 'RIC', 'VET', 'RAI', 'ALB', 'NOR', 'RUS', 'MAG', 'GRO', 'LAT', 'KVY', 'STR'],	# Portugal
         ['HAM', 'BOT', 'RIC', 'KVY', 'LEC', 'PER', 'SAI', 'NOR', 'RAI', 'LAT', 'VET', 'STR', 'GRO', 'ALB', 'RUS', 'VER', 'MAG', 'OCO', 'GAS'],	# Emilia Romagna
         ['HAM', 'PER', 'VET', 'LEC', 'SAI', 'VER', 'ALB', 'NOR', 'STR', 'RIC', 'OCO', 'KVY', 'GAS', 'BOT', 'RAI', 'RUS', 'MAG', 'GRO', 'LAT'],	# Turkey
         ['HAM', 'VER', 'ALB', 'NOR', 'SAI', 'GAS', 'RIC', 'BOT', 'OCO', 'LEC', 'KVY', 'RUS', 'VET', 'LAT', 'RAI', 'MAG', 'PER', 'STR', 'GRO'],	# Bahrain
         ['PER', 'OCO', 'STR', 'SAI', 'RIC', 'ALB', 'KVY', 'BOT', 'RUS', 'NOR', 'GAS', 'VET', 'RAI', 'MAG', 'LAT', 'VER', 'LEC'],	# Sakhir
         ['VER', 'BOT', 'HAM', 'ALB', 'NOR', 'SAI', 'RIC', 'GAS', 'OCO', 'STR', 'KVY', 'RAI', 'LEC', 'VET', 'RUS', 'LAT', 'MAG', 'PER']	# Abu Dhabi
          ]


tracks = ["Austria", "Austria", "Hungary", "Silverstone", "Silverstone", "Spain", "Belgium", "Monza", "Mugello", "Russia", "Nurburgring", 
          "Portugal", "Imola", "Turkey", "Sakhir", "Sakhir", "Yas Marina"]

weather_conditions = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1]