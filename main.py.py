
# -*- coding: utf-8 -*-
# دستیار هوشمند دانش‌آموز - نسخه Kivy برای اندروید

import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle, Rectangle, Line
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.text import Label as CoreLabel

BG = "#F3F4F6"
CARD = "#FFFFFF"
PRIMARY = "#3B82F6"
SUCCESS = "#10B981"
ORANGE = "#F59E0B"
PURPLE = "#8B5CF6"
RED = "#EF4444"
TEXT = "#1F2937"
GRAY = "#6B7280"
BORDER = "#E5E7EB"

KV = r'''
#:import dp kivy.metrics.dp

<RoundButton@Button>:
    background_normal: ""
    background_down: ""
    background_color: 0,0,0,0
    color: 1,1,1,1
    font_size: "15sp"
    bold: True
    canvas.before:
        Color:
            rgba: app.hex_color(self.btn_color)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(14),]

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: app.hex_color("#F3F4F6")
            Rectangle:
                pos: self.pos
                size: self.size

        ScrollView:
            do_scroll_x: False
            bar_width: dp(4)

            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(16)
                spacing: dp(14)

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: dp(125)
                    padding: dp(15)
                    spacing: dp(4)
                    canvas.before:
                        Color:
                            rgba: app.hex_color("#3B82F6")
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(20),]

                    Label:
                        text: "دستیار هوشمند دانش‌آموز"
                        font_size: "25sp"
                        bold: True
                        color: 1,1,1,1
                        halign: "center"
                        valign: "middle"
                        text_size: self.size

                    Label:
                        text: "سیستم جامع مدیریت و تحلیل عملکرد تحصیلی"
                        font_size: "13sp"
                        color: app.hex_color("#DBEAFE")
                        halign: "center"
                        valign: "middle"
                        text_size: self.size

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: dp(315)
                    padding: dp(16)
                    spacing: dp(10)
                    canvas.before:
                        Color:
                            rgba: app.hex_color("#FFFFFF")
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(18),]
                        Color:
                            rgba: app.hex_color("#E5E7EB")
                        Line:
                            rounded_rectangle: (self.x,self.y,self.width,self.height,18)
                            width: 1

                    Label:
                        text: "ثبت دانش‌آموز جدید"
                        size_hint_y: None
                        height: dp(40)
                        font_size: "20sp"
                        bold: True
                        color: app.hex_color("#1F2937")

                    GridLayout:
                        cols: 2
                        spacing: dp(8)
                        size_hint_y: None
                        height: dp(185)

                        Label:
                            text: "نام دانش‌آموز"
                            color: app.hex_color("#6B7280")
                        TextInput:
                            id: name_input
                            multiline: False
                            halign: "center"
                            font_size: "16sp"

                        Label:
                            text: "ریاضی"
                            color: app.hex_color("#6B7280")
                        TextInput:
                            id: math_input
                            multiline: False
                            input_filter: "float"
                            halign: "center"
                            font_size: "16sp"

                        Label:
                            text: "علوم"
                            color: app.hex_color("#6B7280")
                        TextInput:
                            id: science_input
                            multiline: False
                            input_filter: "float"
                            halign: "center"
                            font_size: "16sp"

                        Label:
                            text: "فارسی"
                            color: app.hex_color("#6B7280")
                        TextInput:
                            id: persian_input
                            multiline: False
                            input_filter: "float"
                            halign: "center"
                            font_size: "16sp"

                        Label:
                            text: "زبان"
                            color: app.hex_color("#6B7280")
                        TextInput:
                            id: english_input
                            multiline: False
                            input_filter: "float"
                            halign: "center"
                            font_size: "16sp"

                    RoundButton:
                        text: "ثبت اطلاعات"
                        btn_color: "#10B981"
                        size_hint_y: None
                        height: dp(50)
                        on_release: root.save_student()

                Label:
                    text: "امکانات برنامه"
                    size_hint_y: None
                    height: dp(35)
                    font_size: "20sp"
                    bold: True
                    color: app.hex_color("#1F2937")

                GridLayout:
                    cols: 2
                    spacing: dp(10)
                    size_hint_y: None
                    height: dp(280)

                    RoundButton:
                        text: "مشاهده لیست دانش‌آموزان"
                        btn_color: "#3B82F6"
                        on_release: root.show_students()

                    RoundButton:
                        text: "بالاترین معدل"
                        btn_color: "#F59E0B"
                        on_release: root.highest_average()

                    RoundButton:
                        text: "جستجوی دانش‌آموز"
                        btn_color: "#8B5CF6"
                        on_release: root.search_student()

                    RoundButton:
                        text: "تحلیل کارنامه و نمودار"
                        btn_color: "#10B981"
                        on_release: root.analyze_student()

                    RoundButton:
                        text: "حذف دانش‌آموز"
                        btn_color: "#E11D48"
                        on_release: root.delete_student()

                    RoundButton:
                        text: "حذف همه دانش‌آموزان"
                        btn_color: "#991B1B"
                        on_release: root.delete_all_students()

                RoundButton:
                    text: "خروج از برنامه"
                    btn_color: "#EF4444"
                    size_hint_y: None
                    height: dp(48)
                    on_release: app.stop()

                Widget:
                    size_hint_y: None
                    height: dp(20)
'''

