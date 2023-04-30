import pygame
import time
import random
import os
import ctypes
import subprocess
import webbrowser
#testing
from pygame.locals import *

debug = True
music_volume = 0
clicking = False
running = True
section = "menu"
mouse_on_button = 0

menu_button_scaler_1 = 1
menu_button_scaler_2 = 1
menu_button_scaler_3 = 1

button_count = 0

scalers = [menu_button_scaler_1, menu_button_scaler_2, menu_button_scaler_3]

offset_1 = 0
offset_2 = 0
offset_3 = 0
mouse_locked = False

loading_pre_game = False
loading_settings = False
loading_credits = False
loading_menu = False

a = 0

continue_events = [pygame.K_c, pygame.K_z, pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE]




def get_screen_resolution_linux():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    return [int(resolution[0].decode('UTF-8')), int(resolution[1].decode('UTF-8'))]


def get_screen_resolution_windows():
    user32 = ctypes.windll.user32
    return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


def load_section(section_to_load,
                 graphics_to_load,
                 graphics_location_x,
                 graphics_location_y,
                 scrolling_speed,
                 scrolling_direction):
    global section
    global mouse_locked
    global a
    global screen
    global mouse_on_button
    global loading_menu
    global loading_settings
    global loading_pre_game
    global loading_credits
    global offset_1
    global offset_2
    global offset_3

    mouse_on_button = 0
    mouse_locked = True

    i = 0
    while i < len(graphics_to_load):
        screen.blit(graphics_to_load[i],
                    (graphics_location_x[i] + scrolling_speed[i] * scrolling_direction * a, graphics_location_y[i]))
        i = i + 1

    if a < 16:
        offset_1 = offset_1 + scrolling_direction * 75
        offset_2 = offset_2 + scrolling_direction * 50
        offset_3 = offset_3 + scrolling_direction * 30
        a = a + 1
    else:
        loading_settings = False
        loading_credits = False
        loading_menu = False
        loading_pre_game = False
        a = 0
        mouse_locked = False
        mouse_on_button = 0
        section = section_to_load
        offset_1 = 0
        offset_2 = 0
        offset_3 = 0


def get_mouse_on_button(button_ids,
                        button_x_0,
                        button_y_0,
                        button_x_z,
                        button_y_z):
    global mouse_pos
    global mouse_on_button

    i = 0
    while i < len(button_ids):
        if mouse_pos[0] >= button_x_0[i] and mouse_pos[0] < button_x_z[i] and mouse_pos[1] >= button_y_0[i] and mouse_pos[1] < button_y_z[i]:
            mouse_on_button = button_ids[i]
            break
        else:
            mouse_on_button = 0
        i = i + 1


def blit_buttons_selectable(button_ids,
                            button_graphics,
                            button_x,
                            button_y,
                            offsets,
                            button_duplicate_graphics):
    global screen
    global scalers
    i = 0
    while i < len(button_ids):
        button_duplicate_graphics[i] = pygame.transform.scale_by(button_graphics[i], scalers[i])
        screen.blit(button_duplicate_graphics[i],(offsets[i] + button_x[i] - ((scalers[i] - 1) * 450), + button_y[i] - ((scalers[i] - 1) * 360)))
        if mouse_on_button != button_ids[i]:
            if scalers[i] > 1:
                scalers[i] = scalers[i] - 0.05
        else:
            if scalers[i] < 1.1:
                scalers[i] = scalers[i] + 0.05
        i = i + 1

def document_change_value(document_name,
                          line_to_change,
                          new_value):

    read_file = open(document_name, "r")
    read_data = read_file.readlines()
    read_file.close()

    write_file = open(document_name, "w+")

    i=1
    while i <= len(read_data):
        if i == line_to_change:
            if i == len(read_data):
                write_file.write(str(new_value))
            else:
                write_file.write(str(new_value) + "\n")
        else:
            write_file.write(str(read_data[i-1]))
        i = i + 1
    write_file.close()


def document_read_decode(document_name,
                         type):
    read_file = open(document_name, "r")
    read_data = read_file.readlines()
    read_file.close()
    return_list = []

    i=0
    while i<len(read_data):
        temp = (list(read_data[i]))
        if temp.pop() == "\n":
            if type == "int":
                return_list.append(int("".join(temp)))
            else:
                return_list.append("".join(temp))
        else:
            if type == "int":
                return_list.append(int(read_data[i]))
            else:
                return_list.append(read_data[1])
        i = i + 1
    return return_list

def debug_print():
    print(mouse_pos)


