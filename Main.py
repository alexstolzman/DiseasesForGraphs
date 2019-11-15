from typing import Tuple, List

import pygame
from pygame.math import Vector2

from Edges import Edges
import random
from Button import Button
from Vertices import Vertices


#   also occur from

def render_paragraphs(screen, paragragh_font, black):
    screen.blit(paragragh_font.render("Cholera is a waterborne bacterium that causes", True, black), [865, 20])
    screen.blit(paragragh_font.render("diarrhea, vomiting, and leg cramps in about", True, black), [865, 40])
    screen.blit(paragragh_font.render("10% of the people infected. Without treatment", True, black), [865, 60])
    screen.blit(paragragh_font.render("in these 10%, death can occur within hours.", True, black), [865, 80])
    screen.blit(paragragh_font.render("An estimated 95,00 deaths occur worldwide ", True, black), [865, 100])
    screen.blit(paragragh_font.render("annually. Cholera is found in water or food", True, black), [865, 120])
    screen.blit(paragragh_font.render("that have been contaminated with the feces of", True, black), [865, 140])
    screen.blit(paragragh_font.render("a person who has cholera. It can also occur ", True, black), [865, 160])
    screen.blit(paragragh_font.render("from eating raw shellfish.", True, black), [865, 180])

    screen.blit(paragragh_font.render("The Spanish Flu was an influenza pandemic", True, black), [865, 230])
    screen.blit(paragragh_font.render("that occurred in 1918-1919. It’s estimated", True, black), [865, 250])
    screen.blit(paragragh_font.render("about 500 million people (one-third of the", True, black), [865, 270])
    screen.blit(paragragh_font.render("world’s population) became infected with the", True, black), [865, 290])
    screen.blit(paragragh_font.render(" virus. The death rate is estimated to be ", True, black), [865, 310])
    screen.blit(paragragh_font.render(" between 50 to 100 million people worldwide.", True, black), [865, 330])

    screen.blit(paragragh_font.render("The Plague was rampant between 1346-1353,", True, black), [865, 400])
    screen.blit(paragragh_font.render("mostly  within Europe. It’s caused by a", True, black), [865, 420])
    screen.blit(paragragh_font.render("bacterium called Yersina pestis which is", True, black), [865, 440])
    screen.blit(paragragh_font.render("transmitted by flea bites. While the exact", True, black), [865, 460])
    screen.blit(paragragh_font.render("number of deaths is unknown, it’s estimated", True, black), [865, 480])
    screen.blit(paragragh_font.render("that around 50 million people died. The", True, black), [865, 500])
    screen.blit(paragragh_font.render("Black Death is not eradicated, and still", True, black), [865, 520])
    screen.blit(paragragh_font.render("an average of 500 people worldwide annually.", True, black), [865, 540])


def main() -> None:
    cities = {
        (765, 175): [(735, 220), (560, 190)],  # New York
        (735, 220): [(630, 340), (560, 190), (765, 175)],  # DC
        (630, 340): [(420, 420), (720, 490), (735, 220), (560, 190)],  # Atlanta
        (560, 190): [(630, 340), (480, 130), (765, 175), (735, 220), (420, 420), (300, 230)],  # Chicago
        (480, 130): [(300, 230), (80, 30), (560, 190)],  # Minneapolis
        (80, 30): [(70, 320), (300, 230), (480, 130)],  # Seattle
        (420, 420): [(630, 340), (560, 190), (300, 230), (70, 320)],  # Austin
        (300, 230): [(560, 190), (420, 420), (70, 320), (80, 30), (480, 130)],  # Denver
        (70, 320): [(420, 420), (80, 30), (300, 230)]  # LA
    }

    edges = [
        # Edges("animal", random.randint(1, 15)),
        # Edges("water", random.randint(1, 15)),
        # Edges("air", random.randint(1, 15))
    ]

    pygame.init()

    pygame.init()
    screen = pygame.display.set_mode([1200, 625], pygame.FULLSCREEN)
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    black = [0, 0, 0]
    pygame.display.set_caption('Disease Graph')
    image = pygame.image.load('us.gif')
    font = pygame.font.Font("freesansbold.ttf", 16)
    paragragh_font = pygame.font.Font("freesansbold.ttf", 14)

    buttons = [
        Button(80, 40, (1100, 180), "Cholera", [0, 0, 150], font, "Cholera"),
        Button(100, 40, (1085, 350), "Spanish Flu", [150, 0, 0], font, "Flu"),
        Button(80, 40, (1100, 560), "Plague", [0, 150, 0], font, "Plague")
    ]

    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()
    is_selected = False
    disease_selected = ""
    city_selected = False

    vertices = [
        Vertices(10, pos=Vector2(765, 175), id="New York"),
        Vertices(10, pos=Vector2(735, 220), id="DC"),
        Vertices(10, pos=Vector2(630, 340), id="Atlanta"),
        Vertices(10, pos=Vector2(560, 190), id="Chicago"),
        Vertices(10, pos=Vector2(420, 420), id="Austin"),
        Vertices(10, pos=Vector2(70, 320), id="LA"),
        Vertices(10, pos=Vector2(480, 130), id="Minneapolis"),
        Vertices(10, pos=Vector2(720, 490), id="Miami"),
        Vertices(10, pos=Vector2(80, 30), id="Seattle"),
        Vertices(10, pos=Vector2(300, 230), id="Denver")
    ]

    while running:
        screen.fill(bg_color)
        screen.blit(image, (0, 0))

        screen.blit(font.render("New York", True, black), [775, 170])
        screen.blit(font.render("DC", True, black), [735, 230])
        screen.blit(font.render("Atlanta", True, black), [640, 330])
        screen.blit(font.render("Chicago", True, black), [560, 165])
        screen.blit(font.render("Austin", True, black), [430, 420])
        screen.blit(font.render("LA", True, black), [40, 295])
        screen.blit(font.render("Minneapolis", True, black), [480, 105])
        screen.blit(font.render("Miami", True, black), [720, 465])
        screen.blit(font.render("Seattle", True, black), [20, 40])
        screen.blit(font.render("Denver", True, black), [320, 240])

        edges = Edges()
        edges.generate_edges(screen, cities)
        render_paragraphs(screen, paragragh_font, black)

        for b in buttons:
            b.draw(screen)

        for v in vertices:
            v.draw(screen)

        pygame.display.flip()
        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for v in vertices:
                    if v.rect.collidepoint(pygame.mouse.get_pos()):
                        if v.id == "New York" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "DC" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Atlanta" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Chicago" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Austin" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "LA" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Minneapolis" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Miami" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Seattle" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                        elif v.id == "Denver" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])

                for b in buttons:
                    if b.rect.collidepoint(pygame.mouse.get_pos()):
                        if b.id == "Cholera":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Flu" and bu.id == "Flu":
                                        bu.change_background([150, 0, 0])
                                    elif disease_selected == "Plague" and bu.id == "Plague":
                                        bu.change_background([0, 150, 0])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Cholera"
                        elif b.id == "Flu":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Cholera" and bu.id == "Cholera":
                                        bu.change_background([0, 0, 150])
                                    elif disease_selected == "Plague" and bu.id == "Plague":
                                        bu.change_background([0, 150, 0])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Flu"
                        elif b.id == "Plague":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Flu" and bu.id == "Flu":
                                        bu.change_background([150, 0, 0])
                                    elif disease_selected == "Cholera" and bu.id == "Cholera":
                                        bu.change_background([0, 0, 150])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Plague"

    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
