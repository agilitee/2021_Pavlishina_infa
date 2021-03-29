from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
screen = tk.Canvas(root, bg='white')
screen.pack(fill=tk.BOTH, expand=True)

count_bumbs = 0


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.speed_x = 2
        self.speed_y = 5
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = screen.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        screen.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.speed_x и self.speed_y, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        global count_bumbs
        if self.x + self.r >= 800 or self.x - self.r <= 0 and count_bumbs == 0:
            self.speed_x = -self.speed_x
            count_bumbs += 1
        elif self.y - self.r <= 0 or self.y + self.r >= 600 and count_bumbs == 0:
            self.speed_y = -self.speed_y
            count_bumbs += 1
        self.x += self.speed_x
        self.y += -self.speed_y + 5
        self.speed_y -= 5

    def Hittest(self, object):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            object: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5 <= self.r + object.r:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = screen.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча speed_x и speed_y зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.speed_x = self.f2_power * math.cos(self.an)
        new_ball.speed_y = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            screen.itemconfig(self.id, fill='orange')
        else:
            screen.itemconfig(self.id, fill='black')
        screen.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.an),
                      450 + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            screen.itemconfig(self.id, fill='orange')
        else:
            screen.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.velocity_x = choice([-10, -9, -8, -7, -6, -6, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.velocity_y = choice([-10, -9, -8, -7, -6, -6, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.id = screen.create_oval(0, 0, 0, 0, )
        self.id_points = screen.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def hit(self, points=1):
        """Попадание шарика в цель."""
        screen.coords(self.id, -10, -10, -10, -10)
        self.points += points
        screen.itemconfig(self.id_points, text=self.points)

    def move(self):
        """
        Функция двигает шарики цели и не дает им вылететь за экран
        """
        self.x += self.velocity_x
        self.y += self.velocity_y
        if self.x + self.r >= 800:
            self.velocity_x = -self.velocity_x

        if self.x - self.r <= 0:
            self.velocity_x = -self.velocity_x

        if self.y + self.r >= 600:
            self.velocity_y = -self.velocity_y

        if self.y - self.r <= 0:
            self.velocity_y = -self.velocity_y
        screen.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        screen.itemconfig(self.id, fill='red')

    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(20, 50)
        color = self.color = 'red'
        screen.coords(self.id, x - r, y - r, x + r, y + r)
        screen.itemconfig(self.id, fill=color)

t1 = Target()
screen1 = screen.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, t1, screen1, balls, bullet
    t1.live = 1
    screen.itemconfig(screen1, text='')
    t1.new_target()
    bullet = 0
    balls = []
    screen.bind('<Button-1>', g1.fire2_start)
    screen.bind('<ButtonRelease-1>', g1.fire2_end)
    screen.bind('<Motion>', g1.targetting)
    while t1.live or t2.live or balls:
        t1.move()
        for b in balls:
            b.move()
            b.set_coords()
            if b.Hittest(t1) and t1.live:
                screen.delete(b.id)
                t1.live = 0
                t1.hit()
                screen.bind('<Button-1>', '')
                screen.bind('<ButtonRelease-1>', '')
                screen.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                screen.update()
                time.sleep(1)
                new_game()
        screen.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    screen.itemconfig(screen1, text='')
    screen.delete(Gun)
    root.after(750, new_game)


new_game()

root.mainloop()
