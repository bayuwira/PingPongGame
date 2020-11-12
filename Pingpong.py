import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1

class PongBall(Widget):
    velocity_x = NumericProperty(0) #(0) adalah nilai defalut, kayak misal x = 0
    velocity_y = NumericProperty(0) #untuk menginisiasi bahwa variabel ini adalah integer oleh kivy
    velocity = ReferenceListProperty(velocity_x, velocity_y) #agar bisa reference pada waktu yang sama velocity_x dan velocity_y

    #posisi terakhir bola Latest Position =  Current velocity + current position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# menggerakkan bola dengan memanggil move function
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        '''mantulin bola atas bawah, pada saat sumbu y < 0 a.k.a bola keatas, atau bola berlokasi
        lebih dari layar maka velocity (lihat function move()) akan dikali dengan -1, agar dapat nilai negatif
        dari posisi pemantulan, misal bola ke pojok koordinat (20,100), karna bola ukurannya 50 maka
        supaya ga lewat layar y, self.heigt - 50, jd (20,50) akan dikembalikan nilai (20, -50)
         !ingat berlaku juga untuk sumbu x'''

        if(self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        #bounce off  right
        if(self.ball.x < 0):
            self.ball.velocity_x *= -1
            self.player1.score += 1

        # bounce off right
        if(self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1
            self.player2.score += 1


        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        print(self.ball.velocity)

    def on_touch_move(self, touch):
        if touch.x < self.width / 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve()
        Clock.schedule_interval(game.update, 1.0/60.0) #60fps
        return game

PongApp().run()
