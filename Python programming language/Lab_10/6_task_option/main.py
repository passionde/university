import os

from openpyxl.workbook import Workbook

from particles import electron
from particles import proton
from particles import neutron

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Элементарная частица: '), sg.Listbox(["Электрон", "Протон", "Нейтрон"], key="_particle_", enable_events=True, size=(15, 3), no_scrollbar=True, default_values=["Электрон"])],
          [sg.Text(size=(45, 3), key='-RESULT-', text_color="green")],
          [sg.Button('Ok'), sg.Button("Save"), sg.Button('Cancel')]]

window = sg.Window('Элементарные частицы', layout)

data = [["Номер", "Частица", "Удельный заряд", "Комптоновская длина волны"]]


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "Ok":
        particle = values.get("_particle_")[-1]
        specific_charge = 0
        compton_wavelength = 0

        if particle == "Электрон":
            specific_charge = electron.calc_specific_charge()
            compton_wavelength = electron.calc_compton_wavelength()
        elif particle == "Нейтрон":
            specific_charge = neutron.calc_specific_charge()
            compton_wavelength = neutron.calc_compton_wavelength()
        elif particle == "Протон":
            specific_charge = proton.calc_specific_charge()
            compton_wavelength = proton.calc_compton_wavelength()

        data.append([len(data), particle, f"{specific_charge:2.2e}", f"{compton_wavelength:2.2e}"])
        window["-RESULT-"].update(f'Результаты расчета для частицы "{particle}":\n\tУдельный заряд = {specific_charge:2.2e}\n\tКомптоновская длина волны = {compton_wavelength:2.2e}')

    if event == "Save":
        path = sg.popup_get_folder("Выберите файл для сохранения прогресса")

        if path is None:
            continue

        wb = Workbook()
        sheet = wb.active
        for i in data:
            sheet.append(i)
        path = os.path.join(path, 'results.xlsx')
        wb.save(path)

        sg.popup("Результаты успешно сохранены")

window.close()
