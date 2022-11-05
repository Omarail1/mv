import requests
from faker import Faker
from bs4 import BeautifulSoup

class Checker:
    def __init__(self):
        # manage_files.__init__(self)
        self.set_proxies_r = None
        self.check_index = -1
        self.response = None
        self.responses = []
        self.save_request = False
        self.session = requests.Session()

    def request(self, request_type='', **request_data):
        if (request_type == 'get'):
            try:
                self.response = self.session.get(
                    **request_data, proxies=self.set_proxies_r)
            except:
              pass

        elif (request_type == 'post'):
            try:
                self.response = self.session.post(
                    **request_data, proxies=self.set_proxies_r)
            except:
                pass

        elif (request_type == 'put'):
            try:
                self.response = self.session.put(
                    **request_data, proxies=self.set_proxies_r)
            except:
                pass

        elif (request_type == 'delete'):
            try:
                self.response = self.session.delete(
                    **request_data, proxies=self.set_proxies_r)
            except:
                pass

        elif (request_type == 'options'):
            try:
                self.response = self.session.options(
                    **request_data, proxies=self.set_proxies_r)
            except:
                pass

        self.responses.append(self.response)
        if self.save_request:
            with open('res' + str(len(self.responses)) + '.html', 'w+', encoding="utf-8") as f:
                f.write(self.response.text)
        return self.response

    # def find_between(self, s, first, last):
        # try:
            # start = s.index(first) + len(first)
            # end = s.index(last, start)
            # return s[start:end]
        # except ValueError:
            # return ''

    def find_between(self, first, last):
        try:
            start = self.response.text.index(first)+len(first)
            end = self.response.text.index(last, start)
            return self.response.text[start:end]
        except:
            return ''
            
    # def find_between_req(self, first, last):
        # try:
            # start = self.response.text.index(first) + len(first)
            # end = self.response.text.index(last, start)
            # return self.response.text[start:end]
        # except ValueError:
            # return ''

    def find_html(self, type='', *find_by):
        # print(find_by)
        parser = BeautifulSoup(self.response.text, 'html.parser')
        if (type == 'one'):
            return parser.find(*find_by)
        elif (type == 'all'):
            return parser.find_all(*find_by)

    def find_html_req(self, response, type='', *find_by):
        # print(find_by)
        parser = BeautifulSoup(response, 'html.parser')
        if (type == 'one'):
            return parser.find(*find_by)
        elif (type == 'all'):
            return parser.find_all(*find_by)
    
    def get_user_agent(self):
        return Faker().user_agent()
        
    def data_to_send(self, real_zipcode=False, zipcode=None):
        # print('in data')
        faker = Faker("en_US")
        profile = faker.profile()
        name = profile['name'].split(' ')
        firstName = name[0]
        lastName = name[1]
        data = {
            "first_name": firstName,
            "last_name": lastName,
            'street': faker.street_address(),
            'email': profile['mail'],
            "country": 'United States',
            "phone": faker.msisdn()
        }
        if zipcode == None:
            zipcode = faker.postcode()
        if real_zipcode:
            # print(zipcode)
            place_data = self.get_zipcode_online(zipcode)
            # print(place_data)
        else:
            place_data = {
                'zipcode': zipcode,
                "state": faker.state(),
                "state_shortcut": faker.state_abbr(),
                "city": faker.city(),
            }
        data.update(place_data)
        return data