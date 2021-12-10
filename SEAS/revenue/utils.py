# util/charts.py
colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8',  '#9b59b6',
                   '#d68910', '#196f3d', '#85c1e9', '#34495e', '#2c3e50' ]
colorPrimary, colorSuccess, colorDanger = '#79aec8', colorPalette[0], colorPalette[5]

def generate_color_palette( amount ):

    palette = []
    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette



def revenueChartDataPacker( dataTable, colNames, isArea = False ):
    ''' Packages rows and their column labels into an easy-to-chart form.         
        "dataTable" is a list of tuples, where each tuple is a row of the table,         
        "colNames" is the column names of the table, "isArea" = false is for line chart selector '''

    columns = [ list(t) for t in zip( *dataTable ) ]             # unzips tuples of rows, and aligns corresponding elements to form tuples of cols

    colors = generate_color_palette( len( columns ) )            # unique color list for every column

    xAxisValues = columns[0]                                     # first element of each row tuple is semester alt: [ row[0] for row in dataTable ]

    yAxisValues = [                                       
        { 'labels': label, 'data': columns[i+1], 'borderColor': colors[i+1],  'fill': isArea }
        for i, label in enumerate( colNames[1:] )
    ]  # list of dictionaries containing e.g. { label: "SETS", data: [134,67,67..], borderColor:'#55efc4', fill: true }

    return xAxisValues, yAxisValues 
    
    
    
            