class MainScreen(Screen):

    def popup_message(self, title, message):
        box = BoxLayout(orientation="vertical", padding=15, spacing=12)
        scroll = ScrollView()
        label = Label(
            text=message,
            color=App.get_running_app().hex_color(TEXT),
            font_size="16sp",
            halign="right",
            valign="top",
            size_hint_y=None
        )
        label.bind(texture_size=lambda obj, value: setattr(obj, "height", max(value[1], 80)))
        scroll.add_widget(label)
        box.add_widget(scroll)
        button = Button(
            text="باشه",
            size_hint_y=None,
            height=48,
            background_normal="",
            background_color=App.get_running_app().hex_color(PRIMARY)
        )
        box.add_widget(button)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.65), title_align="center")
        button.bind(on_release=popup.dismiss)
        popup.open()

    def read_students(self):
        result = []
        path = App.get_running_app().file_name
        if not os.path.exists(path):
            return result
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 7:
                        result.append(data)
        except Exception as e:
            self.popup_message("خطای فایل", str(e))
        return result

    def write_students(self, students):
        with open(App.get_running_app().file_name, "w", encoding="utf-8") as f:
            for s in students:
                f.write(",".join(s) + "\n")

    def calculate_status(self, average):
        if average < 10:
            return "نیاز به تلاش بیشتر"
        elif average <= 15:
            return "متوسط"
        return "خیلی خوب"

    def validate_score(self, value):
        try:
            score = float(value)
            if 0 <= score <= 20:
                return True, score
        except ValueError:
            pass
        return False, None

    def save_student(self):
        name = self.ids.name_input.text.strip()
        if not name:
            self.popup_message("خطا", "نام دانش‌آموز را وارد کنید.")
            return

        raw = [
            ("ریاضی", self.ids.math_input.text),
            ("علوم", self.ids.science_input.text),
            ("فارسی", self.ids.persian_input.text),
            ("زبان", self.ids.english_input.text)
        ]
        scores = []
        for subject, value in raw:
            ok, score = self.validate_score(value)
            if not ok:
                self.popup_message("خطا", f"نمره {subject} باید عددی بین 0 تا 20 باشد.")
                return
            scores.append(score)

        average = sum(scores) / 4
        status = self.calculate_status(average)

        try:
            with open(App.get_running_app().file_name, "a", encoding="utf-8") as f:
                f.write(
                    f"{name},{scores[0]},{scores[1]},{scores[2]},"
                    f"{scores[3]},{round(average,2)},{status}\n"
                )
        except Exception as e:
            self.popup_message("خطای ذخیره", str(e))
            return

        self.popup_message(
            "ثبت موفق",
            f"اطلاعات {name} ذخیره شد.\n\nمعدل: {round(average,2)}\nوضعیت: {status}"
        )
        for key in ("name_input", "math_input", "science_input", "persian_input", "english_input"):
            self.ids[key].text = ""

    def show_students(self):
        students = self.read_students()
        if not students:
            self.popup_message("لیست دانش‌آموزان", "هنوز دانش‌آموزی ذخیره نشده است.")
            return
        text = ""
        for i, s in enumerate(students, 1):
            text += (
                f"{i}. {s[0]}\n"
                f"ریاضی: {s[1]}   علوم: {s[2]}\n"
                f"فارسی: {s[3]}   زبان: {s[4]}\n"
                f"معدل: {s[5]}   وضعیت: {s[6]}\n"
                + "─" * 28 + "\n"
            )
        self.popup_message("لیست دانش‌آموزان ذخیره‌شده", text)

    def highest_average(self):
        students = self.read_students()
        if not students:
            self.popup_message("بالاترین معدل", "هنوز دانش‌آموزی ذخیره نشده است.")
            return
        best = max(students, key=lambda s: float(s[5]))
        self.popup_message(
            "بالاترین معدل",
            f"🏆 دانش‌آموز برتر 🏆\n\n"
            f"نام: {best[0]}\nمعدل: {best[5]}\nوضعیت: {best[6]}\n\n"
            f"ریاضی: {best[1]}\nعلوم: {best[2]}\nفارسی: {best[3]}\nزبان: {best[4]}"
        )

    def text_input_popup(self, title, hint, callback):
        box = BoxLayout(orientation="vertical", padding=15, spacing=12)
        entry = TextInput(hint_text=hint, multiline=False, halign="center", font_size="17sp",
                          size_hint_y=None, height=52)
        box.add_widget(entry)
        button = Button(text="ادامه", size_hint_y=None, height=48,
                        background_normal="",
                        background_color=App.get_running_app().hex_color(PRIMARY))
        box.add_widget(button)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.35), title_align="center")

        def go(_):
            value = entry.text.strip()
            if not value:
                self.popup_message("خطا", "مقدار را وارد کنید.")
                return
            popup.dismiss()
            callback(value)

        button.bind(on_release=go)
        popup.open()

    def search_student(self):
        self.text_input_popup("جستجوی دانش‌آموز", "بخشی از نام را وارد کنید", self.perform_search)

    def perform_search(self, query):
        matches = [s for s in self.read_students() if query in s[0]]
        if not matches:
            self.popup_message("نتیجه", "دانش‌آموزی یافت نشد.")
            return
        if len(matches) == 1:
            self.show_student_report(matches[0])
            return

        box = BoxLayout(orientation="vertical", padding=10, spacing=8)
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=8, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))
        popup = Popup(title=f"{len(matches)} دانش‌آموز یافت شد", content=box,
                      size_hint=(0.9, 0.7), title_align="center")
        for student in matches:
            b = Button(text=student[0], size_hint_y=None, height=50,
                       background_normal="",
                       background_color=App.get_running_app().hex_color(CARD),
                       color=App.get_running_app().hex_color(TEXT))
            b.bind(on_release=lambda inst, s=student: (popup.dismiss(), self.show_student_report(s)))
            grid.add_widget(b)
        scroll.add_widget(grid)
        box.add_widget(scroll)
        close = Button(text="بستن", size_hint_y=None, height=45,
                       background_normal="",
                       background_color=App.get_running_app().hex_color(PRIMARY))
        close.bind(on_release=popup.dismiss)
        box.add_widget(close)
        popup.open()

    def show_student_report(self, s):
        self.popup_message(
            "کارنامه",
            f"نام: {s[0]}\n\n"
            f"ریاضی: {s[1]}\nعلوم: {s[2]}\n"
            f"فارسی: {s[3]}\nزبان: {s[4]}\n\n"
            f"معدل: {s[5]}\nوضعیت: {s[6]}"
        )

    def analyze_student(self):
        self.text_input_popup("تحلیل کارنامه", "نام کامل دانش‌آموز را وارد کنید", self.perform_analysis)

    def perform_analysis(self, name):
        target = next((s for s in self.read_students() if s[0] == name), None)
        if not target:
            self.popup_message("تحلیل", "دانش‌آموز یافت نشد.")
            return

        subjects = {
            "ریاضی": float(target[1]),
            "علوم": float(target[2]),
            "فارسی": float(target[3]),
            "زبان": float(target[4])
        }
        average = float(target[5])
        best = max(subjects, key=subjects.get)
        weak = min(subjects, key=subjects.get)

        result = (
            f"دانش‌آموز: {name}\n\n"
            f"معدل: {average}\n\n"
            f"بهترین درس: {best} ({subjects[best]})\n"
            f"نیازمند تمرین: {weak} ({subjects[weak]})\n\n"
            f"تحلیل کلی: {self.calculate_status(average)}"
        )
        self.popup_message("نتیجه تحلیل", result)
        self.show_chart(name, subjects)

    def show_chart(self, name, subjects):
        chart = ChartWidget(subjects=subjects)
        box = BoxLayout(orientation="vertical", padding=8, spacing=8)
        box.add_widget(chart)
        close = Button(text="بستن", size_hint_y=None, height=48,
                       background_normal="",
                       background_color=App.get_running_app().hex_color(PRIMARY))
        box.add_widget(close)
        popup = Popup(title=f"نمودار عملکرد {name}", content=box,
                      size_hint=(0.95, 0.72), title_align="center")
        close.bind(on_release=popup.dismiss)
        popup.open()

    def delete_student(self):
        self.text_input_popup("حذف دانش‌آموز", "نام کامل دانش‌آموز را وارد کنید", self.perform_delete)

    def perform_delete(self, name):
        students = self.read_students()
        new_list = [s for s in students if s[0] != name]
        if len(students) == len(new_list):
            self.popup_message("حذف", "دانش‌آموز یافت نشد.")
            return

        box = BoxLayout(orientation="vertical", padding=15, spacing=12)
        box.add_widget(Label(text=f"آیا از حذف «{name}» مطمئن هستید؟",
                             color=App.get_running_app().hex_color(TEXT)))
        row = BoxLayout(spacing=10, size_hint_y=None, height=50)
        yes = Button(text="بله، حذف شود", background_normal="",
                     background_color=App.get_running_app().hex_color(RED))
        no = Button(text="انصراف", background_normal="",
                    background_color=App.get_running_app().hex_color(GRAY))
        row.add_widget(yes)
        row.add_widget(no)
        box.add_widget(row)
        popup = Popup(title="تایید حذف", content=box, size_hint=(0.9, 0.32))
        no.bind(on_release=popup.dismiss)

        def confirm(_):
            self.write_students(new_list)
            popup.dismiss()
            self.popup_message("موفق", "دانش‌آموز حذف شد.")

        yes.bind(on_release=confirm)
        popup.open()

    def delete_all_students(self):
        path = App.get_running_app().file_name
        if not os.path.exists(path):
            self.popup_message("حذف", "فایلی وجود ندارد.")
            return

        box = BoxLayout(orientation="vertical", padding=15, spacing=12)
        box.add_widget(Label(
            text="آیا از حذف تمام اطلاعات مطمئن هستید؟\nاین عمل بازگشت‌ناپذیر است!",
            color=App.get_running_app().hex_color(TEXT)
        ))
        row = BoxLayout(spacing=10, size_hint_y=None, height=50)
        yes = Button(text="حذف همه", background_normal="",
                     background_color=App.get_running_app().hex_color(RED))
        no = Button(text="انصراف", background_normal="",
                    background_color=App.get_running_app().hex_color(GRAY))
        row.add_widget(yes)
        row.add_widget(no)
        box.add_widget(row)
        popup = Popup(title="تایید", content=box, size_hint=(0.9, 0.35))
        no.bind(on_release=popup.dismiss)

        def confirm(_):
            try:
                os.remove(path)
            except Exception:
                pass
            popup.dismiss()
            self.popup_message("موفق", "تمام اطلاعات حذف شد.")

        yes.bind(on_release=confirm)
        popup.open()


