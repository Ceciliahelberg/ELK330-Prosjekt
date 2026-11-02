import pandas as pd

# Leser inne datafilene med branch data
branch_data = pd.read_csv('mpc_branch.csv', index_col=0)
extra_branch_data = pd.read_csv('branch_extra.csv', index_col=0)

# Leser inne mva base filen (kun en verdi for alle busser)
S_base = pd.read_csv('mpc_base_mva.csv')["Base MVA"].iloc[0]    #S_base = 0.0344 MVA
V_base = 0.23   #V_base = 0.23 kV
Z_base = (V_base ** 2) / S_base   #Z_base = 1.5407 ohm

# Bussene jeg er ute etter
Bus_nr = [1, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31]

branch_radial = branch_data[(branch_data['fbus'].isin(Bus_nr)) & (branch_data['tbus'].isin(Bus_nr))]

# Legger til kabellengde og kabeltype fra ekstra datafilen, matcher fbus og tbus med From Bus og To Bus
branch_radial = branch_radial.merge(extra_branch_data, left_on=["fbus", "tbus"], right_on=["From Bus", "To Bus"])

# Legger til kolonner for R og X i ohm, basert på Z_base
branch_radial["R [Ohm]"] = branch_radial["r"] * Z_base
branch_radial["X [Ohm]"] = branch_radial["x"] * Z_base

# Gjør om R og X til ohm/km ved å dele på lengden i km
branch_radial["R [Ohm/km]"] = branch_radial["R [Ohm]"] / branch_radial["Length [km]"]
branch_radial["X [Ohm/km]"] = branch_radial["X [Ohm]"] / branch_radial["Length [km]"]

# Finner maksimal strømkapasitet for hver branch basert på rateA (antar rateA er i kVA)
branch_radial["I maks [A]"] = branch_radial["rateA"] / (3**0.5 * V_base)

print(branch_radial[["fbus", "tbus", "Length [km]", "Branch type", "R [Ohm/km]", "X [Ohm/km]", "rateA", "I maks [A]", "R [Ohm]", "X [Ohm]"]])

