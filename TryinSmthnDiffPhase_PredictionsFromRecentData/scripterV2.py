# import csv


# def generate_rows(races, tracks, weather_conditions, csv_file, row_start):
#     # dataset columns
#     #30 DRIVERS, 28 CIRCUITS, 60 CARS, 1 RACE RESULT = 119 columns
#     columns = [
#         "race_results","VER","TSU","NOR","PIA","LEC","HAM","RUS","ANT","SAI","ALB","ALO","STR",
#         "LAW","HAD","BEA","OCO","HUL","BOR","GAS","COL","BOT","ZHO","RIC","PER","VET","RAI",
#         "MAG","LAT","SCH","SAR", 
#         "Sochi Autodrom- Sochi- RUSSIA","Mugello Circuit- Scarperia e San Piero- ITALY",
#         "Algarve International Circuit- Portimão- PORTUGAL","Istanbul Park- Istanbul- TURKEY","Shanghai International Circuit- Shanghai- CHINA",
#         "Imola (Autodromo Enzo e Dino Ferrari)- Imola- ITALY","Losail International Circuit- Lusail- QATAR","Miami International Autodrome- Miami- USA",
#         "Jeddah Corniche Circuit- Jeddah- SAUDI ARABIA","Circuit Zandvoort- Zandvoort- NETHERLANDS","Albert Park Grand Prix Circuit- Melbourne- AUSTRALIA",
#         "Bahrain International Circuit- Sakhir- BAHRAIN","Circuit de Barcelona-Catalunya- Barcelona- SPAIN","Circuit de Monaco- Monte Carlo- MONACO","Circuit Gilles Villeneuve- Montreal- CANADA",
#         "Red Bull Ring- Spielberg- AUSTRIA","Silverstone Circuit- Silverstone- UNITED KINGDOM","Hungaroring- Budapest- HUNGARY","Circuit de Spa-Francorchamps- Stavelot- BELGIUM",
#         "Autodromo Nazionale Monza- Monza- ITALY","Marina Bay Street Circuit- Singapore- SINGAPORE","Suzuka International Racing Course- Suzuka- JAPAN","Circuit of the Americas- Austin- USA","Autódromo Hermanos Rodríguez- Mexico City- MEXICO",
#         "Autódromo José Carlos Pace (Interlagos)- São Paulo- BRAZIL","Yas Marina Circuit- Abu Dhabi- UNITED ARAB EMIRATES","Las Vegas Street Circuit- Las Vegas- USA","Baku City Circuit- Baku- AZERBAIJAN",
#         "Mercedes: W11 - 2020","Ferrari: SF1000 - 2020","Red Bull: RB16 - 2020","Williams: FW43 - 2020","McLaren: MCL35 - 2020","AlphaTauri: AT01 - 2020","Racing Point: RP20 - 2020","Alfa Romeo: C39 - 2020","Haas: VF-20 - 2020","Renault: RS20 - 2020",
#         "Mercedes: W12 - 2021","Ferrari: SF21 - 2021","Red Bull: RB16B - 2021","Williams: FW43B - 2021","McLaren: MCL35M - 2021","AlphaTauri: AT02 - 2021","Aston Martin: AMR21 - 2021","Alfa Romeo: C41 - 2021","Haas: VF-21 - 2021","Alpine: A521 - 2021",
#         "Mercedes: W13 - 2022","Ferrari: SF-75 - 2022","Red Bull: RB18 - 2022","Williams: FW44 - 2022","McLaren: MCL36 - 2022","AlphaTauri: AT03 - 2022","Aston Martin: AMR22 - 2022","Alfa Romeo: C42 - 2022","Haas: VF-22 - 2022","Alpine: A522 - 2022",
#         "Mercedes: W14 - 2023","Ferrari: SF-23 - 2023","Red Bull: RB19 - 2023","Williams: FW45 - 2023","McLaren: MCL60 - 2023","AlphaTauri: AT04 - 2023","Aston Martin: AMR23 - 2023","Alfa Romeo: C43 - 2023","Haas: VF-23 - 2023","Alpine: A523 - 2023",
#         "Mercedes: W15 - 2024","Ferrari: SF-24 - 2024","Red Bull: RB20 - 2024","Williams: FW46 - 2024","McLaren: MCL38 - 2024","Racing Bulls: VCARB01 - 2024","Aston Martin: AMR24 - 2024","Kick Sauber: C44 - 2024","Haas: VF-24 - 2024","Alpine: A524 - 2024",
#         "Mercedes: W16 - 2025","Ferrari: SF-25 - 2025","Red Bull: RB21 - 2025","Williams: FW47 - 2025","McLaren: MCL39 - 2025","Racing Bulls: VCARB02 - 2025","Aston Martin: AMR25 - 2025","Kick Sauber: C45 - 2025","Haas: VF-25 - 2025","Alpine: A525 - 2025"
#     ]
#     driver_columns = columns[1:31]  # only driver columns
#     track_columns = columns[31:59]  # only "track" columns
#     car_columns = columns[59:]  # only "car" columns

