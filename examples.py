# this file was created by will goodman 11/16

# Isaiah's gun code examples
def shoot(self):
        # if the player presses space and the timer has been running for more than 0.3 seconds, create a bullet and shoot it
        if pg.key.get_pressed()[pg.K_SPACE] and self.cd.delta > 0.3:
            self.cd.event_time = pg.time.get_ticks()/1000
            b = Bullet()
            self.all_sprites.add(b)
            self.all_bullets.add(b)
            # sound effect
            pg.mixer.Channel(1).play(pg.mixer.Sound(os.path.join(snd_folder, 'pew.wav')))
class Cooldown():
        def __init__(self):
            self.current_time = 0
            self.event_time = 0
            self.delta = 0
        def ticking(self):
            self.current_time = (pg.time.get_ticks())/1000
            self.delta = self.current_time - self.event_time
        def timer(self):
            self.current_time = (pg.time.get_ticks())/1000