import json


class parser_announcements:
    def __init__(self, path: str):
        self.path = path

    def serialization(self, label: str, txt: str, path_img='priroda-reka-doma-krasnyj.jpg'):
        pass

    def deserialization(self):
        pass


class DataScience:
    def __init__(self):
        self.level_one = dict()
        self.level_two = dict()
        self.level_three = {'active': dict(),
                            'in_check': dict(),
                            'inactive': dict()
                            }
        self.BG = {'level_one': self.level_one,
                   'level_two': self.level_two,
                   'level_three': self.level_three

                   }
        self.id = 0
        self.phone_number = None
        self.ad_id = 0

    def default_registration_data_constructor(self, login: str, password: str, phone_number: str, user_name: str,
                                              location: str, sex: str):
        id = self.get_id()
        self.level_one[login] = {'password': password,
                                 'phone_number': phone_number,
                                 'ID': id
                                 }
        self.level_two[f'{id}'] = {
            'user_data': {'user_name': user_name,
                          'location': location,
                          'sex': sex}
        }

    def identification(self, login: str, password: str):
        if login in self.BG['level_one']:
            if self.BG['level_one'][login]['password'] == password:
                with open('my_personal_data.json', 'w') as f:
                    data = self.BG['level_one'][login]
                    data['login'] = login
                    json.dump(data, f)

        return False

    def default_private_data_constructor(self):
        with open('my_personal_data.json', 'r') as f:
            id = json.load(f)['ID']
        self.level_two[f'{id}'] = {
            'announcement': {'active': dict(),
                             'in_check': dict(),
                             'inactive': dict()}
        }

    def default_ad_builder(self, header: str, description: str, price: str, img_path: list):
        with open('my_personal_data.json', 'r') as f:
            f = json.load(f)
            phone_number = f['phone_number']
            id = f['ID']
            ad_id = self.get_ad_id()
        self.level_three['in_check'][f'{ad_id}'] = {'id': f'{id}',
                                                    'header': header,
                                                    'description': description,
                                                    'price': price,
                                                    'phone_number': phone_number,
                                                    'img_paths': img_path

                                                    }
        self.level_two[f'{id}']['announcement']['in_check'][f'{ad_id}'] = '#time'

    def ad_status_change(self, to_instance: str, ad_id: str, from_instance='in_check'):
        with open('my_personal_data.json', 'r') as f:
            f = json.load(f)
            id = f['ID']
        self.level_three[to_instance][ad_id] = self.level_three[from_instance][ad_id]
        del self.level_three[from_instance][ad_id]
        self.level_two[f'{id}']['announcement'][f'{to_instance}'][f'{ad_id}'] = '#time'
        del self.level_two[f'{id}']['announcement'][f'{from_instance}'][f'{ad_id}']

    def get_id(self):
        self.id += 1
        return str(f'id_{self.id}')

    def get_ad_id(self):
        self.ad_id += 1
        return str(f'ad_id_{self.ad_id}')

# test_bg = DataScience()
#
# test_bg.default_registration_data_constructor('login_1', 'password', '8700')
# test_bg.identification('login_1', 'password')
# test_bg.default_private_data_constructor('a', 'krg', 'm')
#
# test_bg.default_ad_builder('z', 'describe', '100',[])
# test_bg.default_ad_builder('g', 'describe', '100',[])
# test_bg.default_ad_builder('s', 'describe', '100',[])
# test_bg.ad_status_change('active','ad_id_1')
#
# test_bg.default_registration_data_constructor('login_2', 'password_2', '9')
# test_bg.identification('login_2', 'password_2')
# test_bg.default_private_data_constructor('c', 's', 'm')
#
# test_bg.default_ad_builder('s', 'describe', '100',[])
# test_bg.default_ad_builder('s', 'describe', '100',[])
#
# test_bg.default_registration_data_constructor('login_3', 'password_3', '5')
# test_bg.identification('login_3', 'password_3')
# test_bg.default_private_data_constructor('b', 'h', 'm')
#
# test_bg.default_ad_builder('g', 'describe', '100',[])
# test_bg.default_ad_builder('g', 'describe', '100',[])
#
# test_bg.identification('login_1', 'password')
#
# test_bg.default_ad_builder('z', '99999999', '100',[])
#
#
# json_bg = json.dumps(test_bg.BG, indent=4)
#
# print(json_bg)
