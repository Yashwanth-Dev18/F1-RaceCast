


def getCar(driver):
    if driver == "HAM" or driver == "BOT":
        return "W09 - 2018"
    elif driver == "RAI" or driver == "VET":
        return "SF71H - 2018"
    elif driver == "VER" or driver == "RIC":
        return "RB14 - 2018"
    elif driver == "STR":
        return "FW41 - 2018"
    elif driver == "ALO" or driver == "VAN":
        return "MCL33 - 2018"
    elif driver == "GAS":
        return "STR13 - 2018"
    elif driver == "OCO" or driver == "PER":
        return "VJM11 - 2018"
    elif driver == "LEC" or driver == "ERI":
        return "C37 - 2018"
    elif driver == "MAG" or driver == "GRO":
        return "VF-18 - 2018"
    elif driver == "SAI" or driver == "HUL":
        return "RS18 - 2018"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['VET', 'HAM', 'RAI', 'RIC', 'ALO', 'VER', 'HUL', 'BOT', 'VAN', 'SAI', 'PER', 'OCO', 'LEC', 'STR', 'GRO', 'MAG', 'GAS', 'ERI'],	# Australia
         ['VET', 'BOT', 'HAM', 'GAS', 'MAG', 'HUL', 'ALO', 'VAN', 'ERI', 'OCO', 'SAI', 'LEC', 'GRO', 'STR', 'PER', 'RAI', 'VER', 'RIC'],	# Bahrain
         ['RIC', 'BOT', 'RAI', 'HAM', 'VER', 'HUL', 'ALO', 'VET', 'SAI', 'MAG', 'OCO', 'PER', 'VAN', 'STR', 'ERI', 'GRO', 'GAS', 'LEC'],	# China
         ['HAM', 'RAI', 'PER', 'VET', 'SAI', 'LEC', 'ALO', 'STR', 'VAN', 'ERI', 'GAS', 'MAG', 'BOT', 'GRO', 'VER', 'RIC', 'HUL', 'OCO'],	# Azerbaijan
         ['HAM', 'BOT', 'VER', 'VET', 'RIC', 'MAG', 'SAI', 'ALO', 'PER', 'LEC', 'STR', 'ERI', 'VAN', 'OCO', 'RAI', 'GRO', 'GAS', 'HUL'],	# Spain
         ['RIC', 'VET', 'HAM', 'RAI', 'BOT', 'OCO', 'GAS', 'HUL', 'VER', 'SAI', 'ERI', 'PER', 'MAG', 'VAN', 'GRO', 'STR', 'LEC', 'ALO'],	# Monaco
         ['VET', 'BOT', 'VER', 'RIC', 'HAM', 'RAI', 'HUL', 'SAI', 'OCO', 'LEC', 'GAS', 'GRO', 'MAG', 'PER', 'ERI', 'VAN', 'ALO', 'STR'],	# Canada
         ['HAM', 'VER', 'RAI', 'RIC', 'VET', 'MAG', 'BOT', 'SAI', 'HUL', 'LEC', 'GRO', 'VAN', 'ERI', 'ALO', 'STR', 'PER', 'OCO', 'GAS'],	# France
         ['VER', 'RAI', 'VET', 'GRO', 'MAG', 'OCO', 'PER', 'ALO', 'LEC', 'ERI', 'GAS', 'SAI', 'STR', 'VAN', 'HAM', 'RIC', 'BOT', 'HUL'],	# Austria
         ['VET', 'HAM', 'RAI', 'BOT', 'RIC', 'HUL', 'OCO', 'ALO', 'MAG', 'PER', 'VAN', 'STR', 'GAS', 'VER', 'GRO', 'SAI', 'ERI', 'LEC'],	# Great Britain
         ['HAM', 'BOT', 'RAI', 'VER', 'HUL', 'GRO', 'PER', 'OCO', 'ERI', 'MAG', 'SAI', 'VAN', 'GAS', 'LEC', 'ALO', 'STR', 'VET', 'RIC'],	# Germany
         ['HAM', 'VET', 'RAI', 'RIC', 'BOT', 'GAS', 'MAG', 'ALO', 'SAI', 'GRO', 'HUL', 'OCO', 'PER', 'ERI', 'STR', 'VAN', 'VER', 'LEC'],	# Hungary
         ['VET', 'HAM', 'VER', 'BOT', 'PER', 'OCO', 'GRO', 'MAG', 'GAS', 'ERI', 'SAI', 'STR', 'VAN', 'RIC', 'RAI', 'LEC', 'ALO', 'HUL'],	# Belgium
         ['HAM', 'RAI', 'BOT', 'VET', 'VER', 'OCO', 'PER', 'SAI', 'STR', 'LEC', 'VAN', 'HUL', 'GAS', 'ERI', 'MAG', 'RIC', 'ALO', 'GRO'],	# Italy
         ['HAM', 'VER', 'VET', 'BOT', 'RAI', 'RIC', 'ALO', 'SAI', 'LEC', 'HUL', 'ERI', 'VAN', 'GAS', 'STR', 'GRO', 'PER', 'MAG', 'OCO'],	# Singapore
         ['HAM', 'BOT', 'VET', 'RAI', 'VER', 'RIC', 'LEC', 'MAG', 'OCO', 'PER', 'GRO', 'HUL', 'ERI', 'ALO', 'STR', 'VAN', 'SAI', 'GAS'],	# Russia
         ['HAM', 'BOT', 'VER', 'RIC', 'RAI', 'VET', 'PER', 'GRO', 'OCO', 'SAI', 'GAS', 'ERI', 'ALO', 'VAN', 'STR', 'LEC', 'HUL', 'MAG'],	# Japan
         ['RAI', 'VER', 'HAM', 'VET', 'BOT', 'HUL', 'SAI', 'PER', 'ERI', 'VAN', 'GAS', 'STR', 'LEC', 'RIC', 'GRO', 'ALO', 'OCO', 'MAG'],	# USA
         ['VER', 'VET', 'RAI', 'HAM', 'BOT', 'HUL', 'LEC', 'VAN', 'ERI', 'GAS', 'OCO', 'STR', 'MAG', 'GRO', 'RIC', 'PER', 'SAI', 'ALO'],	# Mexico
         ['HAM', 'VER', 'RAI', 'RIC', 'BOT', 'VET', 'LEC', 'GRO', 'MAG', 'PER', 'SAI', 'GAS', 'OCO', 'VAN', 'ALO', 'STR', 'HUL', 'ERI'],	# Brazil
         ['HAM', 'VET', 'VER', 'RIC', 'BOT', 'SAI', 'LEC', 'PER', 'GRO', 'MAG', 'ALO', 'STR', 'VAN', 'GAS', 'OCO', 'ERI', 'RAI', 'HUL']	  # Abu Dhabi
          ]


tracks = ['Australia', 'Sakhir', 'China', 'Baku', 'Spain', 'Monaco', 'Canada', 'France', 'Austria', 'Silverstone', 'Hockenheimring', 
          'Hungary', 'Belgium', 'Monza', 'Singapore', 'Sochi', 'Japan', 'Austin', 'Mexico', 'Brazil', 'Yas Marina']

weather_conditions = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]