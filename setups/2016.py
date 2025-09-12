


def getCar(driver):
    if driver == "HAM" or driver == "ROS":
        return "W07 - 2016"
    elif driver == "RAI" or driver == "VET":
        return "SF16-H - 2016"
    elif driver == "KVY" or driver == "RIC":
        return "RB12 - 2016"
    elif driver == "BOT" or driver == "MAS":
        return "FW38 - 2016"
    elif driver == "ALO" or driver == "BUT" or driver == "VAN":
        return "MP4-31 - 2016"
    elif driver == "SAI" or driver == "VER":
        return "STR11 - 2016"
    elif driver == "HUL" or driver == "PER":
        return "VJM09 - 2016"
    elif driver == "ERI" or driver == "NAS":
        return "C35 - 2016"
    elif driver == "GRO":
        return "VF-16 - 2016"
    elif driver == "MAG" or driver == "PAL":
        return "RS16 - 2016"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['ROS', 'HAM', 'VET', 'RIC', 'MAS', 'GRO', 'HUL', 'BOT', 'SAI', 'VER', 'PAL', 'MAG', 'PER', 'BUT', 'NAS', 'ERI', 'RAI', 'ALO', 'KVY'],	# Australia
         ['ROS', 'RAI', 'HAM', 'RIC', 'GRO', 'VER', 'KVY', 'MAS', 'BOT', 'VAN', 'MAG', 'ERI', 'NAS', 'HUL', 'PER', 'SAI', 'BUT', 'VET', 'PAL'],	# Bahrain
         ['ROS', 'VET', 'KVY', 'RIC', 'RAI', 'MAS', 'HAM', 'VER', 'SAI', 'BOT', 'PER', 'ALO', 'BUT', 'HUL', 'ERI', 'MAG', 'GRO', 'NAS', 'PAL'],	# China
         ['ROS', 'HAM', 'RAI', 'BOT', 'MAS', 'ALO', 'MAG', 'GRO', 'PER', 'BUT', 'RIC', 'SAI', 'PAL', 'ERI', 'KVY', 'NAS', 'VER', 'VET', 'HUL'],	# Russia
         ['VER', 'RAI', 'VET', 'RIC', 'BOT', 'SAI', 'PER', 'MAS', 'BUT', 'KVY', 'ERI', 'PAL', 'NAS', 'MAG', 'GRO', 'ALO', 'HUL', 'HAM', 'ROS'],	# Spain
         ['HAM', 'RIC', 'PER', 'VET', 'ALO', 'HUL', 'ROS', 'SAI', 'BUT', 'MAS', 'BOT', 'GRO', 'ERI', 'NAS', 'VER', 'MAG', 'KVY', 'RAI', 'PAL'],	# Monaco
         ['HAM', 'VET', 'BOT', 'VER', 'ROS', 'RAI', 'RIC', 'HUL', 'SAI', 'PER', 'ALO', 'KVY', 'GRO', 'ERI', 'MAG', 'NAS', 'MAS', 'PAL', 'BUT'],	# Canada
         ['ROS', 'VET', 'PER', 'RAI', 'HAM', 'BOT', 'RIC', 'VER', 'HUL', 'MAS', 'BUT', 'NAS', 'GRO', 'MAG', 'PAL', 'ERI', 'ALO', 'SAI', 'KVY'],	# Europe
         ['HAM', 'VER', 'RAI', 'ROS', 'RIC', 'BUT', 'GRO', 'SAI', 'BOT', 'PAL', 'NAS', 'MAG', 'ERI', 'PER', 'ALO', 'HUL', 'MAS', 'VET', 'KVY'],	# Austria
         ['HAM', 'VER', 'ROS', 'RIC', 'RAI', 'PER', 'HUL', 'SAI', 'VET', 'KVY', 'MAS', 'BUT', 'ALO', 'BOT', 'NAS', 'MAG', 'PAL', 'GRO', 'ERI'],	# Great Britain
         ['HAM', 'ROS', 'RIC', 'VET', 'VER', 'RAI', 'ALO', 'SAI', 'BOT', 'HUL', 'PER', 'PAL', 'GRO', 'MAG', 'KVY', 'NAS', 'MAS', 'ERI', 'BUT'],	# Hungary
         ['HAM', 'RIC', 'VER', 'ROS', 'VET', 'RAI', 'HUL', 'BUT', 'BOT', 'PER', 'ALO', 'GRO', 'SAI', 'KVY', 'MAG', 'ERI', 'PAL', 'NAS', 'MAS'],	# Germany
         ['ROS', 'RIC', 'HAM', 'HUL', 'PER', 'VET', 'ALO', 'BOT', 'RAI', 'MAS', 'VER', 'GRO', 'KVY', 'PAL', 'NAS', 'MAG', 'ERI', 'SAI', 'BUT'],	# Belgium
         ['ROS', 'HAM', 'VET', 'RAI', 'RIC', 'BOT', 'VER', 'PER', 'MAS', 'HUL', 'GRO', 'BUT', 'ALO', 'SAI', 'ERI', 'MAG', 'KVY', 'PAL', 'NAS'],	# Italy
         ['ROS', 'RIC', 'HAM', 'RAI', 'VET', 'VER', 'ALO', 'PER', 'KVY', 'MAG', 'MAS', 'NAS', 'SAI', 'PAL', 'ERI', 'BUT', 'BOT', 'HUL', 'GRO'],	# Singapore
         ['RIC', 'VER', 'ROS', 'RAI', 'BOT', 'PER', 'ALO', 'HUL', 'BUT', 'PAL', 'SAI', 'ERI', 'MAS', 'KVY', 'NAS', 'HAM', 'MAG', 'GRO', 'VET'],	# Malaysia
         ['ROS', 'VER', 'HAM', 'VET', 'RAI', 'RIC', 'PER', 'HUL', 'MAS', 'BOT', 'GRO', 'PAL', 'KVY', 'MAG', 'ERI', 'ALO', 'SAI', 'BUT', 'NAS'],	# Japan
         ['HAM', 'ROS', 'RIC', 'VET', 'ALO', 'SAI', 'MAS', 'PER', 'BUT', 'GRO', 'KVY', 'MAG', 'PAL', 'ERI', 'NAS', 'BOT', 'RAI', 'VER', 'HUL'],	# USA
         ['HAM', 'ROS', 'RIC', 'VER', 'VET', 'RAI', 'HUL', 'BOT', 'MAS', 'PER', 'ERI', 'BUT', 'ALO', 'PAL', 'NAS', 'SAI', 'MAG', 'KVY', 'GRO'],	# Mexico
         ['HAM', 'ROS', 'VER', 'PER', 'VET', 'SAI', 'HUL', 'RIC', 'NAS', 'ALO', 'BOT', 'KVY', 'MAG', 'BUT', 'MAS', 'PAL', 'RAI', 'ERI', 'GRO'],	# Brazil
         ['HAM', 'ROS', 'VET', 'VER', 'RIC', 'RAI', 'HUL', 'PER', 'MAS', 'ALO', 'GRO', 'ERI', 'NAS', 'PAL', 'SAI', 'KVY', 'BUT', 'BOT', 'MAG']	# Abu Dhabi

          ]

tracks = ['Australia', 'Bahrain', 'China', 'Sochi', 'Spain', 'Monaco', 'Canada', 'Baku', 'Austria', 'Silverstone', 'Hungary', 'Hockenheimring', 
          'Belgium', 'Monza', 'Singapore', 'Malaysia', 'Japan', 'Austin', 'Mexico', 'Brazil', 'Yas Marina']

weather_conditions = [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1]