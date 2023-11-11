# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# N-Queens Launcher
# ---
import kivy
kivy.require('2.2.0')
from kivy import App
from config import settings
from kivy.uix.screenmanager import ScreenManager, WipeTransition
import scripts.nqueen as nqueen
class App(App):
    def build(self):
        self.title = settings.VersionInfo.get_title()
        self.icon = "assets/logo.png"
        self.screen_manager = ScreenManager(transition = WipeTransition())

        for screen in []:
            self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__ == '__main__':  
    main = App()
    main.run()