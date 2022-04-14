import json
import re

from kivy.utils import rgba
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from json_announcement import DataScience
from akivymd.uix.bottomnavigation2 import Button_Item
from kivy import platform
from kivy.animation import Animation
from kivy.core.window import Window, android
from kivy.graphics import Color
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, BooleanProperty, ListProperty, Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager, ShaderTransition
from kivy.uix.textinput import TextInput
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
import kivymd_extensions.akivymd
from kivymd_extensions.akivymd.uix.bottomnavigation2 import Button_Item
from kivymd_extensions.akivymd.uix.silverappbar import AKSilverAppbar

json_bg = DataScience()


class InternalSlider(ScreenManager):

    def __init__(self, **kwargs):
        super(InternalSlider, self).__init__(**kwargs)


class Second(MDScreen):
    def __init__(self, **kwargs):
        super(Second, self).__init__(**kwargs)
        self.name = 'btn'


class own_announcement(MDScreen):
    def __init__(self, **kwargs):
        super(own_announcement, self).__init__(**kwargs)
        self.name = 'own_announcement'


class own(RecycleView):
    def __init__(self, **kwargs):
        super(own, self).__init__(**kwargs)


class read(MDScreen):
    def __init__(self, **kwargs):
        super(read, self).__init__(**kwargs)


class Block(Screen):
    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.name = 'menu'


class DataAnnouncement:
    def __init__(self):

        ############################## скрыто вызывается 2 раза чтение БД
        try:
            self.data = self.deseralization()
        except:
            self.data = []

        try:
            self.own_data = self.deseralization_id()
        except:
            self.own_data = []
        self.list_of_path_img = list()  # не используется
        # self.none_png = "img/None.png"
        self.qounter = 5

    def deseralization(self):

        return [{'viewclass': 'Announcement', 'img': json_bg.BG["level_three"]["in_check"][f"{i}"]["img_paths"][0],
                 'header': json_bg.BG["level_three"]["in_check"][f"{i}"]["header"],'price': json_bg.BG["level_three"]["in_check"][i]["price"],
                 'ad_id': i, 'personal_id': json_bg.BG["level_three"]["in_check"][f"{i}"]["id"],
                 'description': json_bg.BG["level_three"]["in_check"][f"{i}"]["description"], "callback": lambda x: x}
                for i in json_bg.BG["level_three"]["in_check"]]

    def deseralization_id(self):
        with open('my_personal_data.json', 'r') as f:
            f = json.load(f)

            id = f['ID']
        L = list()
        for j in json_bg.BG["level_two"][id]['announcement']["in_check"]:
            L.append({'viewclass': 'Announcement', 'img': json_bg.BG["level_three"]["in_check"][j]["img_paths"][0],
                      'header': json_bg.BG["level_three"]["in_check"][j]["header"],'price': json_bg.BG["level_three"]["in_check"][j]["price"],
                      'ad_id': j, 'personal_id': json_bg.BG["level_three"]["in_check"][f"{j}"]["id"],
                      'description': json_bg.BG["level_three"]["in_check"][j]["description"], "callback": lambda x: x})

        return L

    def save_announcement(self, header: str, description: str, price: str, img_path: list):
        json_bg.default_ad_builder(header, description, price, img_path)

        print(json.dumps(json_bg.BG, indent=4))
        self.clear_information()

    def append_img_path(self, path):
        if len(self.list_of_path_img) < 6:
            self.list_of_path_img.append(path)
        else:
            self.list_of_path_img[-1] = path

    def clear_information(self):
        self.list_of_path_img.clear()
        self.qounter = 5

    def PRINT(self):
        print(json.dumps(json_bg.BG, indent=4))


