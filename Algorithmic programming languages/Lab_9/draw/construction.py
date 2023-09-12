import simple_draw as sd


def wall_brick(start_point, size_wall, size_brick, color=sd.COLOR_ORANGE, width=2):
    """
    :param start_point: левая нижняя точка стены
    :param size_wall: (width, height) размеры стены
    :param size_brick: (width, height) размеры кирпича
    :param color: цвет обводки
    :param width: толщина линии
    """
    START_X = start_point[0]
    START_Y = start_point[1]
    BRICK_WIDTH = size_brick[0]
    BRICK_HEIGHT = size_brick[1]
    ROW_BRICK_NUMBER = size_wall[0] // BRICK_WIDTH
    ROW_NUMBER = size_wall[1] // BRICK_HEIGHT
    BRICK_OFFSET = int(0.5 * BRICK_WIDTH)

    for current_row in range(ROW_NUMBER):
        # вот здесь определяется, сколько именно составит смещение.
        # для четного ряда будет 50, для нечетного - 0
        OFFSET = BRICK_OFFSET if current_row % 2 == 0 else 0

        for current_brick in range(ROW_BRICK_NUMBER):
            # добавим смещение к началу отсчета для оси X
            left_bottom_x = START_X + OFFSET + BRICK_WIDTH * current_brick
            left_bottom_y = START_Y + BRICK_HEIGHT * current_row
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            right_top_x = left_bottom_x + BRICK_WIDTH
            right_top_y = left_bottom_y + BRICK_HEIGHT
            right_top = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom, right_top, color, width)

    sd.rectangle(
        sd.get_point(START_X, START_Y),
        sd.get_point(START_X + BRICK_OFFSET + BRICK_WIDTH * ROW_BRICK_NUMBER, START_Y + BRICK_HEIGHT * ROW_NUMBER),
        color, width+1
    )





