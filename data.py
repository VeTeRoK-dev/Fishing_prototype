class UserInfo():
    surname = ''
    name = ''
    lastname = ''
    mail = ''
    phone = ''


class Data():
    phone = 0
    code = 0
    
    map_lon = 0
    map_lat = 0
    
    search_object = {}
    parse_list = []
    
    request = ''

    input_surname = ''
    input_name = ''
    input_lastname = ''
    input_mail = ''
    input_phone = 0

    number_rule = 0
    number_penalties = 0

    stateMap = 'Street'
    screen_history = []
    parse_list = []
    
    polygon_text = None
    is_polygon = False
    urlToPenalti = ""
    fish_number = 0
    
    map_src = True
    satellite_src = True
    hybrid_src = True

    db = []

    def save_info(self, surname, name, lastname, mail, phone):
        try:
            input_phone = int(phone)
        except:
            pass
        finally:
            input_phone = ''
        self.input_surname = surname
        self.input_name = name
        self.input_lastname = lastname
        self.input_mail = mail
        self.input_phone = input_phone

user_info = UserInfo()