if __name__ == '__main__':
    if os.name == 'nt':
        resolution_x = get_screen_resolution_windows()[0]
        resolution_y = get_screen_resolution_windows()[1]
    else:
        resolution_x = get_screen_resolution_linux()[0]
        resolution_y = get_screen_resolution_linux()[1]

    settings_data = document_read_decode("settings.txt", "int")


    flags = FULLSCREEN | DOUBLEBUF
    screen = pygame.display.set_mode((resolution_x, resolution_y), flags)

    menu_button_ng = pygame.image.load("menu_button_new_game.png").convert_alpha()
    menu_button_cr = pygame.image.load("menu_button_credits.png").convert_alpha()
    menu_button_st = pygame.image.load("menu_button_settings.png").convert_alpha()

    menu_button_ng2 = menu_button_ng
    menu_button_cr2 = menu_button_cr
    menu_button_st2 = menu_button_st

    menu_background = pygame.image.load("menu_bg.png").convert_alpha()
    menu_column_left = pygame.image.load("menu_collumn_more_right.png").convert_alpha()
    menu_column_right = pygame.image.load("menu_collumn_more_left.png").convert_alpha()
    menu_name = pygame.image.load("menu_name.png").convert_alpha()

    pre_game_button_normal = pygame.image.load("pre-game_button_normal.png").convert_alpha()
    pre_game_button_custom = pygame.image.load("pre-game_button_custom.png").convert_alpha()

    pre_game_button_normal2 = pre_game_button_normal
    pre_game_button_custom2 = pre_game_button_custom

    settings_button_music = pygame.image.load("settings_button_music.png").convert_alpha()
    settings_button_sound = pygame.image.load("settings_button_sound.png").convert_alpha()

    settings_button_music2 = settings_button_music
    settings_button_sound2 = settings_button_sound

    settings_on = pygame.image.load("settings_on.png").convert_alpha()
    settings_off = pygame.image.load("settings_off.png").convert_alpha()

    credits_author = pygame.image.load("credits_author.png").convert_alpha()
    credits_idea = pygame.image.load("credits_idea.png").convert_alpha()

    credits_author2 = credits_author
    credits_idea2 = credits_idea

    pygame.mixer.init()
    pygame.mixer.music.load("menu_music.mp3")
    pygame.mixer.music.play(-1)

    while (running):
        screen.fill((100, 100, 100))
        if settings_data[0] == 0:
            if music_volume > 0:
                music_volume = music_volume - 0.001
        else:
            if music_volume < 0.25:
                music_volume = music_volume + 0.001
        pygame.mixer.music.set_volume(music_volume)

        if section == "menu":
            button_count = 3

            screen.blit(menu_background, (476 + offset_3, 0))
            screen.blit(menu_column_left, (-960 + offset_2, 0))

            if mouse_locked == False:
                mouse_pos = list(pygame.mouse.get_pos())
                get_mouse_on_button([1, 2, 3],
                                    [86, 108, 140],
                                    [134, 373, 859],
                                    [570, 552, 514],
                                    [256, 495, 978])

            blit_buttons_selectable([1, 2, 3],
                                    [menu_button_ng, menu_button_st, menu_button_cr],
                                    [-166, -166, -166],
                                    [-166, 75, 555],
                                    [offset_1, offset_1, offset_1],
                                    [menu_button_ng2, menu_button_st2, menu_button_cr2])

            if loading_pre_game == True:
                load_section("pre-game",
                             [menu_column_right, pre_game_button_normal,
                              pre_game_button_custom],
                             [79, 2280, 2280],
                             [0, -166, 75],
                             [50, 75, 75],
                             -1)


            elif loading_settings == True:
                load_section("settings",
                             [menu_column_right, settings_button_music, settings_button_sound],
                             [79, 2220, 2220],
                             [0, -166, 75],
                             [50, 75, 75],
                             -1)

            elif loading_credits == True:
                load_section("credits",
                             [menu_column_right, credits_author, credits_idea],
                             [79, 2280, 2280],
                             [0, -166, 75],
                             [50, 75, 75],
                             -1)

            screen.blit(menu_name, (652, 467))


        elif section == "pre-game":
            button_count = 2
            screen.blit(menu_background, (-7 + offset_3, 0))
            screen.blit(menu_column_left, (-1664 + offset_2, 0))
            screen.blit(menu_column_right, (-721 + offset_2, 0))
            screen.blit(menu_name, (652, 467))

            if mouse_locked == False:
                mouse_pos = list(pygame.mouse.get_pos())
                get_mouse_on_button([1, 2],
                                    [1381, 1388],
                                    [137, 374],
                                    [1763, 1753],
                                    [256, 495])

            blit_buttons_selectable([1, 2],
                                    [pre_game_button_normal, pre_game_button_custom],
                                    [1080, 1080],
                                    [-166, 75],
                                    [offset_1, offset_1],
                                    [pre_game_button_normal2, pre_game_button_custom2])

            if loading_menu == True:
                load_section("menu",
                             [menu_column_left,
                              menu_button_ng,
                              menu_button_st,
                              menu_button_cr],
                             [-1760, -1366, -1366, -1366],
                             [0, -166, 75, 555],
                             [50, 75, 75, 75], 1)




        elif section == "settings":
            button_count = 2
            screen.blit(menu_background, (-7 + offset_3, 0))
            screen.blit(menu_column_left, (-1664 + offset_2, 0))
            screen.blit(menu_column_right, (-721 + offset_2, 0))
            screen.blit(menu_name, (652, 467))

            if settings_data[0] == 0:
                screen.blit(settings_off, (offset_1 + 1280, -166))
            else:
                screen.blit(settings_on, (offset_1 + 1280, -166))

            if settings_data[1] == 0:
                screen.blit(settings_off, (offset_1 + 1280, 75))
            else:
                screen.blit(settings_on, (offset_1 + 1280, 75))

            if mouse_locked == False:
                mouse_pos = list(pygame.mouse.get_pos())
                get_mouse_on_button([1, 2],
                                    [1326, 1303],
                                    [139, 376],
                                    [1616, 1638],
                                    [256, 499])

            blit_buttons_selectable([2,1],
                                    [settings_button_sound, settings_button_music],
                                    [980, 980],
                                    [75, -166],
                                    [offset_1, offset_1],
                                    [settings_button_sound2, settings_button_music2])


        elif section == "credits":
            button_count = 2
            screen.blit(menu_background, (-7 + offset_3, 0))
            screen.blit(menu_column_left, (-1664 + offset_2, 0))
            screen.blit(menu_column_right, (-721 + offset_2, 0))
            screen.blit(menu_name, (652, 467))

            if mouse_locked == False:
                mouse_pos = list(pygame.mouse.get_pos())
                get_mouse_on_button([1, 2],
                                    [1135, 1163],
                                    [100, 340],
                                    [1887, 1858],
                                    [216, 457])

            blit_buttons_selectable([1,2],
                                    [credits_author, credits_idea],
                                    [1020, 1020],
                                    [-166, 75],
                                    [offset_1, offset_1],
                                    [credits_author2, credits_idea2])



        if loading_menu == True:
            load_section("menu",
                         [menu_column_left,
                          menu_button_ng,
                          menu_button_st,
                          menu_button_cr],
                         [-1760, -1366, -1366, -1366],
                         [0, -166, 75, 555],
                         [50, 75, 75, 75],
                         1)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                running = False
            if section == "menu":
                if clicking == True or event.type == pygame.MOUSEBUTTONDOWN:
                    if clicking == True or event.button == 1:
                        clicking = False
                        if mouse_on_button == 1:
                            loading_pre_game = True
                        elif mouse_on_button == 2:
                            loading_settings = True
                        elif mouse_on_button == 3:
                            loading_credits = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        running = False

            elif section == "settings":
                if clicking == True or event.type == pygame.MOUSEBUTTONDOWN:
                    if clicking == True or event.button == 1:
                        clicking = False
                        document_change_value("settings.txt", mouse_on_button, ((settings_data[mouse_on_button - 1]) - 1) ** 2)
                        settings_data = document_read_decode("settings.txt", "int")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loading_menu = True

            elif section == "pre-game":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loading_menu = True
            elif section == "credits":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loading_menu = True
                elif clicking == True or event.type == pygame.MOUSEBUTTONDOWN:
                    if clicking == True or event.button == 1:
                        if mouse_on_button == 2:
                            webbrowser.open("https://github.com/sushio4", new=2)
                        elif mouse_on_button == 1:
                            webbrowser.open("https://github.com/DerQut", new=2)
                        clicking = False
                        mouse_on_button = 0
            if event.type == pygame.KEYDOWN:
                if mouse_locked == False:
                    for x in continue_events:
                        if event.key == x or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                            mouse_locked = True
                            mouse_on_button = 1
                            break
                else:
                    if event.key == pygame.K_UP:
                        if mouse_on_button > 1:
                            mouse_on_button = mouse_on_button-1
                        else:
                            mouse_on_button = button_count
                    elif event.key == pygame.K_DOWN:
                        if mouse_on_button < button_count:
                            mouse_on_button = mouse_on_button+1
                        else:
                            mouse_on_button = 1

                    for x in continue_events:
                        if event.key == x:
                            clicking = True
                            break
        if debug == True:
            debug_print()
        pygame.display.update()