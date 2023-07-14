import os.path

import wx

from openpyxl import Workbook

import src.sphere as sphere
import src.tetrahedron as tetrahedron
import src.parallelepiped as parallelepiped


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Создание окна
        super().__init__(parent, title=title, pos=(100, 100), size=(300, 340), style=wx.CAPTION | wx.CLOSE_BOX)

        # Параметры фигуры
        self.figure: wx.ComboBox | None = None
        self.material: wx.ComboBox | None = None

        self.param_t_1: wx.StaticText | None = None
        self.param_t_2: wx.StaticText | None = None
        self.param_t_3: wx.StaticText | None = None

        self.param_i_1: wx.TextCtrl | None = None
        self.param_i_2: wx.TextCtrl | None = None
        self.param_i_3: wx.TextCtrl | None = None

        self.data = [["Параметр 1", "Параметр 2", "Параметр 3", "Материал",
                      "Геометрическая фигура", "Объем", "Площадь поверхности", "Масса"]]

        self.Center()

        # Создание контейнера
        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.vbox)

        # Инициализация виджетов
        self.init_set_figure()
        self.init_set_material()
        self.init_params()
        self.init_buttons()

    def init_set_figure(self):
        """Создает виджеты для выбора фигуры"""
        # Выбор фигуры
        set_figure = wx.BoxSizer()

        # Надпись выбора фигуры
        st_figure = wx.StaticText(self.panel, label=f"{'Фигура:':<20}")
        set_figure.Add(st_figure, flag=wx.EXPAND | wx.ALL, border=10)

        # Список доступных фигур
        self.figure = wx.ComboBox(self.panel, pos=(50, 30), choices=["Параллелепипед", "Тетраэдр", "Шар"],
                                  style=wx.CB_READONLY, size=wx.Size(150, 25))
        self.figure.SetSelection(0)
        self.figure.Bind(wx.EVT_COMBOBOX, self.set_frame)
        set_figure.Add(self.figure, flag=wx.EXPAND | wx.ALL, border=8)
        self.vbox.Add(set_figure)

        # Горизонтальная линия
        self.vbox.Add(wx.StaticLine(self.panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

    def init_set_material(self):
        """Создает виджеты для выбора материала"""
        set_material = wx.BoxSizer()

        # Надпись выбора фигуры
        st_material = wx.StaticText(self.panel, label=f"{'Материал:':<17}")
        set_material.Add(st_material, flag=wx.ALL, border=10)

        # Список доступных материалов
        self.material = wx.ComboBox(self.panel, pos=(50, 30), choices=["Медь", "Железо", "Олово"],
                                    style=wx.CB_READONLY, size=wx.Size(150, 25))
        self.material.SetSelection(0)
        set_material.Add(self.material, flag=wx.ALL, border=8)
        self.vbox.Add(set_material)

    def init_params(self):
        param_1 = wx.BoxSizer()
        param_2 = wx.BoxSizer()
        param_3 = wx.BoxSizer()

        self.param_i_1 = wx.TextCtrl(self.panel, size=wx.Size(150, 25))
        self.param_i_2 = wx.TextCtrl(self.panel, size=wx.Size(150, 25))
        self.param_i_3 = wx.TextCtrl(self.panel, size=wx.Size(150, 25))

        self.param_t_1 = wx.StaticText(self.panel, label=f"{'Длина (a) ':19}")
        self.param_t_2 = wx.StaticText(self.panel, label=f"{'Ширина (b)':17}")
        self.param_t_3 = wx.StaticText(self.panel, label=f"{'Высота (h)':19}")

        param_1.Add(self.param_t_1, flag=wx.ALL | wx.EXPAND, border=10)
        param_1.Add(self.param_i_1, flag=wx.ALL | wx.EXPAND, border=10)

        param_2.Add(self.param_t_2, flag=wx.ALL | wx.EXPAND, border=10)
        param_2.Add(self.param_i_2, flag=wx.ALL | wx.EXPAND, border=10)

        param_3.Add(self.param_t_3, flag=wx.ALL | wx.EXPAND, border=10)
        param_3.Add(self.param_i_3, flag=wx.ALL | wx.EXPAND, border=10)

        self.vbox.Add(param_1)
        self.vbox.Add(param_2)
        self.vbox.Add(param_3)

        # Горизонтальная линия
        self.vbox.Add(wx.StaticLine(self.panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

    def init_buttons(self):
        buttons = wx.BoxSizer()

        calc = wx.Button(self.panel, label="Рассчитать")
        download = wx.Button(self.panel, label="Сохранить")

        calc.Bind(wx.EVT_BUTTON, self.calculate)
        download.Bind(wx.EVT_BUTTON, self.download)

        buttons.Add(calc, flag=wx.ALL | wx.EXPAND, border=30)
        buttons.Add(download, flag=wx.ALL | wx.EXPAND, border=30)

        self.vbox.Add(buttons, flag=wx.EXPAND)

    def zero_params(self):
        self.param_t_1.SetLabelText("")
        self.param_t_2.SetLabelText("")
        self.param_t_3.SetLabelText("")

        self.param_i_1.Hide()
        self.param_i_2.Hide()
        self.param_i_3.Hide()

    def set_frame(self, event: wx.CommandEvent):
        # Обнуление значений
        self.zero_params()

        # Получение фигуры
        figure = event.GetString()

        if figure == "Шар":
            self.param_t_1.SetLabelText('Радиус')
            self.param_i_1.Show()
        elif figure == "Тетраэдр":
            self.param_t_1.SetLabelText('Длина ребер')
            self.param_i_1.Show()
        elif figure == "Параллелепипед":
            self.param_t_1.SetLabelText('Длина (a)')
            self.param_t_2.SetLabelText('Ширина (b)')
            self.param_t_3.SetLabelText('Высота (h)')

            self.param_i_1.Show()
            self.param_i_2.Show()
            self.param_i_3.Show()

    def add_data(self, *, figure, material, volume, surface_area, weight, param_1, param_2, param_3):
        self.data.append([param_1, param_2, param_3, material, figure, volume, surface_area, weight])

    def calculate(self, event: wx.CommandEvent):
        figure = self.figure.GetValue()
        material_p = {"Медь": 8.96, "Железо": 7.874, "Олово": 7.3}.get(self.material.GetValue(), 0)
        message_tmp = "Фигура: {}\n\tОбъем: {} см3\n\tПлощадь поверхности: {} см2\n\tМасса ({}): {} грамм"

        volume = 0
        surface_area = 0
        weight = 0

        param_1 = 0
        param_2 = 0
        param_3 = 0

        try:
            if figure == "Шар":
                param_1 = float(self.param_i_1.GetValue())
                volume = sphere.calc_volume(param_1)
                surface_area = sphere.calc_surface_area(param_1)
                weight = sphere.calc_weight(param_1, material_p)

            elif figure == "Тетраэдр":
                param_1 = float(self.param_i_1.GetValue())
                volume = tetrahedron.calc_volume(param_1)
                surface_area = tetrahedron.calc_surface_area(param_1)
                weight = tetrahedron.calc_weight(param_1, material_p)

            elif figure == "Параллелепипед":
                param_1 = float(self.param_i_1.GetValue())
                param_2 = float(self.param_i_2.GetValue())
                param_3 = float(self.param_i_3.GetValue())

                volume = round(parallelepiped.calc_volume(param_1, param_2, param_3), 2)
                surface_area = round(parallelepiped.calc_surface_area(param_1, param_2, param_3), 2)
                weight = round(parallelepiped.calc_weight(param_1, param_2, param_3, material_p), 2)

            wx.MessageBox(message_tmp.format(figure, round(volume, 2), round(surface_area, 2),
                                             self.material.GetValue(), round(weight, 2)))
            self.add_data(figure=figure, material=self.material.GetValue(), volume=volume, surface_area=surface_area,
                          weight=weight, param_1=param_1, param_2=param_2 or "-", param_3=param_3 or "-")
        except:
            wx.MessageBox("При расчетах произошла ошибка, проверьте введенные данные")

    def download(self, event: wx.CommandEvent):
        path = None

        # Инициализация выбора папки
        dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            dialog.Destroy()
            return

        dialog.Destroy()

        # Сохранение в файла
        try:
            wb = Workbook()
            sheet = wb.active
            for i in self.data:
                sheet.append(i)
            path = os.path.join(path, 'results.xlsx')
            wb.save(path)
            wx.MessageBox(f"Файл успешно сохранен по пути:\n{path}")
        except:
            wx.MessageBox("Ошибка при попытке сохранить файл")


app = wx.App()
frame = MyFrame(None, "Геометрический калькулятор")
frame.Show()
app.MainLoop()