#     # create the new rows
#     new_rows = []
#     tracks_index = -1
#     weather_index = -1
#     if not(len(races) == len(tracks) == len(weather_conditions)):
#         print("[ERROR] Races, tracks and weather conditions must be the same length.")
#     for race in races:
#         tracks_index += 1
#         weather_index += 1
#         for idx, driver in enumerate(race, start=1):
#             driver = driver.lower()
#             row = [idx]
#             # ____DRIVERS____
#             driver_entries = 0
#             for d_col in driver_columns:
#                 if d_col.lower() == driver[:3]:
#                   row.append(1)
#                   driver_entries += 1
#                 else:
#                   row.append(0)

#             if driver_entries != 1:
#                 print(f"[ERROR] Driver not found: {driver.upper()} in race {tracks_index+1}, row {row_start + len(new_rows)}")
            
#             # ____TRACKS____
#             track = tracks[tracks_index]
#             track = track.lower()
#             track_entries = 0
#             for t_col in track_columns:
#                 if track in t_col.lower():
#                     row.append(1)
#                     track_entries += 1
#                 else:
#                     row.append(0)
#             if track_entries != 1:
#                 print(f"[ERROR] Track not matched: '{track.upper()}' in race {tracks_index+1}, row {row_start + len(new_rows)}")

#             # ____CARS____
#             car_entries = 0
#             for c_col in car_columns:
#                 if getCar(driver.upper()) is None:
#                   print(f"getCar() returned None for driver: {driver.upper()}")
#                 if getCar(driver.upper()) in c_col:
#                     row.append(1)
#                     car_entries += 1
#                 else:
#                     row.append(0)
#             if car_entries != 1:
#                 print(f"[ERROR] Car not matched for driver {driver.upper()} -({getCar(driver.upper())}) in race {tracks_index+1}, row {row_start + len(new_rows)}")
            
#             # ____WEATHER____
#             weather_entries = 0
#             weather_condition = weather_conditions[weather_index]
#             if weather_condition == 1:
#                 row.append(1)
#                 row.append(0)
#                 weather_entries += 1
#             elif weather_condition == 0:
#                 row.append(0)
#                 row.append(1)
#                 weather_entries += 1
#             else:
#                 print(f"[ERROR] Weather condition invalid: {weather_condition} in race {tracks_index+1}, row {row_start + len(new_rows)}")
#             if weather_entries != 1:
#                 print(f"[ERROR] Weather condition not matched: {weather_condition} in race {tracks_index+1}, row {row_start + len(new_rows)}")

#             new_rows.append(row)
#         #new_rows.append([])  # blank row after each race

#     # read existing file
#     with open(csv_file, "r", newline="", encoding="utf-8") as f:
#         reader = list(csv.reader(f))

#     # ensure at least "row_start-1" rows exist before inserting
#     while len(reader) < row_start-1:
#         reader.append([""]*len(columns))

#     # insert new rows starting at "row_start"
#     for i, row in enumerate(new_rows):
#         if len(reader) > row_start-1 + i:
#             reader[row_start-1 + i] = row
#         else:
#             reader.append(row)

#     # write back to file
#     with open(csv_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerows(reader)


# generate_rows(races, tracks, weather_conditions, "f1_2020_2025_records.csv", 2300)