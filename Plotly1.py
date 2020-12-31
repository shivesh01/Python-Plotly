import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")

fig = go.Figure(data=[go.Surface(z=data.values)])

fig.update_layout()

fig.show()
