import os

from flask import Flask, request, render_template, send_from_directory, current_app
from openpyxl import Workbook

from src import figures

MY_FIGURES = {
    "parallelepiped": "Параллелепипед",
    "sphere": "Сфера",
    "tetrahedron": "Тетраэдр"
}

UPLOAD_FOLDER = "download"
data_user = {}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def save_calc(user_id, param_1, param_2, param_3, p, figure, volume, area, weight):
    if user_id not in data_user:
        data_user[user_id] = [["Параметр 1", "Параметр 2", "Параметр 3", "Плотность", "Геометрическая фигура", "Объем", "Площадь поверхности", "Масса"]]

    if not param_1:
        param_1 = "None"

    if not param_2:
        param_2 = "None"

    if not param_3:
        param_3 = "None"

    data_user[user_id].append([param_1, param_2, param_3, p, figure, volume, area, weight])
    wb = Workbook()
    sheet = wb.active
    for i in data_user[user_id]:
        sheet.append(i)
    wb.save(app.config['UPLOAD_FOLDER'] + f"/results_{user_id}.xlsx")


@app.route('/')
def home():
    return render_template('index.html', title="Калькулятор фигур")


@app.route('/download', methods=['GET', 'POST'])
def download():
    user_id = request.headers.get('X-Forwarded-For', request.remote_addr)
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path=f"results_{user_id}.xlsx")


@app.route("/figures/<figure_type>", methods=['GET', 'POST'])
def calc_figures(figure_type):
    title = f"Фигура | {MY_FIGURES.get(figure_type, 'NOT-FOUND')}"
    user_id = request.headers.get('X-Forwarded-For', request.remote_addr)

    if request.method == "POST":
        # Запрос всех параметров
        a = request.form.get("a", "")
        b = request.form.get("b", "")
        r = request.form.get("r", "")
        h = request.form.get("h", "")
        p = request.form.get("p", "")

        # Проверка валидности данных
        data_err = {
            "title": title,
            "err_a": a.isalpha(),
            "err_b": b.isalpha(),
            "err_r": r.isalpha(),
            "err_h": h.isalpha()
        }
        err_parallelepiped = figure_type == "parallelepiped" and (data_err["err_a"] or data_err["err_b"] or data_err["err_h"])
        err_sphere = figure_type == "sphere" and data_err["err_r"]
        err_tetrahedron = figure_type == "tetrahedron" and (data_err["err_a"])

        # Отображение ошибки
        if err_parallelepiped or err_sphere or err_tetrahedron:
            return render_template(f'{figure_type}.html', **data_err)

        # Расчет значений
        figure = None

        if figure_type == "parallelepiped":
            figure = figures.Parallelepiped(float(a), float(b), float(h))
        elif figure_type == "tetrahedron":
            figure = figures.Tetrahedron(float(a))
        elif figure_type == "sphere":
            figure = figures.Sphere(float(r))

        volume = round(figure.calc_volume(), 1)
        area = round(figure.calc_surface_area(), 1)
        weigth = round(figure.calc_weight(float(p)), 1)

        # Сохранение текущих расчетов
        save_calc(user_id, r or a, b, h, p, MY_FIGURES.get(figure_type), volume, area, weigth)
        return render_template(
            f'{figure_type}.html',
            title=title,
            volume=volume,
            area=area,
            weigth=weigth
        )

    return render_template(f'{figure_type}.html', title=title)


if __name__ == '__main__':
    app.run()
