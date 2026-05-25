import pygame as pg


class InputHandler:
    """Обработка клавиатуры и мыши."""

    def get_pressed_keys(self):
        return pg.key.get_pressed()

    def process_events(self, wolf_timer_id, gameplay, on_quit, on_spawn_wolf, on_attack):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                on_quit()
            elif event.type == wolf_timer_id and gameplay:
                on_spawn_wolf()
            elif event.type == pg.KEYDOWN and event.key == pg.K_f and gameplay:
                on_attack()

    def is_mouse_clicked(self, rect):
        mouse_pos = pg.mouse.get_pos()
        return rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]
