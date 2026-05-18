import math
import turtle
from typing import Final

Point = tuple[float, float]

MAX_RECURSION_LEVEL: Final = 12
BASE_BRANCH_SIZE: Final = 150
SCALE_FACTOR: Final = 0.8


def get_recursion_level() -> int:
    while True:
        try:
            user_input = input(f"Вкажіть рівень рекурсії від 0 до {MAX_RECURSION_LEVEL}: ")
            return parse_recursion_level(user_input)
        except ValueError as error:
            print(error)


def parse_recursion_level(raw_value: str) -> int:
    try:
        level = int(raw_value)
    except ValueError as exc:
        raise ValueError("Рівень рекурсії має бути цілим числом.") from exc

    if not 0 <= level <= MAX_RECURSION_LEVEL:
        raise ValueError(
            f"Рівень рекурсії має бути в діапазоні від 0 до {MAX_RECURSION_LEVEL}."
        )

    return level

def get_vector_scaled(angle: int, first: Point, second: Point, scale: float) -> Point:
    vector_x = second[0] - first[0]
    vector_y = second[1] - first[1]
    x = vector_x * math.cos(math.radians(angle)) - vector_y * math.sin(math.radians(angle))
    y = vector_x * math.sin(math.radians(angle)) + vector_y * math.cos(math.radians(angle))

    return x * scale, y * scale


def draw_tree(painter: turtle.Turtle, first_point: Point, second_point: Point, current_recursion_level, base_recursion_level) -> None:
    painter.penup()
    painter.goto(first_point)
    painter.pendown()
    painter.goto(second_point)

    if current_recursion_level == 0:
        return
    current_recursion_level -= 1

    vector_left = get_vector_scaled(35, first_point, second_point, SCALE_FACTOR)
    vector_right = get_vector_scaled(-35, first_point, second_point, SCALE_FACTOR)

    end_point_left = vector_left[0] + second_point[0], vector_left[1] + second_point[1]
    end_point_right = vector_right[0] + second_point[0], vector_right[1] + second_point[1]

    draw_tree(painter, second_point, end_point_left, current_recursion_level, base_recursion_level)
    draw_tree(painter, second_point, end_point_right, current_recursion_level, base_recursion_level)



def configure_turtle(width, height) -> tuple:
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.setup(width=width, height=height)
    screen.bgcolor("#f3f7f0")
    screen.tracer(0, 0)

    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    my_turtle.speed(0)
    my_turtle.pensize(3)
    my_turtle.pencolor("#50AA00")

    return screen, my_turtle


def main() -> None:
    recursion_level = get_recursion_level()
    width = 1000
    height = 800
    screen, my_turtle = configure_turtle(width, height)

    start_y = -height / 2 + BASE_BRANCH_SIZE
    start_first = (0, start_y)
    start_second = (0, start_y+BASE_BRANCH_SIZE)

    draw_tree(my_turtle, start_first, start_second, recursion_level,recursion_level)

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
