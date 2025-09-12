

def getCar(driver):
    if driver == "HAM" or driver == "BOT":
        return "W10 - 2019"
    elif driver == "LEC" or driver == "VET":
        return "SF90 - 2019"
    elif driver == "VER" or driver == "ALB":
        return "RB15 - 2019"
    elif driver == "RUS":
        return "FW42 - 2019"
    elif driver == "NOR" or driver == "SAI":
        return "MCL34 - 2019"
    elif driver == "KVY" or driver == "GAS":
        return "STR14 - 2019"
    elif driver == "STR" or driver == "PER":
        return "RP19 - 2019"
    elif driver == "RAI":
        return "C38 - 2019"
    elif driver == "MAG" or driver == "GRO":
        return "VF-19 - 2019"
    elif driver == "RIC" or driver == "HUL":
        return "RS19 - 2019"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"


races = [['BOT', 'HAM', 'VER', 'VET', 'LEC', 'MAG', 'HUL', 'RAI', 'STR', 'KVY', 'GAS', 'NOR', 'PER', 'ALB', 'RUS', 'GRO', 'RIC', 'SAI'],	# Australia
         ['HAM', 'BOT', 'LEC', 'VER', 'VET', 'NOR', 'RAI', 'GAS', 'ALB', 'PER', 'KVY', 'MAG', 'STR', 'RUS', 'HUL', 'RIC', 'SAI', 'GRO'],	# Bahrain
         ['HAM', 'BOT', 'VET', 'VER', 'LEC', 'GAS', 'RIC', 'PER', 'RAI', 'ALB', 'GRO', 'STR', 'MAG', 'SAI', 'RUS', 'NOR', 'KVY', 'HUL'],	# China
         ['BOT', 'HAM', 'VET', 'VER', 'LEC', 'PER', 'SAI', 'NOR', 'STR', 'RAI', 'ALB', 'MAG', 'HUL', 'RUS', 'GAS', 'GRO', 'KVY', 'RIC'],	# Azerbaijan
         ['HAM', 'BOT', 'VER', 'VET', 'LEC', 'GAS', 'MAG', 'SAI', 'KVY', 'GRO', 'ALB', 'RIC', 'HUL', 'RAI', 'PER', 'RUS', 'STR', 'NOR'],	# Spain
         ['HAM', 'VET', 'BOT', 'VER', 'GAS', 'SAI', 'KVY', 'ALB', 'RIC', 'GRO', 'NOR', 'PER', 'HUL', 'MAG', 'RUS', 'STR', 'RAI', 'LEC'],	# Monaco
         ['HAM', 'VET', 'LEC', 'BOT', 'VER', 'RIC', 'HUL', 'GAS', 'STR', 'KVY', 'SAI', 'PER', 'GRO', 'RAI', 'RUS', 'MAG', 'ALB', 'NOR'],	# Canada
         ['HAM', 'BOT', 'LEC', 'VER', 'VET', 'SAI', 'RAI', 'HUL', 'NOR', 'GAS', 'RIC', 'PER', 'STR', 'KVY', 'ALB', 'MAG', 'RUS', 'GRO'],	# France
         ['VER', 'LEC', 'BOT', 'VET', 'HAM', 'NOR', 'GAS', 'SAI', 'RAI', 'PER', 'RIC', 'HUL', 'STR', 'ALB', 'GRO', 'KVY', 'RUS', 'MAG'],	# Austria
         ['HAM', 'BOT', 'LEC', 'GAS', 'VER', 'SAI', 'RIC', 'RAI', 'KVY', 'HUL', 'NOR', 'ALB', 'STR', 'RUS', 'VET', 'PER', 'GRO', 'MAG'],	# Great Britain
         ['VER', 'VET', 'KVY', 'STR', 'SAI', 'ALB', 'GRO', 'MAG', 'HAM', 'RUS', 'RAI', 'GAS', 'BOT', 'HUL', 'LEC', 'NOR', 'RIC', 'PER'],	# Hockenheimring
         ['HAM', 'VER', 'VET', 'LEC', 'SAI', 'GAS', 'RAI', 'BOT', 'NOR', 'ALB', 'PER', 'HUL', 'MAG', 'RIC', 'KVY', 'RUS', 'STR', 'GRO'],	# Hungary
         ['NOR', 'MAG', 'GRO', 'RIC', 'RUS', 'RAI', 'SAI', 'VER', 'LEC', 'HAM', 'BOT', 'VET', 'ALB', 'PER', 'KVY', 'HUL', 'GAS', 'STR'],	# Belgium
         ['GAS', 'STR', 'VET', 'RUS', 'RAI', 'GRO', 'MAG', 'KVY', 'SAI', 'LEC', 'BOT', 'HAM', 'RIC', 'HUL', 'ALB', 'PER', 'VER', 'NOR'],	# Monza
         ['VET', 'LEC', 'VER', 'HAM', 'BOT', 'ALB', 'NOR', 'GAS', 'HUL', 'GRO', 'SAI', 'STR', 'RIC', 'KVY', 'MAG', 'RAI', 'PER', 'RUS'],	# Singapore
         ['HAM', 'BOT', 'LEC', 'VER', 'ALB', 'SAI', 'PER', 'NOR', 'MAG', 'HUL', 'STR', 'KVY', 'RAI', 'GAS', 'RUS', 'VET', 'RIC', 'GRO'],	# Russia
         ['BOT', 'VET', 'HAM', 'ALB', 'SAI', 'LEC', 'GAS', 'PER', 'STR', 'KVY', 'NOR', 'RAI', 'GRO', 'MAG', 'RUS', 'VER', 'RIC', 'HUL'],	# Japan
         ['HAM', 'VET', 'BOT', 'LEC', 'ALB', 'VER', 'PER', 'RIC', 'GAS', 'HUL', 'KVY', 'STR', 'SAI', 'MAG', 'RUS', 'GRO', 'RAI', 'NOR'],	# Mexico
         ['BOT', 'HAM', 'VER', 'LEC', 'ALB', 'RIC', 'NOR', 'SAI', 'HUL', 'PER', 'RAI', 'KVY', 'STR', 'GRO', 'GAS', 'RUS', 'MAG', 'VET'],	# Austin
         ['VER', 'GAS', 'SAI', 'RAI', 'RIC', 'HAM', 'NOR', 'PER', 'KVY', 'MAG', 'RUS', 'GRO', 'ALB', 'HUL', 'VET', 'LEC', 'STR', 'BOT'],	# Brazil
         ['HAM', 'VER', 'LEC', 'BOT', 'VET', 'ALB', 'PER', 'NOR', 'KVY', 'SAI', 'RIC', 'HUL', 'RAI', 'MAG', 'GRO', 'RUS', 'GAS', 'STR']	  # Abu Dhabi
          ]


tracks = ['Australia', 'Sakhir', 'China', 'Baku', 'Spain', 'Monaco', 'Canada', 'France', 'Austria', 'Silverstone', 'Hockenheimring', 
          'Hungary', 'Belgium', 'Monza', 'Singapore', 'Sochi', 'Japan', 'Mexico', 'Austin', 'Brazil', 'Yas Marina']

weather_conditions = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]