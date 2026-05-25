import pygame as pg


def apply_hitbox(base_rect, x_offset, width_reduce, y_offset, height_reduce):
    """Возвращает уменьшенный rect для проверки коллизий."""
    rect = base_rect.copy()
    rect.x += x_offset
    rect.width -= width_reduce
    rect.y += y_offset
    rect.height -= height_reduce
    return rect
