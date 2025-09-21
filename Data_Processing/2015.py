


def getCar(driver):
    if driver == "HAM" or driver == "ROS":
        return "W06 - 2015"
    elif driver == "RAI" or driver == "VET":
        return "SF15-T - 2015"
    elif driver == "KVY" or driver == "RIC":
        return "RB11 - 2015"
    elif driver == "BOT" or driver == "MAS":
        return "FW37 - 2015"
    elif driver == "MAG" or driver == "BUT" or driver == "ALO":
        return "MP4-30 - 2015"
    elif driver == "SAI" or driver == "VER":
        return "STR10 - 2015"
    elif driver == "HUL" or driver == "PER":
        return "VJM08 - 2015"
    elif driver == "ERI" or driver == "NAS":
        return "C34 - 2015"
    elif driver == "GRO" or driver == "MAL":
        return "E23 - 2015"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['HAM', 'ROS', 'VET', 'MAS', 'NAS', 'RIC', 'HUL', 'ERI', 'SAI', 'PER', 'BUT', 'RAI', 'VER', 'GRO', 'MAL', 'KVY', 'MAG', 'BOT'],		# Australia
         ['VET', 'HAM', 'ROS', 'RAI', 'BOT', 'MAS', 'VER', 'SAI', 'KVY', 'RIC', 'GRO', 'NAS', 'PER', 'HUL', 'MAL', 'BUT', 'ALO', 'ERI'],		# Malaysia
         ['HAM', 'ROS', 'VET', 'RAI', 'MAS', 'BOT', 'GRO', 'NAS', 'RIC', 'ERI', 'PER', 'ALO', 'SAI', 'BUT', 'VER', 'MAL', 'KVY', 'HUL'],		# China
         ['HAM', 'RAI', 'ROS', 'BOT', 'VET', 'RIC', 'GRO', 'PER', 'KVY', 'MAS', 'ALO', 'NAS', 'HUL', 'ERI', 'MAL', 'VER', 'SAI', 'BUT'],		# Bahrain
         ['ROS', 'HAM', 'VET', 'BOT', 'RAI', 'MAS', 'RIC', 'GRO', 'SAI', 'KVY', 'VER', 'NAS', 'PER', 'ERI', 'HUL', 'BUT', 'MAL', 'ALO'],		# Spain
         ['ROS', 'VET', 'HAM', 'KVY', 'RIC', 'RAI', 'PER', 'BUT', 'NAS', 'SAI', 'HUL', 'GRO', 'ERI', 'BOT', 'MAS', 'VER', 'ALO', 'MAL'],		# Monaco
         ['HAM', 'ROS', 'BOT', 'RAI', 'VET', 'MAS', 'MAL', 'HUL', 'KVY', 'GRO', 'PER', 'SAI', 'RIC', 'ERI', 'VER', 'NAS', 'BUT', 'ALO'],		# Canada
         ['ROS', 'HAM', 'MAS', 'VET', 'BOT', 'HUL', 'MAL', 'VER', 'PER', 'RIC', 'NAS', 'KVY', 'ERI', 'GRO', 'SAI', 'BUT', 'RAI', 'ALO'],		# Austria
         ['HAM', 'ROS', 'VET', 'MAS', 'BOT', 'KVY', 'HUL', 'RAI', 'PER', 'ALO', 'ERI', 'SAI', 'RIC', 'VER', 'GRO', 'MAL', 'BUT', 'NAS'],		# Great Britain
         ['VET', 'KVY', 'RIC', 'VER', 'ALO', 'HAM', 'GRO', 'ROS', 'BUT', 'ERI', 'NAS', 'MAS', 'BOT', 'MAL', 'SAI', 'RAI', 'PER', 'HUL'],		# Hungary
         ['HAM', 'ROS', 'GRO', 'KVY', 'PER', 'MAS', 'RAI', 'VER', 'BOT', 'ERI', 'NAS', 'VET', 'ALO', 'BUT', 'SAI', 'RIC', 'MAL', 'HUL'],		# Belgium
         ['HAM', 'VET', 'MAS', 'BOT', 'RAI', 'PER', 'HUL', 'RIC', 'ERI', 'KVY', 'SAI', 'VER', 'NAS', 'BUT', 'ROS', 'ALO', 'GRO', 'MAL'],		# Italy
         ['VET', 'RIC', 'RAI', 'ROS', 'BOT', 'KVY', 'PER', 'VER', 'SAI', 'NAS', 'ERI', 'MAL', 'GRO', 'BUT', 'ALO', 'HAM', 'MAS', 'HUL'],		# Singapore
         ['HAM', 'ROS', 'VET', 'RAI', 'BOT', 'HUL', 'GRO', 'MAL', 'VER', 'SAI', 'ALO', 'PER', 'KVY', 'ERI', 'RIC', 'BUT', 'MAS', 'NAS'],		# Japan
         ['HAM', 'VET', 'PER', 'MAS', 'KVY', 'NAS', 'MAL', 'RAI', 'BUT', 'VER', 'ALO', 'BOT', 'RIC', 'SAI', 'GRO', 'ROS', 'HUL', 'ERI'],		# Russia
         ['HAM', 'ROS', 'VET', 'VER', 'PER', 'BUT', 'SAI', 'MAL', 'NAS', 'RIC', 'ALO', 'KVY', 'HUL', 'ERI', 'RAI', 'MAS', 'GRO', 'BOT'],		# USA
         ['ROS', 'HAM', 'BOT', 'KVY', 'RIC', 'MAS', 'HUL', 'PER', 'VER', 'GRO', 'MAL', 'ERI', 'SAI', 'BUT', 'NAS', 'VET', 'RAI', 'ALO'],		# Mexico
         ['ROS', 'HAM', 'VET', 'RAI', 'BOT', 'HUL', 'KVY', 'GRO', 'VER', 'MAL', 'RIC', 'PER', 'NAS', 'BUT', 'ALO', 'ERI', 'SAI', 'MAS'],		# Brazil
         ['ROS', 'HAM', 'RAI', 'VET', 'PER', 'RIC', 'HUL', 'MAS', 'GRO', 'KVY', 'SAI', 'BUT', 'BOT', 'ERI', 'NAS', 'VER', 'ALO', 'MAL']		# Abu Dhabi
          ]


tracks = ['Australia', 'Malaysia', 'China', 'Bahrain', 'Spain', 'Monaco', 'Canada', 'Austria', 'Silverstone', 'Hungary', 'Belgium', 'Monza', 
          'Singapore', 'Japan', 'Sochi', 'Austin', 'Mexico', 'Brazil', 'Yas Marina']

weather_conditions = [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1]
