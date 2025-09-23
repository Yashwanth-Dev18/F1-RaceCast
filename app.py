import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cache the model loading
@st.cache_resource
def load_model_and_features():
    model = joblib.load("f1_gb_main_model.pkl")
    df = pd.read_csv("f1records.csv")
    feature_columns = df.drop(columns=['race_results']).columns.tolist()
    return model, feature_columns

# Loading model and features
model, feature_columns = load_model_and_features()

# MAPPING DRIVERS' NAMES TO ABBREVIATIONS
DRIVER_MAPPING = {
    'Max Verstappen': 'VER', 'Yuki Tsunoda': 'TSU', 'Lando Norris': 'NOR', 
    'Oscar Piastri': 'PIA', 'Charles Leclerc': 'LEC', 'Lewis Hamilton': 'HAM',
    'George Russell': 'RUS', 'Andrea Kimi Antonelli': 'ANT', 'Carlos Sainz': 'SAI',
    'Alexander Albon': 'ALB', 'Fernando Alonso': 'ALO', 'Lance Stroll': 'STR',
    'Liam Lawson': 'LAW', 'Isack Hadjar': 'HAD', 'Ollie Bearman': 'BEA',
    'Esteban Ocon': 'OCO', 'Nico Hulkenberg': 'HUL', 'Gabriel Bortoleto': 'BOR',
    'Pierre Gasly': 'GAS', 'Franco Colapinto': 'COL', 'Valtteri Bottas': 'BOT',
    'Guanyu Zhou': 'ZHO', 'Daniel Ricciardo': 'RIC', 'Sergio Pérez': 'PER',
    'Sebastian Vettel': 'VET', 'Nico Rosberg': 'ROS', 'Kevin Magnussen': 'MAG',
    'Mick Schumacher': 'SCH', 'Kimi Räikkönen': 'RAI', 'Romain Grosjean': 'GRO',
    'Daniil Kvyat': 'KVY', 'Nicholas Latifi': 'LAT', 'Marcus Ericsson': 'ERI',
    'Felipe Massa': 'MAS', 'Jenson Button': 'BUT', 'Felipe Nasr': 'NAS',
    'Pastor Maldonado': 'MAL', 'Jolyon Palmer': 'PAL', 'Stoffel Vandoorne': 'VAN',
    'Logan Sargeant': 'SAR', 'Adrian Sutil': 'SUT'
}

# CIRCUITS
CIRCUITS = [
    "Sochi Autodrom- Sochi- RUSSIA", "Hockenheimring- Hockenheim- GERMANY",
    "Nürburgring GP-Strecke- Nürburg- GERMANY", "Mugello Circuit- Scarperia e San Piero- ITALY",
    "Algarve International Circuit- Portimão- PORTUGAL", "Istanbul Park- Istanbul- TURKEY",
    "Circuit Paul Ricard- Le Castellet- FRANCE", "Shanghai International Circuit- Shanghai- CHINA",
    "Imola (Autodromo Enzo e Dino Ferrari)- Imola- ITALY", "Losail International Circuit- Lusail- QATAR",
    "Miami International Autodrome- Miami- USA", "Jeddah Corniche Circuit- Jeddah- SAUDI ARABIA",
    "Circuit Zandvoort- Zandvoort- NETHERLANDS", "Albert Park Grand Prix Circuit- Melbourne- AUSTRALIA",
    "Bahrain International Circuit- Sakhir- BAHRAIN", "Circuit de Barcelona-Catalunya- Barcelona- SPAIN",
    "Circuit de Monaco- Monte Carlo- MONACO", "Circuit Gilles Villeneuve- Montreal- CANADA",
    "Red Bull Ring- Spielberg- AUSTRIA", "Silverstone Circuit- Silverstone- UNITED KINGDOM",
    "Hungaroring- Budapest- HUNGARY", "Circuit de Spa-Francorchamps- Stavelot- BELGIUM",
    "Autodromo Nazionale Monza- Monza- ITALY", "Marina Bay Street Circuit- Singapore- SINGAPORE",
    "Suzuka International Racing Course- Suzuka- JAPAN", "Circuit of the Americas- Austin- USA",
    "Autódromo Hermanos Rodríguez- Mexico City- MEXICO", "Autódromo José Carlos Pace (Interlagos)- São Paulo- BRAZIL",
    "Yas Marina Circuit- Abu Dhabi- UNITED ARAB EMIRATES", "Las Vegas Street Circuit- Las Vegas- USA",
    "Baku City Circuit- Baku- AZERBAIJAN", "Sepang International Circuit- Sepang- MALAYSIA"
]

