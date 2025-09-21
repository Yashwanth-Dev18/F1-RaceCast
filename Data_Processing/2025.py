

# ** 2025 - ONLY TILL MONZA **

def getCar(driver):
    if driver == "ANT" or driver == "RUS":
        return "W16 - 2025"
    elif driver == "LEC" or driver == "HAM":
        return "SF-25 - 2025"
    elif driver == "VER" or driver == "TSU":
        return "RB21 - 2025"
    elif driver == "ALB" or driver == "SAI":
        return "FW47 - 2025"
    elif driver == "NOR" or driver == "PIA":
        return "MCL39 - 2025"
    elif driver == "HAD" or driver == "LAW":
        return "VCARB02 - 2025"
    elif driver == "ALO" or driver == "STR":
        return "AMR25 - 2025"
    elif driver == "BOR" or driver == "HUL":
        return "C45 - 2025"
    elif driver == "BEA" or driver == "OCO":
        return "VF-25 - 2025"
    elif driver == "GAS" or driver == "COL":
        return "A525 - 2025"

    else:
        print("Driver not found")
        print("ERROR")
        return "Unknown"
    

races = [['NOR', 'VER', 'RUS', 'ANT', 'ALB', 'STR', 'HUL', 'LEC', 'PIA', 'HAM', 'GAS', 'TSU', 'OCO', 'BEA', 'LAW', 'BOR', 'ALO', 'SAI', 'HAD'], #Australia
         ['PIA', 'NOR', 'RUS', 'VER', 'OCO', 'ANT', 'ALB', 'BEA', 'STR', 'SAI', 'HAD', 'LAW', 'BOR', 'HUL', 'TSU', 'ALO', 'LEC', 'HAM', 'GAS'], #Shanghai
         ['VER', 'NOR', 'PIA', 'LEC', 'RUS', 'ANT', 'HAM', 'HAD', 'ALB', 'BEA', 'ALO', 'TSU', 'GAS', 'SAI', 'HUL', 'LAW', 'OCO', 'BOR', 'STR'], #Japan
         ['PIA', 'RUS', 'NOR', 'LEC', 'HAM', 'VER', 'GAS', 'OCO', 'TSU', 'BEA', 'ANT', 'ALB', 'HAD', 'ALO', 'LAW', 'STR', 'BOR', 'SAI', 'HUL'], #Bahrain
         ['PIA', 'VER', 'LEC', 'NOR', 'RUS', 'ANT', 'HAM', 'SAI', 'ALB', 'HAD', 'ALO', 'LAW', 'BEA', 'OCO', 'HUL', 'STR', 'BOR', 'TSU', 'GAS'], #Saudi Arabia
         ['PIA', 'NOR', 'RUS', 'VER', 'ALB', 'ANT', 'LEC', 'HAM', 'SAI', 'TSU', 'HAD', 'OCO', 'GAS', 'HUL', 'ALO', 'STR', 'LAW', 'BOR', 'BEA'], #Miami
         ['VER', 'NOR', 'PIA', 'HAM', 'ALB', 'LEC', 'RUS', 'SAI', 'HAD', 'TSU', 'ALO', 'HUL', 'GAS', 'LAW', 'STR', 'COL', 'BEA', 'BOR', 'ANT', 'OCO'], #Imola
         ['NOR', 'LEC', 'PIA', 'VER', 'HAM', 'HAD', 'OCO', 'LAW', 'ALB', 'SAI', 'RUS', 'BEA', 'COL', 'BOR', 'STR', 'HUL', 'TSU', 'ANT', 'ALO', 'GAS'], #Monaco
         ['PIA', 'NOR', 'LEC', 'RUS', 'HUL', 'HAM', 'HAD', 'GAS', 'ALO', 'VER', 'LAW', 'BOR', 'TSU', 'SAI', 'COL', 'OCO', 'BEA', 'ANT', 'ALB', 'STR'], #Barcelona
         ['RUS', 'VER', 'ANT', 'PIA', 'LEC', 'HAM', 'ALO', 'HUL', 'OCO', 'SAI', 'BEA', 'TSU', 'COL', 'BOR', 'GAS', 'HAD', 'STR', 'NOR', 'LAW', 'ALB'], #Canada
         ['NOR', 'PIA', 'LEC', 'HAM', 'RUS', 'LAW', 'ALO', 'BOR', 'HUL', 'OCO', 'BEA', 'HAD', 'GAS', 'STR', 'COL', 'TSU', 'ALB', 'VER', 'ANT', 'SAI'], #Austria
         ['NOR', 'PIA', 'HUL', 'HAM', 'VER', 'GAS', 'STR', 'ALB', 'ALO', 'RUS', 'BEA', 'SAI', 'OCO', 'LEC', 'TSU', 'ANT', 'HAD', 'BOR', 'LAW', 'COL'], #Silverstone
         ['PIA', 'NOR', 'LEC', 'VER', 'RUS', 'ALB', 'HAM', 'LAW', 'BOR', 'GAS', 'BEA', 'HUL', 'TSU', 'STR', 'OCO', 'ANT', 'ALO', 'SAI', 'COL', 'HAD'], #Belgium
         ['NOR', 'PIA', 'RUS', 'LEC', 'ALO', 'BOR', 'STR', 'LAW', 'VER', 'ANT', 'HAD', 'HAM', 'HUL', 'SAI', 'ALB', 'OCO', 'TSU', 'COL', 'GAS', 'BEA'], #Hungary
         ['PIA', 'VER', 'HAD', 'RUS', 'ALB', 'BEA', 'STR', 'ALO', 'TSU', 'OCO', 'COL', 'LAW', 'SAI', 'HUL', 'BOR', 'ANT', 'GAS', 'NOR', 'LEC', 'HAM'], #Netherlands
         ['VER', 'NOR', 'PIA', 'LEC', 'RUS', 'HAM', 'ALB', 'BOR', 'ANT', 'HAD', 'SAI', 'BEA', 'TSU', 'LAW', 'OCO', 'GAS', 'COL', 'STR', 'ALO', 'HUL'], #Monza

        ]

tracks = ["melbourne", "shanghai", "suzuka", "sakhir", "jeddah", "miami", "imola", "monaco", "barcelona", "canada", "austria", "silverstone", 
          "belgium", "hungaroring", "netherlands", "monza"]

weather_conditions = [0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1]