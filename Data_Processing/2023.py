



def getCar(driver):
    if driver == "HAM" or driver == "RUS":
        return "W14 - 2023"
    elif driver == "LEC" or driver == "SAI":
        return "SF-23 - 2023"
    elif driver == "VER" or driver == "PER":
        return "RB19 - 2023"
    elif driver == "ALB" or driver == "SAR":
        return "FW45 - 2023"
    elif driver == "NOR" or driver == "PIA":
        return "MCL60 - 2023"
    elif driver == "TSU" or driver == "RIC" or driver == "LAW":
        return "AT04 - 2023"
    elif driver == "ALO" or driver == "STR":
        return "AMR23 - 2023"
    elif driver == "BOT" or driver == "ZHO":
        return "C43 - 2023"
    elif driver == "HUL" or driver == "MAG":
        return "VF-23 - 2023"
    elif driver == "GAS" or driver == "OCO":
        return "A523 - 2023"
    
    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['VER', 'PER', 'ALO', 'SAI', 'HAM', 'STR', 'RUS', 'BOT', 'GAS', 'ALB', 'TSU', 'SAR', 'MAG', 'HUL', 'ZHO', 'NOR', 'OCO', 'LEC', 'PIA'], #Bahrain
         ['PER', 'VER', 'ALO', 'RUS', 'HAM', 'SAI', 'LEC', 'OCO', 'GAS', 'MAG', 'TSU', 'HUL', 'ZHO', 'PIA', 'SAR', 'NOR', 'BOT', 'ALB', 'STR'], #Saudi Arabia
         ['VER', 'HAM', 'ALO', 'STR', 'PER', 'NOR', 'HUL', 'PIA', 'ZHO', 'TSU', 'BOT', 'SAI', 'GAS', 'OCO', 'SAR', 'MAG', 'RUS', 'ALB', 'LEC'], #Australia
         ['PER', 'VER', 'LEC', 'ALO', 'SAI', 'HAM', 'STR', 'RUS', 'NOR', 'TSU', 'PIA', 'ALB', 'MAG', 'GAS', 'OCO', 'SAR', 'HUL', 'BOT', 'ZHO'], #Azerbaijan
         ['VER', 'PER', 'ALO', 'RUS', 'SAI', 'HAM', 'LEC', 'GAS', 'OCO', 'MAG', 'TSU', 'STR', 'BOT', 'ALB', 'HUL', 'ZHO', 'NOR', 'PIA', 'SAR'], #Miami
         ['VER', 'PER', 'LEC', 'ALO', 'SAI', 'HAM', 'RUS', 'OCO', 'GAS', 'MAG', 'TSU', 'STR', 'BOT', 'ALB', 'HUL', 'ZHO', 'NOR', 'PIA', 'SAR'], #Monaco
         ['VER', 'HAM', 'RUS', 'PER', 'SAI', 'STR', 'ALO', 'OCO', 'ZHO', 'GAS', 'LEC', 'TSU', 'PIA', 'HUL', 'ALB', 'NOR', 'MAG', 'BOT', 'SAR'], #Spain
         ['VER', 'ALO', 'HAM', 'LEC', 'SAI', 'PER', 'ALB', 'OCO', 'STR', 'BOT', 'PIA', 'GAS', 'NOR', 'TSU', 'HUL', 'ZHO', 'MAG', 'RUS', 'SAR'], #Canada
         ['VER', 'LEC', 'PER', 'NOR', 'ALO', 'SAI', 'RUS', 'HAM', 'STR', 'GAS', 'ALB', 'ZHO', 'SAR', 'OCO', 'BOT', 'PIA', 'MAG', 'TSU', 'HUL'], #Austria
         ['VER', 'NOR', 'HAM', 'PIA', 'RUS', 'PER', 'ALO', 'ALB', 'LEC', 'SAI', 'SAR', 'BOT', 'HUL', 'STR', 'ZHO', 'TSU', 'GAS', 'MAG', 'OCO'], #Silverstone
         ['VER', 'NOR', 'PER', 'HAM', 'PIA', 'RUS', 'LEC', 'SAI', 'ALO', 'STR', 'ALB', 'BOT', 'RIC', 'HUL', 'TSU', 'ZHO', 'MAG', 'SAR', 'OCO', 'GAS'], #Hungary
         ['VER', 'PER', 'LEC', 'HAM', 'ALO', 'RUS', 'NOR', 'OCO', 'STR', 'TSU', 'GAS', 'BOT', 'ZHO', 'ALB', 'MAG', 'RIC', 'SAR', 'HUL', 'SAI', 'PIA'], #Belgium
         ['VER', 'ALO', 'GAS', 'PER', 'SAI', 'HAM', 'NOR', 'ALB', 'PIA', 'OCO', 'STR', 'HUL', 'LAW', 'MAG', 'BOT', 'TSU', 'RUS', 'ZHO', 'LEC', 'SAR'], #Netherlands
         ['VER', 'PER', 'SAI', 'LEC', 'RUS', 'HAM', 'ALB', 'NOR', 'ALO', 'BOT', 'LAW', 'PIA', 'SAR', 'ZHO', 'GAS', 'STR', 'HUL', 'MAG', 'OCO', 'TSU'], #Monza
         ['SAI', 'NOR', 'HAM', 'LEC', 'VER', 'GAS', 'PIA', 'PER', 'LAW', 'MAG', 'ALB', 'ZHO', 'HUL', 'SAR', 'ALO', 'RUS', 'BOT', 'OCO', 'TSU', 'STR'], #Singapore
         ['VER', 'NOR', 'PIA', 'LEC', 'HAM', 'SAI', 'RUS', 'ALO', 'OCO', 'GAS', 'LAW', 'TSU', 'ZHO', 'HUL', 'MAG', 'ALB', 'SAR', 'STR', 'PER', 'BOT'], #Japan
         ['VER', 'PIA', 'NOR', 'RUS', 'LEC', 'ALO', 'OCO', 'BOT', 'ZHO', 'PER', 'STR', 'GAS', 'ALB', 'MAG', 'TSU', 'HUL', 'LAW', 'SAR', 'HAM', 'SAI'], #Qatar
         ['VER', 'NOR', 'SAI', 'PER', 'RUS', 'GAS', 'STR', 'TSU', 'ALB', 'SAR', 'HUL', 'BOT', 'ZHO', 'MAG', 'RIC', 'ALO', 'PIA', 'OCO', 'HAM', 'LEC'], #Austin
         ['VER', 'HAM', 'LEC', 'SAI', 'NOR', 'RUS', 'RIC', 'PIA', 'ALB', 'OCO', 'GAS', 'TSU', 'HUL', 'ZHO', 'BOT', 'SAR', 'STR', 'ALO', 'MAG', 'PER'], #Mexico
         ['VER', 'NOR', 'ALO', 'PER', 'STR', 'SAI', 'GAS', 'HAM', 'TSU', 'OCO', 'SAR', 'HUL', 'RIC', 'PIA', 'RUS', 'BOT', 'ZHO', 'MAG', 'ALB', 'LEC'], #Brazil
         ['VER', 'LEC', 'PER', 'OCO', 'STR', 'SAI', 'HAM', 'RUS', 'ALO', 'PIA', 'GAS', 'ALB', 'MAG', 'RIC', 'ZHO', 'SAR', 'BOT', 'TSU', 'HUL', 'NOR'], #Las Vegas
         ['VER', 'LEC', 'RUS', 'PER', 'NOR', 'PIA', 'ALO', 'TSU', 'HAM', 'STR', 'RIC', 'OCO', 'GAS', 'ALB', 'HUL', 'SAR', 'ZHO', 'SAI', 'BOT', 'MAG'] #Yas Marina
          ]


tracks = ["sakhir", "jeddah", "melbourne", "Baku", "Miami", "Monaco", "Barcelona", "Canada",
          "austria", "Silverstone", "Hungaroring", "Belgium", "Zandvoort", "Monza", "Singapore", "Suzuka", "Qatar", "Austin",
          "Mexico", "brazil", "Las Vegas", "Yas Marina"]

weather_conditions = [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1]