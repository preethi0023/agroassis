from data.mock_data import MOCK_EXPERTS

SOIL_TYPES = [
    "Sandy",
    "Clay",
    "Loamy",
    "Silt",
    "Peat",
    "Chalky"
]

CLIMATE_TYPES = [
    "Tropical",
    "Subtropical",
    "Mediterranean",
    "Temperate",
    "Continental",
    "Arid"
]

def get_irrigation_recommendation(soil_type, temperature, humidity, rainfall, climate_type):
    """
    Calculate irrigation recommendations based on input parameters.
    Returns a dictionary with schedule, water amount, and notes.
    """
    # Base water requirements (L/m²/day) for different soil types
    soil_water_needs = {
        "Sandy": 7,
        "Clay": 4,
        "Loamy": 5,
        "Silt": 6,
        "Peat": 3,
        "Chalky": 6
    }
    
    # Calculate base water requirement
    base_water = soil_water_needs[soil_type]
    
    # Adjust for temperature
    temp_factor = max(1, (temperature - 20) * 0.1 + 1)
    
    # Adjust for humidity
    humidity_factor = max(0.5, (100 - humidity) / 100)
    
    # Adjust for rainfall
    rainfall_reduction = min(1, rainfall / 50)  # 50mm rainfall = max reduction
    
    # Calculate final water amount
    water_amount = round(base_water * temp_factor * humidity_factor * (1 - rainfall_reduction), 1)
    
    # Generate schedule and notes
    schedule = []
    notes = []
    
    if temperature > 30:
        schedule.append("Water early morning or late evening")
        notes.append("High temperature detected - avoid midday watering")
    else:
        schedule.append("Water during early morning")
    
    if rainfall > 0:
        notes.append(f"Recent rainfall of {rainfall}mm has been considered in the calculation")
    
    if humidity < 30:
        notes.append("Low humidity - consider additional misting for sensitive plants")
    
    return {
        "schedule": schedule,
        "water_amount": water_amount,
        "notes": notes
    }

def get_mock_experts():
    """Return list of mock agricultural experts"""
    return MOCK_EXPERTS
