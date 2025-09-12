


def getCar(driver):
    if driver == "HAM" or driver == "ROS":
        return "W05 - 2014"
    elif driver == "RAI" or driver == "ALO":
        return "SF14-T - 2014"
    elif driver == "VET" or driver == "RIC":
        return "RB10 - 2014"
    elif driver == "BOT" or driver == "MAS":
        return "FW36 - 2014"
    elif driver == "MAG" or driver == "BUT":
        return "MP4-29 - 2014"
    elif driver == "KVY":
        return "STR9 - 2014"
    elif driver == "HUL" or driver == "PER":
        return "VJM07 - 2014"
    elif driver == "SUT":
        return "C33 - 2014"
    elif driver == "GRO" or driver == "MAL":
        return "E22 - 2014"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"


races = [['ROS', 'MAG', 'BUT', 'ALO', 'BOT', 'HUL', 'RAI', 'KVY', 'PER', 'SUT', 'GRO', 'MAL', 'VET', 'HAM', 'MAS', 'RIC'],	# Australia
         ['HAM', 'ROS', 'VET', 'ALO', 'HUL', 'BUT', 'MAS', 'BOT', 'MAG', 'KVY', 'GRO', 'RAI', 'RIC', 'SUT', 'MAL', 'PER'],	# Malaysia
         ['HAM', 'ROS', 'PER', 'RIC', 'HUL', 'VET', 'MAS', 'BOT', 'ALO', 'RAI', 'KVY', 'GRO', 'MAL', 'BUT', 'MAG', 'SUT'],	# Bahrain
         ['HAM', 'ROS', 'ALO', 'RIC', 'VET', 'HUL', 'BOT', 'RAI', 'PER', 'KVY', 'BUT', 'MAG', 'MAL', 'MAS', 'GRO', 'SUT'],	# China
         ['HAM', 'ROS', 'RIC', 'VET', 'BOT', 'ALO', 'RAI', 'GRO', 'PER', 'HUL', 'BUT', 'MAG', 'MAS', 'KVY', 'MAL', 'SUT'],	# Spain
         ['ROS', 'HAM', 'RIC', 'ALO', 'HUL', 'BUT', 'MAS', 'GRO', 'MAG', 'RAI', 'BOT', 'SUT', 'KVY', 'VET', 'PER', 'MAL'],	# Monaco
         ['RIC', 'ROS', 'VET', 'BUT', 'HUL', 'ALO', 'BOT', 'MAG', 'RAI', 'PER', 'MAS', 'SUT', 'GRO', 'KVY', 'HAM', 'MAL'],	# Canada
         ['ROS', 'HAM', 'BOT', 'MAS', 'ALO', 'PER', 'MAG', 'RIC', 'HUL', 'RAI', 'BUT', 'MAL', 'SUT', 'GRO', 'VET', 'KVY'],	# Austria
         ['HAM', 'BOT', 'RIC', 'BUT', 'VET', 'ALO', 'MAG', 'HUL', 'KVY', 'PER', 'GRO', 'SUT', 'MAL', 'ROS', 'MAS', 'RAI'],	# Great Britain
         ['ROS', 'BOT', 'HAM', 'VET', 'ALO', 'RIC', 'HUL', 'BUT', 'MAG', 'PER', 'RAI', 'MAL', 'SUT', 'KVY', 'GRO', 'MAS'],	# Germany
         ['RIC', 'ALO', 'HAM', 'ROS', 'MAS', 'RAI', 'VET', 'BOT', 'BUT', 'SUT', 'MAG', 'MAL', 'KVY', 'PER', 'HUL', 'GRO'],	# Hungary
         ['RIC', 'ROS', 'BOT', 'RAI', 'VET', 'BUT', 'ALO', 'PER', 'KVY', 'HUL', 'MAG', 'MAS', 'SUT', 'HAM', 'GRO', 'MAL'],	# Belgium
         ['HAM', 'ROS', 'MAS', 'BOT', 'RIC', 'VET', 'PER', 'BUT', 'RAI', 'MAG', 'KVY', 'HUL', 'MAL', 'SUT', 'GRO', 'ALO'],	# Italy
         ['HAM', 'VET', 'RIC', 'ALO', 'MAS', 'PER', 'RAI', 'HUL', 'MAG', 'BOT', 'MAL', 'GRO', 'KVY', 'BUT', 'SUT', 'ROS'],	# Singapore
         ['HAM', 'ROS', 'VET', 'RIC', 'BUT', 'BOT', 'MAS', 'HUL', 'PER', 'KVY', 'RAI', 'MAG', 'GRO', 'MAL', 'SUT', 'ALO'],	# Japan
         ['HAM', 'ROS', 'BOT', 'BUT', 'MAG', 'ALO', 'RIC', 'VET', 'RAI', 'PER', 'MAS', 'HUL', 'KVY', 'SUT', 'GRO', 'MAL'],  # Russia
         ['HAM', 'ROS', 'RIC', 'MAS', 'BOT', 'ALO', 'VET', 'MAG', 'MAL', 'GRO', 'BUT', 'RAI', 'KVY', 'HUL', 'PER', 'SUT'],	# USA
         ['ROS', 'HAM', 'MAS', 'BUT', 'VET', 'ALO', 'RAI', 'HUL', 'MAG', 'BOT', 'KVY', 'MAL', 'PER', 'SUT', 'GRO', 'RIC'],	# Brazil
         ['HAM', 'MAS', 'BOT', 'RIC', 'BUT', 'HUL', 'PER', 'VET', 'ALO', 'RAI', 'MAG', 'GRO', 'ROS', 'SUT', 'MAL']		    	# Abu Dhabi
          ]


tracks = ['Australia', 'Malaysia', 'Bahrain', 'China', 'Spain', 'Monaco', 'Canada', 'Austria', 'Silverstone', 'Hockenheimring',
          'Hungaroring', 'Belgium', 'Monza', 'Singapore', 'Japan', 'Sochi', 'Austin', 'Brazil', 'Yas Marina']

weather_conditions = [1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1]