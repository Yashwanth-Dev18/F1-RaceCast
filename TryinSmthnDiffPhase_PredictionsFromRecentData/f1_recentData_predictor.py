import pandas as pd
import numpy as np
import joblib

# 1. Load the trained model
model = joblib.load("f1_xgb_mod1.pkl")

# 2. Load dataset to understand the structure
df = pd.read_csv("f1_2020_2025_records.csv")  # replace with your actual CSV path
columns = df.columns.tolist()
columns.remove("race_results")  # remove target

# 3. Get all unique values for each category from the dataset
all_drivers = ['VER', 'TSU', 'NOR', 'PIA', 'LEC', 'HAM', 'RUS', 'ANT', 'SAI', 'ALB', 
               'ALO', 'STR', 'LAW', 'HAD', 'BEA', 'OCO', 'HUL', 'BOR', 'GAS', 'COL', 
               'BOT', 'ZHO', 'RIC', 'PER', 'VET', 'RAI', 'MAG', 'LAT', 'SCH', 'SAR']

all_tracks = ['Sochi Autodrom- Sochi- RUSSIA', 'Mugello Circuit- Scarperia e San Piero- ITALY',
              'Algarve International Circuit- Portimão- PORTUGAL', 'Istanbul Park- Istanbul- TURKEY',
              'Shanghai International Circuit- Shanghai- CHINA', 'Imola (Autodromo Enzo e Dino Ferrari)- Imola- ITALY',
              'Losail International Circuit- Lusail- QATAR', 'Miami International Autodrome- Miami- USA',
              'Jeddah Corniche Circuit- Jeddah- SAUDI ARABIA', 'Circuit Zandvoort- Zandvoort- NETHERLANDS',
              'Albert Park Grand Prix Circuit- Melbourne- AUSTRALIA', 'Bahrain International Circuit- Sakhir- BAHRAIN',
              'Circuit de Barcelona-Catalunya- Barcelona- SPAIN', 'Circuit de Monaco- Monte Carlo- MONACO',
              'Circuit Gilles Villeneuve- Montreal- CANADA', 'Red Bull Ring- Spielberg- AUSTRIA',
              'Silverstone Circuit- Silverstone- UNITED KINGDOM', 'Hungaroring- Budapest- HUNGARY',
              'Circuit de Spa-Francorchamps- Stavelot- BELGIUM', 'Autodromo Nazionale Monza- Monza- ITALY',
              'Marina Bay Street Circuit- Singapore- SINGAPORE', 'Suzuka International Racing Course- Suzuka- JAPAN',
              'Circuit of the Americas- Austin- USA', 'Autódromo Hermanos Rodríguez- Mexico City- MEXICO',
              'Autódromo José Carlos Pace (Interlagos)- São Paulo- BRAZIL', 'Yas Marina Circuit- Abu Dhabi- UNITED ARAB EMIRATES',
              'Las Vegas Street Circuit- Las Vegas- USA', 'Baku City Circuit- Baku- AZERBAIJAN']

all_cars = ['Mercedes: W11 - 2020', 'Ferrari: SF1000 - 2020', 'Red Bull: RB16 - 2020', 'Williams: FW43 - 2020',
            'McLaren: MCL35 - 2020', 'AlphaTauri: AT01 - 2020', 'Racing Point: RP20 - 2020', 'Alfa Romeo: C39 - 2020',
            'Haas: VF-20 - 2020', 'Renault: RS20 - 2020', 'Mercedes: W12 - 2021', 'Ferrari: SF21 - 2021',
            'Red Bull: RB16B - 2021', 'Williams: FW43B - 2021', 'McLaren: MCL35M - 2021', 'AlphaTauri: AT02 - 2021',
            'Aston Martin: AMR21 - 2021', 'Alfa Romeo: C41 - 2021', 'Haas: VF-21 - 2021', 'Alpine: A521 - 2021',
            'Mercedes: W13 - 2022', 'Ferrari: SF-75 - 2022', 'Red Bull: RB18 - 2022', 'Williams: FW44 - 2022',
            'McLaren: MCL36 - 2022', 'AlphaTauri: AT03 - 2022', 'Aston Martin: AMR22 - 2022', 'Alfa Romeo: C42 - 2022',
            'Haas: VF-22 - 2022', 'Alpine: A522 - 2022', 'Mercedes: W14 - 2023', 'Ferrari: SF-23 - 2023',
            'Red Bull: RB19 - 2023', 'Williams: FW45 - 2023', 'McLaren: MCL60 - 2023', 'AlphaTauri: AT04 - 2023',
            'Aston Martin: AMR23 - 2023', 'Alfa Romeo: C43 - 2023', 'Haas: VF-23 - 2023', 'Alpine: A523 - 2023',
            'Mercedes: W15 - 2024', 'Ferrari: SF-24 - 2024', 'Red Bull: RB20 - 2024', 'Williams: FW46 - 2024',
            'McLaren: MCL38 - 2024', 'Racing Bulls: VCARB01 - 2024', 'Aston Martin: AMR24 - 2024', 'Kick Sauber: C44 - 2024',
            'Haas: VF-24 - 2024', 'Alpine: A524 - 2024', 'Mercedes: W16 - 2025', 'Ferrari: SF-25 - 2025',
            'Red Bull: RB21 - 2025', 'Williams: FW47 - 2025', 'McLaren: MCL39 - 2025', 'Racing Bulls: VCARB02 - 2025',
            'Aston Martin: AMR25 - 2025', 'Kick Sauber: C45 - 2025', 'Haas: VF-25 - 2025', 'Alpine: A525 - 2025']

