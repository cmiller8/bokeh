from bokeh.plotting import ColumnDataSource, figure, gridplot, output_file, show
from bokeh.sampledata.autompg import autompg

output_file("panning.html")

# Load some Automobile data into a data source. Interesting columns are:
# "yr" - Year manufactured
# "mpg" - miles per gallon
# "displ" - engine displacement
# "hp" - engine horsepower
# "cyl" - number of cylinders
source = ColumnDataSource(autompg.to_dict("list"))
source.add(autompg["yr"], name="yr")

# Let's set up some plot options in a dict that we can re-use on multiple plots
plot_config = dict(plot_width=300, plot_height=300, tools="pan,wheel_zoom,box_zoom,select")

# First let's plot the "yr" vs "mpg" using the plot config above
# Note that we are supplying our our data source to the renderer explicitly
p1 = figure(title="MPG by Year", **plot_config)
p1.circle("yr", "mpg", color="blue", source=source)

# EXERCISE: make another figure p2 with circle renderer, for "hp" vs "displ" with
# color "green". This renderer should use the same data source as the renderer
# above, that is what will cause the plots selections to be linked
p2 = figure(title="HP vs. Displacement", **plot_config)
p2.circle("hp", "displ", color="green", source=source)

# EXERCISE: and another figure p3 with circle renderer for "mpg" vs "displ",
# with the size proportional to "cyl". Set the the line color to be "red"
# with no fill, and use the same data source again to link selections
p3 = figure(title="MPG vs. Displacement", **plot_config)
p3. circle("mpg", "displ", size="cyl", line_color="red", fill_color=None, source=source)

# gridplot(...) accepts nested lists of plot objects
p = gridplot([[p1, p2, p3]])

show(p)
