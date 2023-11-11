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
d3.movingbubbles(df, speed={"slow": 10, "medium": 2, "fast": 1}, filepath='movingbubbles.html')
#