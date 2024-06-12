from random import random
from threading import Thread
import time

import numpy as np
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create a figure
plot = figure(title="Real-time Data Streaming with Bokeh", x_axis_label='Time', y_axis_label='Value')
plot.line('x', 'y', source=source)

# Update function to stream data
def update():
    new_data = dict(
        x=[time.time()],
        y=[random()]
    )
    source.stream(new_data, rollover=200)

# Add a periodic callback to update the data
curdoc().add_periodic_callback(update, 100)

# Add the plot to the document
curdoc().add_root(column(plot))

# Function to simulate data streaming
def data_streaming():
    while True:
        time.sleep(1)
        update()

# Run the data streaming in a separate thread
thread = Thread(target=data_streaming)
thread.start()
