import turtle

def koch_snowflake(t, order, size):
    '''Рекурсивно малює криву Коха'''

    if order == 0:
        # Базовий випадок: якщо рівень рекурсії 0, просто малюємо пряму лінію.
        t.forward(size)
    else:
        # Рекурсивний крок: ділимо лінію на 4 сегменти, повертаючи на 60 градусів.
        koch_snowflake(t, order - 1, size / 3) # Перша третина
        t.left(60)
        koch_snowflake(t, order - 1, size / 3) # Друга третина (вершина трикутника)
        t.right(120)
        koch_snowflake(t, order - 1, size / 3) # Третя третина (друга сторона трикутника)
        t.left(60)
        koch_snowflake(t, order - 1, size / 3) # Четверта третина

def draw_full_koch_snowflake(t, order, size):
    '''Малює повну сніжинку Коха, що складається з трьох кривих Коха'''

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120) # Повертаємо для малювання наступної сторони сніжинки

def main():
    # Налаштування вікна Turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")
    screen.bgcolor("lightblue")

    # Створення об'єкта черепашки
    t = turtle.Turtle()
    t.speed(0) # Максимальна швидкість малювання
    t.pensize(2)
    t.pencolor("darkblue")

    # Запит рівня рекурсії у користувача
    while True:
        try:
            recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха (наприклад, 0-6): "))
            if 0 <= recursion_level <= 6: # Обмежуємо рівень, щоб уникнути надмірної завантаженості
                break
            else:
                print("Будь ласка, введіть число від 0 до 6.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")

    # Вихідні параметри
    initial_side_length = 300

    # Переміщення черепашки до початкової позиції (щоб сніжинка була по центру)
    t.penup()
    t.goto(-initial_side_length / 2, initial_side_length / 2 / 1.732 * 0.5) # Приблизне центрування
    t.pendown()

    # Малювання сніжинки
    draw_full_koch_snowflake(t, recursion_level, initial_side_length)

    # Оновлення екрану, щоб показати намальований фрактал
    screen.update()

    # Залишаємо вікно відкритим до закриття користувачем
    screen.mainloop()

if __name__ == "__main__":
    main()