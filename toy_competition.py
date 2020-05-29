from colour import Color


def color_tuple(color):
    return int(color.rgb[0] * 255), int(color.rgb[1] * 255), int(color.rgb[2] * 255)


print(color_tuple(Color('orange')))
