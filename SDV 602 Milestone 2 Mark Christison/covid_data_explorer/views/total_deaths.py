import PySimpleGUI as sg
import menu
import elements.popup_calendar as popup_calendar
from elements.draw_figure import draw_figure, fig
from csv_data_reader import countries as countries_list


def view_total_deaths_window():
    col1 = [[sg.Canvas(key='-CANVAS-')]]

    col2 = [[sg.Text("Choose a Country"), sg.Combo(countries_list)],
            [sg.Button(button_text="Start Data", size=(15, 1)), sg.Button(button_text="End Data", size=(15, 1))],
            [sg.Button(button_text="Update Graph", size=(15, 1)), sg.Button(button_text="Reset Graph", size=(15, 1))]]

    layout = [[sg.Menu(menu.menu_def, tearoff=False)],
              [sg.Text("Current Deaths", size=(100, 3), key='-TITLE-', justification='center')],
              [sg.Column(col1), sg.Column(col2, element_justification='center')]]

    window = sg.Window(menu.TITLE + ' - Current Deaths', layout, finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, fig) #TODO

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == "Start Data":
            start_date = popup_calendar.popup_get_date()
        if event == "End Data":
            end_date = popup_calendar.popup_get_date()
        if event in menu.menu_options:
            menu.run_menu(event, window)
    window.close()
