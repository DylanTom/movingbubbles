import pandas as pd

# Load d3blocks
from d3blocks import D3Blocks

#
# Initialize
d3 = D3Blocks()
#
# Load example data
df = pd.read_csv("input.csv")
#
# Plot
d3.movingbubbles(
    df,
    speed={"slow": 0, "medium": 20, "fast": 10},
    filepath="movingbubbles.html",
)
# 0 = Dylan
# 1 = Clara
# 2 = Justin


# Meeting
# Aleep
# Class
# Wake Up and Think About Life
# Wake Up
# Cook
# Eat
# In Crossings
# In Dryden
# Losing Money
# Having a Crisis
# Getting Drunk
# DTI Stuff
