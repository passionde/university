import os

import docx
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

import premises

# Глобальные настройки
Window.size = (600, 400)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Калькулятор тепловой мощности"

document = docx.Document()


class ScreenMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_room = Button(
            text="Комната",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_room,
        )
        button_apartment = Button(
            text="Квартира",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_apartment,
        )
        button_house = Button(
            text="Многоэтажный дом",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_house,
        )

        button_save = Button(
            text="Сохранить расчеты",
            background_color=[146/255, 52/255, 235/255, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_save,
        )

        boxlayout.add_widget(button_room)
        boxlayout.add_widget(button_apartment)
        boxlayout.add_widget(button_house)
        boxlayout.add_widget(button_save)
        self.add_widget(boxlayout)

    def _on_press_button_room(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'room'

    def _on_press_button_apartment(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'apartment'

    def _on_press_button_house(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'house'

    def _on_press_button_save(self, *args):
        message = f'Файл успешно сохранен в {os.path.abspath(os.curdir)}'
        try:
            document.save("history.docx")
        except:
            message = "Ошибка при попытки сохранения"

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text=''))
        layout.add_widget(Label(text=message))
        layout.add_widget(Label(text=''))
        layout.add_widget(Label(text=''))

        button = Button(text='Закрыть')
        layout.add_widget(button)
        popup = Popup(title='Уведомление', content=layout)
        popup.background_color = (255/255, 186/255, 3/255, 1)
        button.bind(on_press=popup.dismiss)
        popup.open()


class ScreenPremises(Screen):
    def __init__(self, type_premises, **kwargs):
        super().__init__(**kwargs)
        self.type_premises = type_premises

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        text = ""
        if type_premises == "apartment":
            text = "Квартира"
        elif type_premises == "house":
            text = "Многоэтажный дом"
        elif type_premises == "room":
            text = "Комната"
        else:
            raise "unknown type_premises"

        label = Label(text=text)
        self.input_width = TextInput(hint_text='Введите ширину (метры)', multiline=False)
        self.input_length = TextInput(hint_text='Введите длину (метры)', multiline=False)

        text = "Введите количество комнат" if type_premises == "apartment" else "Введите количество этажей"
        self.input_number = TextInput(hint_text=text, multiline=False)

        self.result = Label(text='')

        button_get_result = Button(
            text="Рассчитать",
            background_color=[0, 1.5, 3, 1],
            on_press=self._get_result,
        )

        button_return = Button(
            text="<- Назад",
            background_color=[0, 1.5, 3, 1],
            on_press=self._return_menu,
        )

        boxlayout.add_widget(label)
        boxlayout.add_widget(self.input_width)
        boxlayout.add_widget(self.input_length)

        if type_premises in ["apartment", "house"]:
            boxlayout.add_widget(self.input_number)

        boxlayout.add_widget(self.result)
        boxlayout.add_widget(button_get_result)
        boxlayout.add_widget(button_return)

        self.add_widget(boxlayout)

    def _return_menu(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def _get_result(self, *args):
        is_correct_data = True
        if self.type_premises in ["apartment", "house"]:
            is_correct_data = str(self.input_width.text).isnumeric() and str(
                self.input_length.text).isnumeric() and str(self.input_number.text).isnumeric()
        else:
            is_correct_data = str(self.input_width.text).isnumeric() and str(self.input_length.text).isnumeric()

        if is_correct_data:
            prem_class = premises.Room(float(self.input_width.text), float(self.input_length.text))
            if self.type_premises == "apartment":
                prem_class = premises.Apartment(float(self.input_width.text), float(self.input_length.text),
                                                int(self.input_number.text))
            elif self.type_premises == "house":
                prem_class = premises.House(float(self.input_width.text), float(self.input_length.text),
                                            int(self.input_number.text))
            text = f"Площадь помещения: {prem_class.calc_area()} М^2\nТепловой мощности для обогрева: {prem_class.calc_heat_power()} Вт"

            self.result.text = text
            document.add_paragraph(f"[{self.type_premises}]\n{text}")
        else:
            self.input_width.text = ""
            self.input_length.text = ""
            self.input_number.text = ""


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMenu(name='menu'))
        sm.add_widget(ScreenPremises("room", name='room'))
        sm.add_widget(ScreenPremises("apartment", name='apartment'))
        sm.add_widget(ScreenPremises("house", name='house'))

        return sm


if __name__ == "__main__":
    MyApp().run()
