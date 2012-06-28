class PyPlotHelper(object):
    '''
    The following format string characters are accepted to control the line style or marker:

    character   description
    '-'     solid line style
    '--'    dashed line style
    '-.'    dash-dot line style
    ':'     dotted line style
    '.'     point marker
    ','     pixel marker
    'o'     circle marker
    'v'     triangle_down marker
    '^'     triangle_up marker
    '<'     triangle_left marker
    '>'     triangle_right marker
    '1'     tri_down marker
    '2'     tri_up marker
    '3'     tri_left marker
    '4'     tri_right marker
    's'     square marker
    'p'     pentagon marker
    '*'     star marker
    'h'     hexagon1 marker
    'H'     hexagon2 marker
    '+'     plus marker
    'x'     x marker
    'D'     diamond marker
    'd'     thin_diamond marker
    '|'     vline marker
    '_'     hline marker

    The following color abbreviations are supported:

    character   color
    'b'     blue
    'g'     green
    'r'     red
    'c'     cyan
    'm'     magenta
    'y'     yellow
    'k'     black
    'w'     white


    The following hatch abbreviations are supported:

    character   description

    r'/'   - diagonal hatching
    r'\\'   - back diagonal
    r'|'   - vertical
    r'-'   - horizontal
    r'+'   - crossed
    r'x'   - crossed diagonal
    r'o'   - small circle
    r'O'   - large circle
    r'.'   - dots
    r'*'   - stars
    '''
    STYLE_CHARACTERS  = ['-', '--', '-.', ':']
#    MARKER_CHARACTERS = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', 
    MARKER_CHARACTERS = ['o', 'v', '^', '<', '>', '1', '2', 
                            '3', '4', 's', 'p', '*', 'h', 'H', '+', 
                            'x', 'D', 'd', '|', '_']

    COLOUR_CHARACTERS = ['r', 'y', 'b', 'g', 'c', 'm', 'k']
    HATCH_CHARACTERS = [r'/', r'\\', r'|', r'-', 
                        r'x', r'.', r'*',
                        r'o', r'+', r'O',]


    @classmethod
    def line_styles(cls):
        colours = cls.colour_characters()
        styles = cls.style_characters()
        markers = cls.marker_characters()

        while True:
           yield {'linestyle': styles.next(),
                    'color': colours.next(),
                    'marker': markers.next()}

        

    @classmethod
    def marker_characters(cls):
        current = 0
        max = len(cls.MARKER_CHARACTERS)

        while True:
            yield cls.MARKER_CHARACTERS[current]
            current = (current + 1) % max
        

    @classmethod
    def hatch_characters(cls):
        current = 0
        max = len(cls.HATCH_CHARACTERS)

        while True:
            yield cls.HATCH_CHARACTERS[current]
            current = (current + 1) % max
        

    @classmethod
    def colour_tuples(cls):
        import numpy

        current = 0


        # July
        july = [
#                [38, 37, 28],
#                [235, 10, 68],
                [160, 232, 183],
                [242, 100, 61],
#                [242, 167, 61],
                ]

        # Cheer up emo kid
        cheer = [[ 85,  98, 112],
                [ 78, 205, 196],
                [199, 244, 100],
#                [255, 107, 107],
                [196,  77,  88]]
        colour_tuples = [numpy.array(t) for t in cheer + july]
        max = len(colour_tuples)

        while True:
            yield tuple(numpy.clip(colour_tuples[current] * (1.1 / 255.0), 0, 1.0))
            current = (current + 1) % max
        

    @classmethod
    def colour_characters(cls):
        current = 0
        max = len(cls.COLOUR_CHARACTERS)

        while True:
            yield cls.COLOUR_CHARACTERS[current]
            current = (current + 1) % max
        

    @classmethod
    def style_characters(cls):
        current = 0
        max = len(cls.STYLE_CHARACTERS)

        while True:
            yield cls.STYLE_CHARACTERS[current]
            current = (current + 1) % max
        
        

if __name__ == '__main__':
    import numpy as np
    from pylab import *
    from math import sin, cos, pi

    num_points = 25

    a = float(num_points) / 2
    b = a / 2

    x = list(range(num_points))

    # define some example functions
    f1 = x[:]
    f2 = [a] * num_points
    f3 = [a + b * sin(p * pi / 4) for p in x]
    f4 = [a + b * cos(p * pi / 4) for p in x]

    styles = PyPlotHelper.line_styles()

    figure(1)
    
    for f in [f1, f2, f3, f4]:
        h = plot(x, f, **styles.next())

    show()
