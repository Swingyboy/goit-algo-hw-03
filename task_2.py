import turtle


def koch_snowflake(t: turtle.Turtle, order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float) -> None:
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # Drawing 3 sides of the snowflake
    for i in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    order = int(input("Enter the recursion depth: "))
    size = 450
    draw_koch_snowflake(order, size)


if __name__ == "__main__":
    main()
