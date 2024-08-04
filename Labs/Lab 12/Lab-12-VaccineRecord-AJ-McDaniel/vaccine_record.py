# The VaccineRecord encapsulates the COVID-19 vaccine data (doses 1 and 2) for a person.
'''
VaccineRecord
------------------------------
- first_name : string
- last_name : string
- dob : string
- d1_manufacturer : string
- d1_batch : string
- d1_date : string
- d1_location : string
- d2_manufacturer : string
- d2_batch : string
- d2_date : string
- d2_location : string
------------------------------
+ format_date : string
------------------------------
 
'''

class _VaccineRecord_:
    def __init__(self, first_name, last_name, dob, d1_manufacturer, d1_date, d1_location, d2_manufacturer, d2_date, d2_location):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__d1_manufacturer = d1_manufacturer
        self.__d1_date = d1_date
        self.__d1_location = d1_location
        self.__d2_manufacturer = d2_manufacturer
        self.__d2_date = d2_date
        self.__d2_location = d2_location

    #toString
    def __str__(self):
        return f'''First Name: {self.get_first_name()}
Last Name: {self.get_last_name()}
Date of Birth: {self.get_dob()}
Dose 1 Manufacturer: {self.get_d1_manufacturer()}
Dose 1 Date: {self.get_d1_date()}
Dose 1 Location: {self.get_d1_location()}
Dose 2 Manufacturer: {self.get_d2_manufacturer()}
Dose 2 Date: {self.get_d2_date()}
Dose 2 Location: {self.get_d2_location()}'''

    #Getters
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_dob(self):
        return self.__dob
    def get_d1_manufacturer(self):
        return self.__d1_manufacturer
    def get_d1_date(self):
        return self.__d1_date
    def get_d1_location(self):
        return self.__d1_location
    def get_d2_manufacturer(self):
        return self.__d2_manufacturer
    def get_d2_date(self):
        return self.__d2_date
    def get_d2_location(self):
        return self.__d2_location

    #Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_dob(self, dob):
        self.__dob = dob
    def set_d1_manifacturer(self, d1_manufacturer):
        self.__d1_manufacturer = d1_manufacturer
    def set_d1_date(self, d1_date):
        self.__d1_date = d1_date
    def set_d1_location(self, d1_location):
        self.__d1_location = d1_location
    def set_d2_manifacturer(self, d2_manufacturer):
        self.__d2_manufacturer = d2_manufacturer
    def set_d2_date(self, d2_date):
        self.__d2_date = d2_date
    def set_d2_location(self, d2_location):
        self.__d2_location = d2_location

    #Method
    def format_date(self, month, day, year):
        
        day = str(day).rjust(2, '0')
        month = str(month).rjust(2, '0')
        year = str(year).ljust(4, '0')
        
        return month + "/" + day + "/" + year