# MAPPING TEAM NAMES TO CARS FOR BETTER ACCESSIBILITY
TEAM_CARS = {
    'Mercedes': [
        'Mercedes: W05 - 2014', 'Mercedes: W06 - 2015', 'Mercedes: W07 - 2016',
        'Mercedes: W08 - 2017', 'Mercedes: W09 - 2018', 'Mercedes: W10 - 2019',
        'Mercedes: W11 - 2020', 'Mercedes: W12 - 2021', 'Mercedes: W13 - 2022',
        'Mercedes: W14 - 2023', 'Mercedes: W15 - 2024', 'Mercedes: W16 - 2025'
    ],
    'Ferrari': [
        'Ferrari: SF14-T - 2014', 'Ferrari: SF15-T - 2015', 'Ferrari: SF16-H - 2016',
        'Ferrari: SF70H - 2017', 'Ferrari: SF71H - 2018', 'Ferrari: SF90 - 2019',
        'Ferrari: SF1000 - 2020', 'Ferrari: SF21 - 2021', 'Ferrari: SF-75 - 2022',
        'Ferrari: SF-23 - 2023', 'Ferrari: SF-24 - 2024', 'Ferrari: SF-25 - 2025'
    ],
    'Red Bull': [
        'Red Bull: RB10 - 2014', 'Red Bull: RB11 - 2015', 'Red Bull: RB12 - 2016',
        'Red Bull: RB13 - 2017', 'Red Bull: RB14 - 2018', 'Red Bull: RB15 - 2019',
        'Red Bull: RB16 - 2020', 'Red Bull: RB16B - 2021', 'Red Bull: RB18 - 2022',
        'Red Bull: RB19 - 2023', 'Red Bull: RB20 - 2024', 'Red Bull: RB21 - 2025'
    ],
    'Williams': [
        'Williams: FW36 - 2014', 'Williams: FW37 - 2015', 'Williams: FW38 - 2016',
        'Williams: FW40 - 2017', 'Williams: FW41 - 2018', 'Williams: FW42 - 2019',
        'Williams: FW43 - 2020', 'Williams: FW43B - 2021', 'Williams: FW44 - 2022',
        'Williams: FW45 - 2023', 'Williams: FW46 - 2024', 'Williams: FW47 - 2025'
    ],
    'McLaren': [
        'McLaren: MP4-29 - 2014', 'McLaren: MP4-30 - 2015', 'McLaren: MP4-31 - 2016',
        'McLaren: MCL32 - 2017', 'McLaren: MCL33 - 2018', 'McLaren: MCL34 - 2019',
        'McLaren: MCL35 - 2020', 'McLaren: MCL35M - 2021', 'McLaren: MCL36 - 2022',
        'McLaren: MCL60 - 2023', 'McLaren: MCL38 - 2024', 'McLaren: MCL39 - 2025'
    ],
    'Alpine/Renault': [
        'Renault: RS16 - 2016', 'Renault: RS17 - 2017', 'Renault: RS18 - 2018',
        'Renault: RS19 - 2019', 'Renault: RS20 - 2020', 'Alpine: A521 - 2021',
        'Alpine: A522 - 2022', 'Alpine: A523 - 2023', 'Alpine: A524 - 2024',
        'Alpine: A525 - 2025'
    ],
    'Aston Martin / Racing Point / Force India': [
        'Force India: VJM07 - 2014', 'Force India: VJM08 - 2015', 'Force India: VJM09 - 2016',
        'Force India: VJM10 - 2017', 'Force India: VJM11 - 2018', 'Racing Point: RP19 - 2019',
        'Racing Point: RP20 - 2020', 'Aston Martin: AMR21 - 2021', 'Aston Martin: AMR22 - 2022',
        'Aston Martin: AMR23 - 2023', 'Aston Martin: AMR24 - 2024', 'Aston Martin: AMR25 - 2025'
    ],
    'Racing Bulls / AlphaTauri / Toro Rosso': [
        'Toro Rosso: STR9 - 2014', 'Toro Rosso: STR10 - 2015', 'Toro Rosso: STR11 - 2016',
        'Toro Rosso: STR12 - 2017', 'Toro Rosso: STR13 - 2018', 'Toro Rosso: STR14 - 2019',
        'AlphaTauri: AT01 - 2020', 'AlphaTauri: AT02 - 2021', 'AlphaTauri: AT03 - 2022',
        'AlphaTauri: AT04 - 2023', 'Racing Bulls: VCARB01 - 2024', 'Racing Bulls: VCARB02 - 2025'
    ],
    'Kick Sauber / Alfa Romeo / Sauber': [
        'Sauber: C33 - 2014', 'Sauber: C34 - 2015', 'Sauber: C35 - 2016',
        'Sauber: C36 - 2017', 'Sauber: C37 - 2018', 'Alfa Romeo: C38 - 2019',
        'Alfa Romeo: C39 - 2020', 'Alfa Romeo: C41 - 2021', 'Alfa Romeo: C42 - 2022',
        'Alfa Romeo: C43 - 2023', 'Kick Sauber: C44 - 2024', 'Kick Sauber: C45 - 2025'
    ],
    'Haas': [
        'Haas: VF-16 - 2016', 'Haas: VF-17 - 2017', 'Haas: VF-18 - 2018',
        'Haas: VF-19 - 2019', 'Haas: VF-20 - 2020', 'Haas: VF-21 - 2021',
        'Haas: VF-22 - 2022', 'Haas: VF-23 - 2023', 'Haas: VF-24 - 2024',
        'Haas: VF-25 - 2025'
    ],
    'Lotus': [
        'Lotus: E22 - 2014', 'Lotus: E23 - 2015'
    ]
}

