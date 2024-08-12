''' The graph.py file utilizes altair to create a graph'''
import altair as alt
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> alt.Chart:
    ''' The chart function starts by using information from our data frame
    to generate labeling infomation. We then update the properties to the 
    values that we want - this referes to height, width, background color,
    and padding around the chart '''
    chart = alt.Chart(df).mark_circle().encode(
        x=alt.X(x, title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(target, title=target),
        tooltip=[x, y, target]
    )
    chart.properties(
        update={
                'width': 3200,
                'height': 1400,
                'background': 'white',
                'padding': {'left': 50, 'top': 50, 'right': 50, 'bottom': 50}
            }
    )
    chart.configure(
        title={
            'anchor': 'start',
            'fontSize': 24,
            'font': 'Arial'
        },
        axis={
            'labelFontSize': 14,
            'titleFontSize': 18
        }
    )
    return chart

if __name__ == "__main__":
    # This is an example of chart creation using some of our data
    df = DataFrame({
        'Name': ['Spore Mephit', 'Pit Fiend', 'Dust Devil'],
        '_id': [1, 2, 3],
        'Type': ['Monster', 'Fiend', 'Elemental']
    })

    # Call the chart function and save the result
    viz = chart(df, x='Name', y='_id', target='Type')
    viz.save("visualization.html")
