import pandas as pd

# Leser inn aktiv effekt for alle lastene
p_load = pd.read_csv('p_load.csv', index_col="Date", parse_dates=True)
# Leser inn reaktiv effekt for alle lastene
q_load = pd.read_csv('q_load.csv', index_col="Date", parse_dates=True)

# Bussene jeg er ute etter
load_bus = ["25", "29", "30", "31"]

# Vinter data
# Ny tabell med kun de bussene jeg er ute etter
p_load_data = p_load[load_bus].copy()
q_load_data = q_load[load_bus].copy()

# Summerer lastene for hver time
p_load_data["Total Load"] = p_load_data.sum(axis=1)
# Finner timen med høyest total last
max_load_time = p_load_data["Total Load"].idxmax()


# Sommer data
sommer = p_load_data[p_load_data.index.month.isin([6, 7]) & (p_load_data.index.hour.isin([12, 13, 14]))]

# Finner timen med lavest total last om sommeren
min_load_time = sommer["Total Load"].idxmin()

# Vinter data
print("Timen med høyest last:", max_load_time)
print(p_load_data.loc[max_load_time] * 1000)  # Konverterer fra MW til kW for utskrift
print(q_load_data.loc[max_load_time] * 1000)  # Konverterer fra MVar til kVAr for utskrift

# Sommer data
print("Timen med lavest last om sommeren:", min_load_time)
print(p_load_data.loc[min_load_time] * 1000)  # Konverterer fra MW til kW for utskrift
print(q_load_data.loc[min_load_time] * 1000)  # Konverterer fra MVar til kVAr for utskrift