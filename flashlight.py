from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import flash

class FlashlightLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FlashlightLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.is_on = False
        
        # Label to show status
        self.status_label = Label(text='Flashlight is OFF')
        self.add_widget(self.status_label)
        
        # Button to toggle
        self.toggle_btn = Button(text='Turn ON')
        self.toggle_btn.bind(on_press=self.toggle_flashlight)
        self.add_widget(self.toggle_btn)

    def toggle_flashlight(self, instance):
        if not self.is_on:
            flash.on()
            self.status_label.text = 'Flashlight is ON'
            self.toggle_btn.text = 'Turn OFF'
            self.is_on = True
        else:
            flash.off()
            self.status_label.text = 'Flashlight is OFF'
            self.toggle_btn.text = 'Turn ON'
            self.is_on = False

class FlashlightApp(App):
    def build(self):
        return FlashlightLayout()

if __name__ == '__main__':
    FlashlightApp().run()