import pandas as pd

# Leser inn datafilen med bussdata
bus_data = pd.read_csv('mpc_bus.csv')


# Bussene jeg er ute etter
Bus_nr = [1, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31]

bus_radial = bus_data[bus_data['bus_i'].isin(Bus_nr)]

print(bus_radial[["bus_i", "type", "basekV"]])