# 4. Function to create an input vector matching the training data format
def create_input_vector(driver, track, car, track_condition):
    # Create an array of zeros with the same length as the training features
    vector = np.zeros(len(columns))
    
    # Find the indices for each input and set them to 1
    # Driver
    if driver in all_drivers:
        idx = all_drivers.index(driver)
        vector[idx] = 1
    
    # Track
    # Find the track that matches the input (case-insensitive partial match)
    matched_track = None
    for t in all_tracks:
        if track.lower() in t.lower():
            matched_track = t
            break
    
    if matched_track:
        idx = len(all_drivers) + all_tracks.index(matched_track)
        vector[idx] = 1
    else:
        raise ValueError(f"Track '{track}' not found in available tracks")
    
    # Car
    # Find the car that matches the input (case-insensitive partial match)
    matched_car = None
    for c in all_cars:
        if car.lower() in c.lower():
            matched_car = c
            break
    
    if matched_car:
        idx = len(all_drivers) + len(all_tracks) + all_cars.index(matched_car)
        vector[idx] = 1
    else:
        raise ValueError(f"Car '{car}' not found in available cars")
    
    # Track condition
    if track_condition.lower() == "dry":
        idx = len(all_drivers) + len(all_tracks) + len(all_cars)
        vector[idx] = 1
    elif track_condition.lower() == "wet":
        idx = len(all_drivers) + len(all_tracks) + len(all_cars) + 1
        vector[idx] = 1
    else:
        raise ValueError("track_condition must be 'dry' or 'wet'")
    
    return vector.reshape(1, -1)

# 5. Function to predict finishing position
def predict_result(driver, track, car, track_condition):
    X_input = create_input_vector(driver, track, car, track_condition)
    pred = model.predict(X_input)
    position = int(round(pred[0]))
    print(f"Predicted finishing position: P{position}")

# 6. Interactive function to get user input
def interactive_prediction():
    print("F1 Grid Position Predictor")
    print("=" * 40)
    
    print("\nAvailable Drivers:")
    for i, driver in enumerate(all_drivers):
        print(f"{driver}", end=", " if (i+1) % 10 != 0 else "\n")
    
    print("\n\nExample Tracks: Baku, Monaco, Silverstone, Spa")
    print("Example Cars: McLaren: MCL39 - 2025, Red Bull: RB21 - 2025")
    print("Track Conditions: dry, wet")
    print("=" * 40)
    
    driver = input("Enter driver code (e.g., HAM): ").strip().upper()
    track = input("Enter track name: ").strip()
    car = input("Enter car (team with year): ").strip()
    track_condition = input("Enter track condition (dry/wet): ").strip().lower()
    
    try:
        predict_result(driver, track, car, track_condition)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 7. Example usage
if __name__ == "__main__":
    # You can use either direct function call or interactive mode
    
    # Direct example:
    print("Direct example prediction:")
    predict_result(
        driver="HAM",
        track="Baku",
        car="Mercedes: W16 - 2025",
        track_condition="dry"
    )
    
    print("\n" + "="*40 + "\n")
    
    # Interactive mode:
    interactive_prediction()