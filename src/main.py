import pygame
import numpy as np
from graphics import Drawer
from transformations import translate, scale, rotate

# Инициализация Pygame
pygame.init()

# Настройки окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Трансформация и моделирование матриц")

# Создание экземпляра класса Drawer
drawer = Drawer(screen)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Пример использования матричных преобразований
    points = np.array([[100, 100], [200, 100], [150, 200]])
    translated_points = translate(points, 50, 50)
    scaled_points = scale(translated_points, 1.5, 1.5)
    rotated_points = rotate(scaled_points, 45)

    # Рисование осей координат
    drawer.draw_axes()

    # Рисование преобразованных точек
    drawer.draw_polygon(rotated_points)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()