import time
import pandas as pd
from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="My_geolocate")

# Create table for storing lat and long
Address_GeoCodes = []

# Create table for storing incorrect addresses
Incorrect_Addresses = []

# Create Function
def get_geocode(addresses):
    for i in addresses:
        location = geolocator.geocode(i)
        if hasattr(location, "latitude"):
            Address_GeoCodes.append((i, location.latitude, location.longitude))
        else:
            Address_GeoCodes.append((i, None, None))
            Incorrect_Addresses.append(i)
        time.sleep(1)

# Import Data
df = pd.read_csv('[path]')

# Execute geolocating function
get_geocode(df.address_full)

# Convert to pandas dataframe
df_final = pd.DataFrame(Address_GeoCodes, columns=["ExposureLocation", "Latitude", "Longitude"])

# Export to CSV
df_final.to_csv("[filename]", index=False, header=True)