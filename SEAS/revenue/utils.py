# util/charts.py
colorPalette = [ '#196f9d', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8',  '#9b59b6',
                   '#d68910', '#55efc4', '#196f3d', '#85c1e9', '#34495e', '#2c3e50' ]
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


def iubRevenueChartDataPacker( dataTable, colNames ):
    ''' Packages rows and their column labels into an easy-to-chart form.         
        "dataTable" is a list of tuples, where each tuple is a row of the table,         
        "colNames" is the column names of the table '''

    columns = [ list(t) for t in zip( *dataTable ) ]             # unzips tuples of rows, and aligns corresponding elements to form tuples of cols
    colors = generate_color_palette( len( columns ) )            # a unique color for every column

    xAxisValues = columns[0]                                     # first element of each row tuple is semester alt: [ row[0] for row in dataTable ]

    totals = columns[-2]                                         # total revenue of IUB in each semester

    changes = columns[-1]                                        # percentage change in revenue vs the same session semester of the previous year

    yAxisValues = [                                       
        { 'label': label, 'data': columns[i+1], 'borderColor': colors[i+1] }
        for i, label in enumerate( colNames[1:-2] )
    ]  # list of dictionaries containing e.g. { label: "SETS", data: [134,67,67..], borderColor:'#55efc4' }

    return xAxisValues, yAxisValues, totals, changes 


def deptRevenueChartDataPacker( dataTable, colNames ):
    ''' Packages rows and their column labels into an easy-to-chart form.         
        "dataTable" is a list of tuples, where each tuple is a row of the table,         
        "colNames" is the column names of the table '''

    columns = [ list(t) for t in zip( *dataTable ) ]             # unzips tuples of rows, and aligns corresponding elements to form tuples of cols
    colors = generate_color_palette( len( columns ) )            # a unique color for every column
    numOfDep = ( len( colNames )//2 )                            # used for slicing between department rev and % change

    xAxisValues = columns[0]                                     # first element of each row tuple is semester alt: [ row[0] for row in dataTable ]

    yAxisValues = [                                       
        { 'label': label, 'data': columns[i+1], 'borderColor': colors[i+1] }
        for i, label in enumerate( colNames[ 1 : numOfDep ] )
    ]  # list of dictionaries containing e.g. { label: "SETS", data: [134,67,67..], borderColor:'#55efc4'}

    percChanges = [
        { 'label': label, 'data': columns[i+1], 'backgroundColor': colors[i+1] }
        for i, label in enumerate( colNames[ numOfDep+1 : -1 ] )        
    ] # list of dictionaries containing e.g. { label: "%SETS", data: [ 34,7,12..], backgroundColor:'#55efc4',}

    return xAxisValues, yAxisValues, percChanges 