class ChartWidget(Widget):
    def __init__(self, subjects=None, **kwargs):
        self.subjects = subjects or {}
        super().__init__(**kwargs)
        self.bind(pos=self.redraw, size=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()
        if not self.subjects:
            return

        with self.canvas:
            Color(*App.get_running_app().hex_color("#FFFFFF"))
            Rectangle(pos=self.pos, size=self.size)

            left = 25
            bottom = 70
            chart_w = max(self.width - 45, 100)
            chart_h = max(self.height - 120, 100)
            gap = chart_w / (len(self.subjects) + 1)
            bar_w = min(52, gap * 0.55)

            Color(*App.get_running_app().hex_color("#6B7280"))
            Line(points=[
                self.x + left, self.y + bottom,
                self.x + left + chart_w, self.y + bottom
            ], width=1.2)

            for i, (name, score) in enumerate(self.subjects.items()):
                x = self.x + left + gap * (i + 0.5)
                y = self.y + bottom
                h = (score / 20.0) * chart_h

                Color(*App.get_running_app().hex_color("#3B82F6"))
                RoundedRectangle(pos=(x-bar_w/2, y), size=(bar_w, h), radius=[6,])

                lab = CoreLabel(text=str(score), font_size=14, bold=True,
                                color=App.get_running_app().hex_color(TEXT))
                lab.refresh()
                Rectangle(texture=lab.texture,
                           pos=(x-lab.texture.size[0]/2, y+h+5),
                           size=lab.texture.size)

                lab2 = CoreLabel(text=name, font_size=12, bold=True,
                                 color=App.get_running_app().hex_color(TEXT))
                lab2.refresh()
                Rectangle(texture=lab2.texture,
                           pos=(x-lab2.texture.size[0]/2, self.y+18),
                           size=lab2.texture.size)


class StudentApp(App):
    title = "دستیار هوشمند دانش‌آموز"

    def build(self):
        # مسیر مناسب برای اندروید و دسکتاپ
        self.file_name = os.path.join(self.user_data_dir, "students.txt")
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        return sm

    def hex_color(self, value):
        value = value.lstrip("#")
        return tuple(int(value[i:i+2], 16)/255 for i in (0, 2, 4)) + (1,)


if __name__ == "__main__":
    StudentApp().run()
