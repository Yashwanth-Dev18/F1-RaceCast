


def getCar(driver):
    if driver == "VER" or driver == "PER":
        return "RB20 - 2024"
    elif driver == "LEC" or driver == "SAI":
        return "SF-24 - 2024"
    elif driver == "HAM" or driver == "RUS":
        return "W15 - 2024"
    elif driver == "NOR" or driver == "PIA":
        return "MCL38 - 2024"
    elif driver == "ALO" or driver == "STR":
        return "AMR24 - 2024"
    elif driver == "TSU" or driver == "RIC" or driver == "LAW":
        return "VCARB01 - 2024"
    elif driver == "HUL" or driver == "MAG" or driver == "BEA":
        return "VF-24 - 2024"
    elif driver == "BOT" or driver == "ZHO":
        return "C44 - 2024"
    elif driver == "GAS" or driver == "OCO":
        return "A524 - 2024"
    elif driver == "ALB" or driver == "COL" or driver == "SAR":
        return "FW46 - 2024"
    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['VER', 'PER', 'SAI', 'LEC', 'RUS', 'NOR', 'HAM', 'PIA', 'ALO', 'STR', 'ZHO', 'MAG', 'RIC', 'TSU', 'ALB', 'HUL', 'OCO', 'GAS', 'BOT', 'SAR'], # Bahrain
           ['VER', 'PER', 'LEC', 'PIA', 'ALO', 'RUS', 'BEA', 'NOR', 'HAM', 'HUL', 'ALB', 'MAG', 'OCO', 'TSU', 'SAR', 'RIC', 'BOT', 'ZHO', 'STR', 'GAS'], # Saudi
           ['SAI', 'LEC', 'NOR', 'PIA', 'PER', 'STR', 'TSU', 'ALO', 'HUL', 'MAG', 'ALB', 'RIC', 'GAS', 'BOT', 'ZHO', 'OCO', 'RUS', 'HAM', 'VER'], # Australia
           ['VER', 'PER', 'SAI', 'LEC', 'NOR', 'ALO', 'RUS', 'PIA', 'HAM', 'TSU', 'HUL', 'STR', 'MAG', 'BOT', 'OCO', 'GAS', 'SAR', 'ZHO', 'RIC', 'ALB'], # Japan
           ["VER", "NOR", "PER", "LEC", "SAI", "RUS", "ALO", "PIA", "HAM", "HUL", "OCO", "ALB", "GAS", "ZHO", "STR", "MAG", "SAR", "RIC", "TSU", 'BOT'], # China
           ["NOR", "VER", "LEC", "PER", "SAI", "HAM", "TSU", "RUS", "ALO", "OCO", "HUL", "GAS", "PIA", "ZHO", "RIC", "BOT", "STR", "MAG", "ALB", "SAR"],  # Miami
           ["VER", "NOR", "LEC", "PIA", "SAI", "HAM", "RUS", "PER", "STR", "TSU", "HUL", "MAG", "RIC", "OCO", "ZHO", "GAS", "SAR", "BOT", "ALO", "ALB"], # Imola
           ['LEC', 'PIA', 'SAI', 'NOR', 'RUS', 'VER', 'HAM', 'TSU', 'ALB', 'GAS', 'ALO', 'RIC', 'BOT', 'STR', 'SAR', 'ZHO', 'OCO', 'PER', 'HUL', 'MAG'], # Monaco
           ['VER', 'NOR', 'RUS', 'HAM', 'PIA', 'ALO', 'STR', 'RIC', 'GAS', 'HUL', 'MAG', 'BOT', 'TSU', 'ZHO', 'SAI', 'ALB', 'PER', 'LEC', 'SAR'], # Canada
           ['VER', 'NOR', 'HAM', 'RUS', 'LEC', 'SAI', 'PIA', 'PER', 'GAS', 'OCO', 'HUL', 'ALO', 'ZHO', 'STR', 'RIC', 'BOT', 'MAG', 'ALB', 'TSU', 'SAR'], # Spain
           ['RUS', 'PIA', 'SAI', 'HAM', 'VER', 'HUL', 'PER', 'MAG', 'RIC', 'GAS', 'LEC', 'OCO', 'STR', 'TSU', 'ALB', 'BOT', 'ZHO', 'ALO', 'SAR', 'NOR'], # Austria
           ['HAM', 'VER', 'NOR', 'PIA', 'SAI', 'HUL', 'STR', 'ALO', 'ALB', 'TSU', 'SAR', 'MAG', 'RIC', 'LEC', 'BOT', 'OCO', 'PER', 'ZHO', 'RUS', 'GAS'], # Silverstone
           ['PIA', 'NOR', 'HAM', 'LEC', 'VER', 'SAI', 'PER', 'RUS', 'TSU', 'STR', 'ALO', 'RIC', 'HUL', 'ALB', 'MAG', 'BOT', 'SAR', 'OCO', 'ZHO', 'GAS'], # Hungary
           ['HAM', 'PIA', 'LEC', 'VER', 'NOR', 'SAI', 'PER', 'ALO', 'OCO', 'RIC', 'STR', 'ALB', 'GAS', 'MAG', 'BOT', 'TSU', 'SAR', 'HUL', 'ZHO', 'RUS'], # Belgium
           ['NOR', 'VER', 'LEC', 'PIA', 'SAI', 'PER', 'RUS', 'HAM', 'GAS', 'ALO', 'HUL', 'RIC', 'STR', 'ALB', 'OCO', 'SAR', 'TSU', 'MAG', 'BOT', 'ZHO'], # Netherlands
           ['LEC', 'PIA', 'NOR', 'SAI', 'HAM', 'VER', 'RUS', 'PER', 'ALB', 'MAG', 'ALO', 'COL', 'RIC', 'OCO', 'GAS', 'BOT', 'HUL', 'ZHO', 'STR', 'TSU'], # Italy
           ['PIA', 'LEC', 'RUS', 'NOR', 'VER', 'ALO', 'ALB', 'COL', 'HAM', 'BEA', 'HUL', 'GAS', 'RIC', 'ZHO', 'OCO', 'BOT', 'PER', 'SAI', 'STR', 'TSU'], # Baku
           ['NOR', 'VER', 'PIA', 'RUS', 'LEC', 'HAM', 'SAI', 'ALO', 'HUL', 'PER', 'COL', 'TSU', 'OCO', 'STR', 'ZHO', 'BOT', 'GAS', 'RIC', 'MAG', 'ALB'], # Singapore
           ['LEC', 'SAI', 'VER', 'NOR', 'PIA', 'RUS', 'PER', 'HUL', 'LAW', 'COL', 'MAG', 'GAS', 'ALO', 'TSU', 'STR', 'ALB', 'BOT', 'OCO', 'ZHO', 'HAM'], # Austin
           ['SAI', 'NOR', 'LEC', 'HAM', 'RUS', 'VER', 'MAG', 'PIA', 'HUL', 'GAS', 'STR', 'COL', 'OCO', 'BOT', 'ZHO', 'LAW', 'PER', 'ALO', 'ALB', 'TSU'], # Mexico
           ['VER', 'OCO', 'GAS', 'RUS', 'LEC', 'NOR', 'TSU', 'PIA', 'LAW', 'HAM', 'PER', 'BEA', 'BOT', 'ALO', 'ZHO', 'SAI', 'COL', 'HUL', 'ALB', 'STR'], # Brazil
           ['RUS', 'HAM', 'SAI', 'LEC', 'VER', 'NOR', 'PIA', 'HUL', 'TSU', 'PER', 'ALO', 'MAG', 'ZHO', 'COL', 'STR', 'LAW', 'OCO', 'BOT', 'ALB', 'GAS'], # Las Vegas
           ['VER', 'LEC', 'PIA', 'RUS', 'GAS', 'SAI', 'ALO', 'ZHO', 'MAG', 'NOR', 'BOT', 'HAM', 'TSU', 'LAW', 'ALB', 'HUL', 'PER', 'STR', 'COL', 'OCO'], # Qatar
           ['NOR', 'SAI', 'LEC', 'HAM', 'RUS', 'VER', 'GAS', 'HUL', 'ALO', 'PIA', 'ALB', 'TSU', 'ZHO', 'STR', 'MAG', 'LAW', 'BOT', 'COL', 'PER'] # Yas Marina

          ]

tracks = ["sakhir", "jeddah", "melbourne", "suzuka", "shanghai", "Miami", "Imola", "Monaco", "Canada", "Barcelona",
          "austria", "Silverstone", "Hungaroring", "belgium", "Netherlands", "Monza", "Baku", "Singapore", "Austin",
          "Mexico", "brazil", "Las Vegas", "qatar", "Yas Marina"]

weather_conditions = [1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1]
