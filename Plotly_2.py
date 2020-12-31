import plotly.graph_objects as go
import pandas as pd
import numpy as np

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")

z = z_data.values

sh_0, sh_1 = z.shape

x, y = np.linspace(0,1,sh_0), np.linspace(0,1,sh_1)

fig = go.Figure(data=[go.Surface(z=z, y=y, x=x)])

fig.update_layout(title=" Mount Bruno", width=1200, height=700, autosize=False
                  , margin=dict(l=90, r=150, b=65, t=90))

fig.show()
