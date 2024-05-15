import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from datetime import date
import json

import calc_days_elapsed
from calc_days_elapsed import days_percent
from calc_days_elapsed import weeks_since_birth
from calc_days_elapsed import calc_all_weeks


def open_file(file= "config.json"):
  """ 
  opens config and returns contents as string
  """
  with open(file, "r") as ret:
    return json.load(ret)
  
config = open_file()   

class MainMenu(Screen):
    pass
class ProgBarMenu(Screen):
    pass
class ProgressOfCurrentYear(Screen):
    pocy_bar = ObjectProperty(None)
    pocy_text = ObjectProperty(None)

    def procent_of_year(self):
        ret = float(days_percent())
        return ret
    
    def procent_text(self):
        ret = f"this much: {days_percent()} %"
        return ret
    
class ProgressOfLife(Screen):
    pol_bar = ObjectProperty(None)
    pol_text = ObjectProperty(None)

    def percent_of_life(slef):
        bd = int(config["ProgressOfLife"]["bday"])
        bm = int(config["ProgressOfLife"]["bmonth"])
        by= int(config["ProgressOfLife"]["byear"])
        ls = int(config["ProgressOfLife"]["lifespan"])
        ret = (weeks_since_birth(bd, bm, by) *100 ) / calc_all_weeks(ls)
        return float("{:.2f}".format(ret))
    
    def percent_ol_text(self):
        return f"this much have passed {self.percent_of_life()}"
    
class CustomizeLife(Screen):
    cl_text_ls = ObjectProperty(None)
    cl_text_bd = ObjectProperty(None)
    cl_text_bm = ObjectProperty(None)
    cl_text_by = ObjectProperty(None)
    cl_input_ls = ObjectProperty(None)
    cl_input_bd = ObjectProperty(None)
    cl_input_bm = ObjectProperty(None)
    cl_input_by = ObjectProperty(None)


    def get_lifespan(self):
        return config["ProgressOfLife"]["lifespan"]
    def get_bday(self):
        return config["ProgressOfLife"]["bday"]
    def get_bmonth(self):
        return config["ProgressOfLife"]["bmonth"]
    def get_byear(self):
        return config["ProgressOfLife"]["byear"]
    


    def print_lifespan(self):
        return f"Lifespan: {str(self.get_lifespan())}"    
    def print_bday(self):
        return f"Birth date: {str(self.get_bday())}"    
    def print_bmonth(self):
        return f"Birth month: {str(self.get_bmonth())}"    
    def print_byear(self):
        return f"Brith year: {str(self.get_byear())}"
    

    def update_config(self):
        if self.set_lifespan() and self.set_bday() and self.set_bmonth() and self.set_byear():
            try:
                with open("config.json","w") as file:
                    config["ProgressOfLife"]["lifespan"] = self.cl_input_ls
                    config["ProgressOfLife"]["bday"] = self.cl_input_bd
                    config["ProgressOfLife"]["bmonth"]= self.cl_input_bm
                    config["ProgressOfLife"]["byear"]= self.cl_input_by
                    json.dump(config, file)
            except:
                self.error_popup

    def set_lifespan(self):
        x = self.cl_input_ls
        if type(x) is int and x>0  and x<150:
            return True
        else:
            return False

    def set_bday(self):
        x = self.cl_input_bd
        if type(x) is int and x <31:
            return True
        else:
            return  False

    def set_bmonth(self):
        x = self.cl_input_bm
        if type(x) is int and x < 12:
            return True
        else:
            return False  

    def set_byear(self):
        x = self.cl_input_by
        if type(x) is int:
            return True
        else:
            return False
    
    def error_popup(self):
        pop = Popup(title="Invalid input",
                    content=Label(text="Please enter valid information."),
                    size_hint=(None, None), size=(400, 400))
        pop.open()
    
                    

class WindowMenager(ScreenManager):
    pass

kv = Builder.load_file("progbar.kv")   
sm = WindowMenager()
 
class progbarApp(App):
    def build(self):
        return kv




if __name__ == "__main__":
    progbarApp().run()

