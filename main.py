from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivymd.app import MDApp

# Carregando o arquivo KV que descreve a interface do aplicativo
KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 20

    TextInput:
        id: input_number
        hint_text: 'Digite um número'
        input_filter: 'int'
        input_type: 'number'

    Button:
        text: 'Gerar Tabuada'
        on_press: app.generate_tabuada()  # Alterei 'root' para 'app'

    Label:
        id: tabuada_label
        text: 'Tabuada será exibida aqui'
'''

# Classe do aplicativo
class TabuadaApp(App):
    def build(self):
        return Builder.load_string(KV)

    def generate_tabuada(self):
        input_number = self.root.ids.input_number
        tabuada_label = self.root.ids.tabuada_label
        number = int(input_number.text)
        tabuada = ""
        for i in range(1, 11):
            tabuada += f"{number} x {i} = {number * i}\n"
        tabuada_label.text = tabuada

if __name__ == '__main__':
    TabuadaApp().run()
