from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.filechooser import FileChooserListView

class MainPage(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        # Створення кнопок для переходу на інші екрани
        btn1 = Button(text='First(CheckBox + TexInput) (Галочка + Введення тексту)')
        btn1.on_press = self.next1
        btn2 = Button(text='Second блок(Label + Image)(рандом фото і текст)')
        btn2.on_press = self.next2
        btn3 = Button(text= 'Third блок(ColorPicker +ToggleButton) (палітра кольрів + перемикач )')
        btn3.on_press = self.next3
        btn4 = Button(text='Fourth блок(ProgressBar + FileChoose) (Смуга прогресу + обирач файлів )')
        btn4.on_press = self.next4

        # Створення головного вікна з кнопками
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn2)  # Змінено: Обміняно btn1 з btn2
        layout.add_widget(btn3)  # Змінено: Обміняно btn2 з btn3
        layout.add_widget(btn4)  # Змінено: Обміняно btn3 з btn4
        layout.add_widget(btn1)  # Змінено: Обміняно btn4 з btn1

        self.add_widget(layout)

    def next1(self):
        # Перехід на екран з CheckBox і TextInput
        self.manager.transition.direction = "up"
        one_screen = ButtonOneScreen()
        one_screen.on_return = self.return_to_main
        self.manager.add_widget(one_screen)
        self.manager.current = "subscreen"

    def next2(self):
        # Перехід на екран з Label і Image
        self.manager.transition.direction = "up"
        two_screen = ButtonTwoScreen()
        two_screen.on_return = self.return_to_main
        self.manager.add_widget(two_screen)
        self.manager.current = "subscreen"

    def next3(self):
        # Перехід на екран з ColorPicker і ToggleButton
        self.manager.transition.direction = "up"
        third_screen = ButtonThirdScreen()
        third_screen.on_return = self.return_to_main
        self.manager.add_widget(third_screen)
        self.manager.current = "subscreen"
        
    def next4(self):
        # Перехід на екран з ProgressBar і FileChooser
        self.manager.transition.direction = "up"
        four_screen = ButtonFourScreen()
        four_screen.on_return = self.return_to_main
        self.manager.add_widget(four_screen)
        self.manager.current = "subscreen"

    def return_to_main(self):
        # Повернення до головного екрану
        self.manager.remove_widget(self.manager.current_screen)
        self.manager.current = "first"

class ButtonOneScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору(головного меню)')
        btn_back.on_press = self.go_back
        tex_input = TextInput(text = "Введіть бажаний текс:?")
        cb1 = CheckBox()
        cb2 = CheckBox()

        # Створення екрану з CheckBox, TextInput і кнопкою для повернення
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(cb1)
        layout.add_widget(cb2)
        layout.add_widget(tex_input) 
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
            
class ButtonTwoScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text= "Вернутися до вибору (головного меню)")
        btn_back.on_press = self.go_back
        label = Label(text="Рандом текст")
        self.button = Button()
        self.button.background_normal = "images/image.png"

        # Створення екрану з Label, Image і кнопкою для повернення
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(label)
        layout.add_widget(btn_back)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()

class ButtonThirdScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору (головного меню)')
        btn_back.on_press = self.go_back
        color_picker = ColorPicker()
        toggle_button = ToggleButton(text='ToggleButton (Перемикач): Дозволяє вибирати між двома станами (увімкнено/вимкнено)')
        
        # Створення екрану з ColorPicker, ToggleButton і кнопкою для повернення
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(toggle_button)
        layout.add_widget(btn_back) 
        layout.add_widget(color_picker)

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
    
class ButtonFourScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Вернутися до вибору (головного меню)')
        btn_back.on_press = self.go_back
        progress_bar = ProgressBar(max=100)
        progress_bar.value = 50   #смуга прогресу, тут потрібно ввести цифру від 0 до 100, щоб виміряти свій прогресс
        file_chooser = FileChooserListView()
        def selected(file_chooser, selection):
            print("Selected:", selection)
        file_chooser.bind(selection=selected)

        # Створення екрану з ProgressBar, FileChooser і кнопкою для повернення
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(file_chooser)
        layout.add_widget(progress_bar)
        layout.add_widget(btn_back)

        self.add_widget(layout)
        
    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
       
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage())
        return sm

if __name__ == '__main__':
    MyApp().run()
