import simple_draw as sd


def smile(x, y, color=sd.COLOR_GREEN):
    position = sd.get_point(x, y)
    sd.circle(position, radius=50, color=color, width=2)
    sd.line(sd.get_point(position.x - 30, position.y - 20), sd.get_point(position.x - 10, position.y - 30), color=color,
            width=2)
    sd.line(sd.get_point(position.x - 10, position.y - 30), sd.get_point(position.x + 10, position.y - 30), color=color,
            width=2)
    sd.line(sd.get_point(position.x + 10, position.y - 30), sd.get_point(position.x + 30, position.y - 20), color=color,
            width=2)

    sd.line(sd.get_point(position.x - 20, position.y + 20), sd.get_point(position.x - 15, position.y + 20), color=color,
            width=5)
    sd.line(sd.get_point(position.x + 20, position.y + 20), sd.get_point(position.x + 15, position.y + 20), color=color,
            width=5)