class Announcement(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class On_active_button(Button_Item):
    selected_item = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FloatInput(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)


class Definition(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def clear_js(self):
        with open('BG.json','w') as f:
            f.write('')

class Five(MDBoxLayout, Screen):
    COUNTER = NumericProperty(1)
    index_1 = NumericProperty(1)
    index_2 = NumericProperty(2)
    index_3 = NumericProperty(3)
    index_4 = NumericProperty(4)
    index_5 = NumericProperty(5)

    def __init__(self, **kwargs):
        super(Five, self).__init__(**kwargs)

    def tr(self, index):
        if index >= self.COUNTER:
            self.COUNTER = index
            return 'left'
        else:
            self.COUNTER = index
            return 'right'


class General(ScreenManager):
    def __init__(self, **kwargs):
        super(General, self).__init__(**kwargs)


class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Ego(Screen, DataAnnouncement):
    def __init__(self, **kwargs):
        super(Ego, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def file_manager_open(self):
        self.file_manager.show('\\')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.parent.parent.children[-1].current = 'constructor_announcement'
        self.exit_manager()
        img = path.split('\\')[-1].split('.')[-1]
        if img.lower() in ('png', 'jpeg', 'jpg'):
            toast(path)
            self.append_img_path(path)
            self.parent.children[0].ids.card.children[self.qounter].source = path
            if self.qounter > 0:
                self.qounter -= 1
            # print(self.list_of_path_img)       Есть списком\\\

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()
        self.parent.parent.children[-1].current = 'constructor_announcement'

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back_constructor_announcement()

        return True


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class MainApp(MDApp, DataAnnouncement):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        global general_menu
        general_menu = General()

    def build(self):

        # self.theme_cls.primary_palette = 'Gray'
        # self.theme_cls.theme_style='Light'
        general_menu.add_widget(Builder.load_file("splashScreen.kv"))

        general_menu.add_widget(Builder.load_file("login.kv"))
        general_menu.add_widget(Builder.load_file("signup.kv"))
        general_menu.add_widget(Builder.load_file("initialize.kv"))

        general_menu.add_widget(Five())
        general_menu.add_widget(Definition())

        return general_menu

    def back_constructor_announcement(self):
        self.root.children[-1].children[-1].children[-1].manager.transition.direction = 'right'
        self.root.children[-1].children[-1].current = 'constructor_announcement'

    def on_touch(self, instance):
        pass

    def reading(self, instance):
        try:
            self.root.children[-1].children[-1].ids.read.personal_id = instance.personal_id
            self.root.children[-1].children[-1].ids.read.header = instance.header
            self.root.children[-1].children[-1].ids.read.description = instance.description
            self.root.children[-1].children[-1].ids.read.ad_id = instance.ad_id
            list_of_path = json_bg.BG['level_three']['in_check'][f'{instance.ad_id}']['img_paths']
            self.root.children[-1].children[-1].ids.read.source_1 = list_of_path[0]
            self.root.children[-1].children[-1].ids.read.price = instance.price
            self.root.children[-1].children[-1].ids.read.source_2 = list_of_path[1]
            self.root.children[-1].children[-1].ids.read.source_3 = list_of_path[2]
            self.root.children[-1].children[-1].ids.read.source_4 = list_of_path[3]
            self.root.children[-1].children[-1].ids.read.source_5 = list_of_path[4]
            self.root.children[-1].children[-1].ids.read.source_6 = list_of_path[5]
        except:
            pass

    def on_start(self):
        Clock.schedule_once(self.change_screen_after_init, 7)

    def change_screen_after_init(self, dt):
        try:

            with open('my_personal_data.json', 'r') as f:
                f = json.load(f)
                login = f['login']
                password = f['password']
            if json_bg.identification(login, password):
                self.root.current = 'Five'
            else:

                self.root.current = 'login'

        except:
            self.root.current = 'login'

    def rv_constructor_clock(self, instance, text=''):
        if instance == self.root.children[-1].children[-1].children[-1].children[-1].children[-2]:
            Clock.schedule_once(self.rv_constructor, .7)
        elif instance == self.root.children[-1].children[-1].children[-1].children[-1].children[
            -1].ids.search_string.ids.search_field_button:
            self.search(text)

    def search(self, text):

        l = list()
        if text != '':
            for i in json_bg.BG['level_three']['in_check']:

                if text.lower() in json_bg.BG['level_three']['in_check'][i]['header'].lower():
                    l.append({'viewclass': 'Announcement',
                              'img': json_bg.BG["level_three"]["in_check"][f"{i}"]["img_paths"][0],
                              'header': json_bg.BG["level_three"]["in_check"][f"{i}"]["header"],'price': json_bg.BG["level_three"]["in_check"][i]["price"],
                              'ad_id': i, 'personal_id': json_bg.BG["level_three"]["in_check"][f"{i}"]["id"],
                              'description': json_bg.BG["level_three"]["in_check"][f"{i}"]["description"],
                              "callback": lambda x: x})
            self.root.children[-1].children[-1].children[-1].children[-1].remove_widget(
                self.root.children[-1].children[-1].children[-1].children[-1].children[-2])
            self.data = l
            self.root.children[-1].children[-1].children[-1].children[-1].add_widget(RV())

    def rv_constructor(self, instance):
        self.root.children[-1].children[-1].children[-1].children[-1].remove_widget(
            self.root.children[-1].children[-1].children[-1].children[-1].children[-2])
        self.data = self.deseralization()
        self.root.children[-1].children[-1].children[-1].children[-1].add_widget(RV())

    ###############################################################
    def own_rv_constructor_timer(self, instance):
        Clock.schedule_once(self.own_rv_constructor, .7)

    def own_rv_constructor(self, instance):
        print(self.root.children[-1].children[-1].children[-1].children[-1])
        self.root.children[-1].children[-1].children[-1].children[-1].remove_widget(
            self.root.children[-1].children[-1].children[-1].children[-1].children[-2])
        self.own_data = self.deseralization_id()
        self.root.children[-1].children[-1].children[-1].children[-1].add_widget(own())
        print(self.root.children[-1].children[-1].children[-1].children[-1])

    def verificare(self):
        if self.root.children[0].ids.login.text != '' and self.root.children[0].ids.password.ids.text_field.text != '':
            try:
                if json_bg.identification(self.root.children[0].ids.login.text,
                                          self.root.children[0].ids.password.ids.text_field.text):
                    self.root.current = 'Five'
                    self.root.transition.direction = 'left'
                else:
                    toast('Логин или пароль введены неверно')
            except:
                toast('Логин или пароль введены неверно')

    def previous_slide(self, instance):
        self.root.children[0].ids.slide.load_previous()

    def check_complete_slide_information(self, instance):
        color = [255 / 255, 15 / 255, 0 / 255, 1]
        icon = 'alert-decagram'
        bool_value = True
        self.root.children[0].ids.registration.disabled = bool_value
        self.root.children[0].ids.registration.md_bg_color = rgba(178, 178, 178, 78 / 255)

        if instance == self.root.children[0].ids.slide_2:
            if self.root.children[0].ids.first_name.text != '' and self.root.children[0].ids.last_name.text != '':
                color = [0 / 255, 207 / 255, 255 / 255, 1]
                icon = 'check-decagram'
            self.root.children[0].ids.progress_1.value = 100
            self.root.children[0].ids.progress_1.color = color
            self.root.children[0].ids.icon_1.text_color = color
            self.root.children[0].ids.Name.text_color = color
            self.root.children[0].ids.icon_1.icon = icon

        if instance == self.root.children[0].ids.slide_3:
            if self.root.children[0].ids.login.text != '' and self.root.children[
                0].ids.password.ids.text_field.text != '' and self.root.children[0].ids.number.text != '' and \
                    self.root.children[0].ids.first_name.text != '' and self.root.children[0].ids.last_name.text != '':
                color = [0 / 255, 207 / 255, 255 / 255, 1]
                icon = 'check-decagram'
                bool_value = False
                self.root.children[0].ids.registration.disabled = bool_value
                self.root.children[0].ids.registration.md_bg_color = rgba(0, 207, 255, 255)
            self.root.children[0].ids.progress_2.value = 100
            self.root.children[0].ids.progress_2.color = color
            self.root.children[0].ids.icon_2.text_color = color
            self.root.children[0].ids.Contact.text_color = color
            self.root.children[0].ids.icon_2.icon = icon

    def signup(self):
        login = self.root.children[0].ids.login.text
        password = self.root.children[0].ids.password.ids.text_field.text
        number = self.root.children[0].ids.number.text
        sex = self.root.children[0].ids.sex.text
        location = self.root.children[0].ids.location.text
        user_name = f'{self.root.children[0].ids.first_name.text} {self.root.children[0].ids.last_name.text}'
        json_bg.default_registration_data_constructor(login, password, number, user_name, location, sex)

    def next_slide(self, instance):
        self.root.children[0].ids.slide.load_next(mode='next')

    def clear_text_fields_in_signup(self):

        self.root.children[0].ids.first_name.text = ''
        self.root.children[0].ids.login.text = ''
        self.root.children[0].ids.password.ids.text_field.text = ''
        self.root.children[0].ids.number.text = ''
        self.root.children[0].ids.sex.text = ''
        self.root.children[0].ids.location.text = ''
        self.root.children[0].ids.last_name.text = ''

        self.root.children[0].ids.progress_1.value = 0
        self.root.children[0].ids.icon_1.text_color = 0, 0, 0, 1
        self.root.children[0].ids.Name.text_color = 0, 0, 0, 1
        self.root.children[0].ids.icon_1.icon = "numeric-1-circle"

        self.root.children[0].ids.registration.disabled = True
        self.root.children[0].ids.registration.md_bg_color = [178 / 255, 178 / 255, 178 / 255, .3]
        self.root.children[0].ids.progress_2.value = 0
        self.root.children[0].ids.icon_2.text_color = 0, 0, 0, 1
        self.root.children[0].ids.Contact.text_color = 0, 0, 0, 1
        self.root.children[0].ids.icon_2.icon = "numeric-2-circle"


if __name__ == '__main__':
    MainApp().run()

# android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
# if platform == 'android':
#    from android.permissions import request_permissions, Permission
#    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
