from flexx import flx, ui, event
import particles


class App(flx.Widget):
    def init(self):
        self.data = [["Номер", "Частица", "Удельный заряд", "Комптоновская длина волны"]]
        self.e = particles.Electron()
        self.n = particles.Neutron()
        self.p = particles.Proton()


        with flx.HSplit(flex=3):
            flx.HBox()  # Отступ

            with flx.VBox():
                flx.HBox()  # Отступ
                with flx.HBox():
                    ui.Label(wrap=True, text='Элементарная частица:')
                    self.particles = ui.ComboBox(editable=True,
                                            options=("Электрон", "Нейтрон", "Протон"))
                    self.btn_save = flx.Label()
                    self.btn_save.set_html(
                        '<a href="https://drive.google.com/uc?export=download&id=1-PC4-qhPAqs8v8CJqQXWG7IiDkQQnL5e" download="results.xlsx" target=_blank>Скачать справку</a>')

                with flx.VBox():
                    self.result_1 = flx.Label(wrap=True, text='', style='color: green; text-align: center;')
                    self.result_2 = flx.Label(wrap=True, text='', style='color: green; text-align: center;')
                    self.result_3 = flx.Label(wrap=True, text='', style='color: green; text-align: center;')

                with flx.VBox():
                    flx.HBox()  # Отступ
                    self.btn = flx.Button(text='Рассчитать')
                    flx.HBox()  # Отступ
                flx.HBox()  # Отступ
            flx.HBox()  # Отступ

    @event.reaction('btn.pointer_down')
    def _print_result_text(self, *events):
        particle = self.particles.text
        specific_charge = 0
        compton_wavelength = 0

        if particle == "Электрон":
            specific_charge = self.e.calc_specific_charge()
            compton_wavelength = self.e.calc_compton_wavelength()
        elif particle == "Нейтрон":
            specific_charge = self.n.calc_specific_charge()
            compton_wavelength = self.n.calc_compton_wavelength()
        elif particle == "Протон":
            specific_charge = self.p.calc_specific_charge()
            compton_wavelength = self.p.calc_compton_wavelength()
        else:
            self.result_1.set_text("")
            self.result_2.set_text("")
            self.result_3.set_text("")
            return

        self.result_1.set_text(f'Результаты расчета для частицы "{particle}":')
        self.result_2.set_text(f'Удельный заряд = {specific_charge:2.2e}')
        self.result_3.set_text(f'Комптоновская длина волны = {compton_wavelength:2.2e}')

        self.data.append([len(self.data), particle, f"{specific_charge:2.2e}", f"{compton_wavelength:2.2e}"])


app = flx.App(App)
app.launch('browser')
flx.run()

