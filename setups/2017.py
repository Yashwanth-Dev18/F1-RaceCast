


def getCar(driver):
    if driver == "HAM" or driver == "BOT":
        return "W08 - 2017"
    elif driver == "RAI" or driver == "VET":
        return "SF70H - 2017"
    elif driver == "VER" or driver == "RIC":
        return "RB13 - 2017"
    elif driver == "STR" or driver == "MAS":
        return "FW40 - 2017"
    elif driver == "ALO" or driver == "VAN" or driver == "BUT":
        return "MCL32 - 2017"
    elif driver == "SAI" or driver == "KVY" or driver == "GAS":
        return "STR12 - 2017"
    elif driver == "OCO" or driver == "PER":
        return "VJM10 - 2017"
    elif driver == "ERI":
        return "C36 - 2017"
    elif driver == "MAG" or driver == "GRO":
        return "VF-17 - 2017"
    elif driver == "HUL" or driver == "PAL":
        return "RS17 - 2017"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"



races = [['VET', 'HAM', 'BOT', 'RAI', 'VER', 'MAS', 'PER', 'SAI', 'KVY', 'OCO', 'HUL', 'VAN', 'ALO', 'MAG', 'STR', 'RIC', 'ERI', 'PAL', 'GRO'],	# Australia
         ['HAM', 'VET', 'VER', 'RIC', 'RAI', 'BOT', 'SAI', 'MAG', 'PER', 'OCO', 'GRO', 'HUL', 'PAL', 'MAS', 'ERI', 'ALO', 'KVY', 'VAN', 'STR'],	# China
         ['VET', 'HAM', 'BOT', 'RAI', 'RIC', 'MAS', 'PER', 'GRO', 'HUL', 'OCO', 'KVY', 'PAL', 'ALO', 'ERI', 'SAI', 'STR', 'VER', 'MAG', 'VAN'],	# Bahrain
         ['BOT', 'VET', 'RAI', 'HAM', 'VER', 'PER', 'OCO', 'HUL', 'MAS', 'SAI', 'STR', 'KVY', 'MAG', 'VAN', 'ERI', 'RIC', 'PAL', 'GRO', 'ALO'],	# Russia
         ['HAM', 'VET', 'RIC', 'PER', 'OCO', 'HUL', 'SAI', 'KVY', 'GRO', 'ERI', 'ALO', 'MAS', 'MAG', 'PAL', 'STR', 'BOT', 'VAN', 'VER', 'RAI'],	# Spain
         ['VET', 'RAI', 'RIC', 'BOT', 'VER', 'SAI', 'HAM', 'GRO', 'MAS', 'MAG', 'PAL', 'OCO', 'PER', 'KVY', 'STR', 'VAN', 'ERI', 'BUT', 'HUL'],	# Monaco
         ['HAM', 'BOT', 'RIC', 'VET', 'PER', 'OCO', 'RAI', 'HUL', 'STR', 'GRO', 'PAL', 'MAG', 'ERI', 'VAN', 'ALO', 'KVY', 'VER', 'MAS', 'SAI'],	# Canada
         ['RIC', 'BOT', 'STR', 'VET', 'HAM', 'OCO', 'MAG', 'SAI', 'ALO', 'ERI', 'VAN', 'GRO', 'RAI', 'PER', 'MAS', 'HUL', 'VER', 'KVY', 'PAL'],	# Azerbaijan
         ['BOT', 'VET', 'RIC', 'HAM', 'RAI', 'GRO', 'PER', 'OCO', 'MAS', 'STR', 'PAL', 'VAN', 'HUL', 'ERI', 'KVY', 'SAI', 'MAG', 'ALO', 'VER'],	# Austria
         ['HAM', 'BOT', 'RAI', 'VER', 'RIC', 'HUL', 'VET', 'OCO', 'PER', 'MAS', 'VAN', 'MAG', 'GRO', 'ERI', 'KVY', 'STR', 'ALO', 'SAI', 'PAL'],	# Great Britain
         ['VET', 'RAI', 'BOT', 'HAM', 'VER', 'ALO', 'SAI', 'PER', 'OCO', 'VAN', 'KVY', 'PAL', 'MAG', 'STR', 'ERI', 'HUL', 'GRO', 'RIC'],	# Hungary
         ['HAM', 'VET', 'RIC', 'RAI', 'BOT', 'HUL', 'GRO', 'MAS', 'OCO', 'SAI', 'STR', 'KVY', 'PAL', 'VAN', 'MAG', 'ERI', 'PER', 'ALO', 'VER'],	# Belgium
         ['HAM', 'BOT', 'VET', 'RIC', 'RAI', 'OCO', 'STR', 'MAS', 'PER', 'VER', 'MAG', 'KVY', 'HUL', 'SAI', 'GRO', 'ALO', 'ERI', 'VAN', 'PAL'],	# Italy
         ['HAM', 'RIC', 'BOT', 'SAI', 'PER', 'PAL', 'VAN', 'STR', 'GRO', 'OCO', 'MAS', 'MAG', 'HUL', 'ERI', 'KVY', 'ALO', 'VET', 'VER', 'RAI'],	# Singapore
         ['VER', 'HAM', 'RIC', 'VET', 'BOT', 'PER', 'VAN', 'STR', 'MAS', 'OCO', 'ALO', 'MAG', 'GRO', 'GAS', 'PAL', 'HUL', 'ERI', 'SAI', 'RAI'],	# Malaysia
         ['HAM', 'VER', 'RIC', 'BOT', 'RAI', 'OCO', 'PER', 'MAG', 'GRO', 'MAS', 'ALO', 'PAL', 'GAS', 'VAN', 'STR', 'HUL', 'ERI', 'VET', 'SAI'],	# Japan
         ['HAM', 'VET', 'RAI', 'VER', 'BOT', 'OCO', 'SAI', 'PER', 'MAS', 'KVY', 'STR', 'VAN', 'GRO', 'ERI', 'MAG', 'ALO', 'RIC', 'HUL'],	# USA
         ['VER', 'BOT', 'RAI', 'VET', 'OCO', 'STR', 'PER', 'MAG', 'HAM', 'ALO', 'MAS', 'VAN', 'GAS', 'GRO', 'SAI', 'ERI', 'HUL', 'RIC'],	# Mexico
         ['VET', 'BOT', 'RAI', 'HAM', 'VER', 'RIC', 'MAS', 'ALO', 'PER', 'HUL', 'SAI', 'GAS', 'ERI', 'GRO', 'STR', 'OCO', 'VAN', 'MAG'],	# Brazil
         ['BOT', 'HAM', 'VET', 'RAI', 'VER', 'HUL', 'PER', 'OCO', 'ALO', 'MAS', 'GRO', 'VAN', 'MAG', 'GAS', 'ERI', 'STR', 'SAI', 'RIC']	  # Abu Dhabi

          ]


tracks = ['Australia', 'China', 'Bahrain', 'Russia', 'Spain', 'Monaco', 'Canada', 'Azerbaijan', 'Austria', 'Silverstone', 'Hungary', 'Belgium',
          'Monza', 'Singapore', 'Malaysia', 'Japan', 'Austin', 'Mexico', 'Brazil', 'Yas Marina']

weather_conditions = [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1]