# MAPPING WEATHER TO TRACK CONDITIONS
WEATHER_MAPPING = {
    'Sunny/Cloudy': 'dry_track',
    'Rainy': 'wet_track'
}

# Function to create input vector
def create_input_vector(driver_code, circuit, car, weather_condition):
    vector = np.zeros(len(feature_columns))
    
    # Set driver column
    driver_col = driver_code
    if driver_col in feature_columns:
        idx = feature_columns.index(driver_col)
        vector[idx] = 1

    # Set circuit column (exact match)
    if circuit in feature_columns:
        idx = feature_columns.index(circuit)
        vector[idx] = 1

    # Set car column (exact match)
    if car in feature_columns:
        idx = feature_columns.index(car)
        vector[idx] = 1

    # Set weather condition
    if weather_condition in feature_columns:
        idx = feature_columns.index(weather_condition)
        vector[idx] = 1

    return vector.reshape(1, -1)


# I'm adding this to the Streamlit UI
st.set_page_config(page_title="F1: RaceCast", page_icon="🏎️", layout="wide")

st.title("🏎️ F1:RaceCast    - A race result predictor")
st.markdown("Predicts finishing positions based on driver, car, circuit, and weather conditions.")

# Input section
col1, col2 = st.columns(2)

with col1:
    # Driver selection
    driver_full = st.selectbox("Select Driver", list(DRIVER_MAPPING.keys()))
    driver_code = DRIVER_MAPPING[driver_full]
    
    # Circuit selection
    circuit = st.selectbox("Select Circuit", CIRCUITS)

with col2:
    # Team selection
    team = st.selectbox("Select Team", list(TEAM_CARS.keys()))
    
    # Car selection based on team
    team_cars = TEAM_CARS[team]
    car = st.selectbox("Select Car", team_cars)
    
    # Weather selection
    weather_display = st.selectbox("Weather Condition", list(WEATHER_MAPPING.keys()))
    weather_condition = WEATHER_MAPPING[weather_display]


# PREDICTION BUTTON
if st.button("Predict Position", type="primary"):
    with st.spinner("Calculating prediction..."):
        try:
            X_input = create_input_vector(driver_code, circuit, car, weather_condition)
            pred = model.predict(X_input)[0]
            
            # Just making sure the position is between 0 and 21
            final_position = max(1, min(20, int(round(pred))))
            
            # Displaying result with emoji :)
            position_emojis = {1: "🥇", 2: "🥈", 3: "🥉"}
            emoji = position_emojis.get(final_position, "🏁")
            
            st.success(f"### {emoji} Predicted Finishing Position: P{final_position}")
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("<div style='text-align: center;'>   Developed by:    Yashwanth Krishna Devanaboina    </div>", unsafe_allow_html=True)
st.markdown("")
st.markdown("<div style='text-align: center;'>AI/ML Engineer | Software Developer | CS student at Lnu | AWS Certified Cloud Practitioner | Cisco Certified Data Analyst</div>", unsafe_allow_html=True)
st.markdown("""<div style='text-align: center;'><a href="https://github.com/Yashwanth-Dev18" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/yashwanth-krishna-devanaboina-66ab83212" target="_blank">LinkedIn</a></div>""", unsafe_allow_html=True)

# SIDEBAR STUFF
st.sidebar.header("ML Model Information")
st.sidebar.markdown("""
- **Algorithm**: Gradient Boosting Regressor
- **Training Data**: F1 Seasons 2014 to 2025(till Monza)
- **MAE (Error Margin)**: ~ 3 positions
- **Features**: 194 one-hot encoded columns, 5K rows of data
""")

st.sidebar.header("How to Use")
st.sidebar.markdown("""
1. **Select Driver**: Choose your driver
2. **Select Circuit**: Pick from 32 F1 circuits
3. **Select Team**: Choose Team to proceed with the car selection
4. **Select Car**: Pick specific car model from that team
5. **Select Weather**: Sunny/Cloudy (dry) or Rainy (wet)
6. **Click Predict**: Get finishing position prediction based on the provided scenario
""")

# 
st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown("*Note: Predictions are ML-based probabilistic estimates based on historical " \
"data from the Hybrid Era of F1 Motorsport (2014-2025)*")
st.sidebar.markdown("I built this app as a PoC to predict race positions for F1(an unpredictable sport), amidst all the chaos.")
st.sidebar.markdown("-----------------------------------")