"""This script contains function used for the Python demo
created for the Refficiency away weekend 2021"""

# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt


def cost_calculation_external(qty,price):
  """This function multiplies the quantity of items
  by the unit prices and prints total cost.

  Inputs
  qty - item quantity
  price - unit price

  Outputs
  Total cost print to screen
  """
  # Calculation
  cost = qty*price
  # Output
  print(cost)


def plot_unfccc(filepath, header=3, nrows=6, first_col=2, 
                figsize=[12,5], xtitle='Year', ytitle='CO2 emissions (kt)'):
  """This function plots emissions over time for each sector included in a 
  UNFCCC .csv file

  Inputs
  filepath - path to data file
  header - rows before data in .csv
  nrows - rows of data to plot
  first_col - first column with data
  figsize - size of output plot
  xtitle - Title of x axis
  ytitle - Title of y axis
  """
  # Importing
  data = pd.read_csv(filepath, skiprows=header, nrows=nrows)

  # Extract data
  years = data.columns[first_col:]
  emissions = data.values[:,first_col:]

  # Convert emissions data to numeric
  emissions_vals = pd.to_numeric(emissions.flatten(), errors='coerce').reshape(emissions.shape).astype(float)

  # Extract final year value
  years_vals = years.values
  years_vals[-1] = "".join(filter(str.isdigit,years_vals[-1]))

  # Convert years to numeric values
  years_vals = years.astype(float)

  # Extract the names of the sectors
  sectors = data.values[:,0]

  # Now we'll create a prettier looking plot containing a line for each entry
  fig, ax = plt.subplots(1,1,figsize=figsize)
  for i in range(emissions.shape[0]):
    ax.scatter(years_vals, emissions_vals[i], label=sectors[i])

  # Adding some labels
  ax.legend(), ax.set_title(filepath.split('.')[0].split('/')[-1], fontsize=18), ax.set_xlabel(xtitle, fontsize=15), ax.set_ylabel(ytitle,fontsize=15)
  plt.show()