import json
import re

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


class Block(Screen):
    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.name = 'menu'


class DataAnnouncement:
    # list_dicts_of_info=ListProperty([{'text': ''}])
    def __init__(self):

        self.data = [
            {'viewclass': 'Announcement', 'img': '', 'text': f'{i}', "callback": lambda x: x}
            for i in range(5)]
        self.list_of_path_img = list()
        self.none_png = "img/None.png"

    def save_announcement(self, header: str, description: str, price: str):
        json_bg.default_ad_builder(header, description, price, self.list_of_path_img)
        print(json.dumps(json_bg.BG, indent=4))
        self.clear_information()

    def append_img_path(self, path):
        if len(self.list_of_path_img) < 6:
            self.list_of_path_img.append(path)
        else:
            self.list_of_path_img[-1] = path

    def clear_information(self):
        self.list_of_path_img.clear()

    def PRINT(self):
        print(json.dumps(json_bg.BG, indent=4))


BG = DataAnnouncement()


class Announcement(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class On_active_button(Button_Item):
    selected_item = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def on_touch_down(self, touch):


#
#    if self.collide_point(touch.x, touch.y):
#        for item in self.parent.children:
#            if item.selected_item:
#                item.selected_item = False
#        self.selected_item = True
#    print('g')
#    return super().on_touch_down(touch)


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


class Ego(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
            BG.append_img_path(path)

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

        global general
        general = General()
        self.FACE_CONTROL = False

    def build(self):
        # self.theme_cls.primary_palette = 'Red'
        # self.theme_cls.theme_style='Dark'
        general.add_widget(Builder.load_file("splashScreen.kv"))
        general.add_widget(Builder.load_file("login.kv"))
        general.add_widget(Builder.load_file("signup.kv"))
        general.add_widget(Builder.load_file("initialize.kv"))

        general.add_widget(Five())
        general.add_widget(Definition())

        return general

    def back_constructor_announcement(self):
        self.root.children[-1].children[-1].children[-1].manager.transition.direction = 'right'
        self.root.children[-1].children[-1].current = 'constructor_announcement'

    def on_touch(self, instance):
        pass

    def on_start(self):
        Clock.schedule_once(self.change_screen_to_login, 7)
    def change_screen_to_login(self, dt):
        self.root.current = 'login'
    def change_screen_to_Five(self, dt):
        self.root.current = 'Five'

    def rv_constructor(self, instance):
        self.root.children[-1].children[-1].children[-1].children[-1].remove_widget(
            self.root.children[-1].children[-1].children[-1].children[-1].children[-2])
        self.data = [{}]
        self.root.children[-1].children[-1].children[-1].children[-1].add_widget(RV())

    def previous_slide(self, instance):
        self.root.children[0].ids.slide.load_previous()

    def check_complete_slide_information(self, instance):
        color = [255 / 255, 15 / 255, 0 / 255, 1]
        btn_color = [178 / 255, 178 / 255, 178 / 255, .3]
        icon = 'alert-decagram'
        bool_value=True
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
                0].ids.password.ids.text_field.text != '' and self.root.children[0].ids.number.text != '':
                color = [0 / 255, 207 / 255, 255 / 255, 1]
                icon = 'check-decagram'
                bool_value=False
                btn_color=(60/255,136/255,123/255,.7)
            self.root.children[0].ids.registration.disabled=bool_value
            self.root.children[0].ids.registration.md_bg_color = btn_color
            self.root.children[0].ids.progress_2.value = 100
            self.root.children[0].ids.progress_2.color = color
            self.root.children[0].ids.icon_2.text_color = color
            self.root.children[0].ids.Contact.text_color = color
            self.root.children[0].ids.icon_2.icon = icon

    def signup(self):
        login = self.root.children[0].ids.login.text
        password=self.root.children[0].ids.password.ids.text_field.text
        number = self.root.children[0].ids.number.text
        sex= self.root.children[0].ids.sex.text
        location= self.root.children[0].ids.location.text
        user_name=f'{self.root.children[0].ids.first_name.text} {self.root.children[0].ids.last_name.text}'
        json_bg.default_registration_data_constructor(login,password,number,user_name,location,sex)

    def next_slide(self, instance):
        self.root.children[0].ids.slide.load_next(mode='next')


if __name__ == '__main__':
    MainApp().run()

# android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
# if platform == 'android':
#    from android.permissions import request_permissions, Permission
#    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
