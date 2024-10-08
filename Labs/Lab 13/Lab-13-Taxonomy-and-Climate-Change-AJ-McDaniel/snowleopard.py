# import Mammal class
from mammal import _Mammal_


# create your SnowLeopard class that extends from the Mammal class
class _SnowLeopard_(_Mammal_):
    
        
        
    # Call the superclass's __init__ method and pass the requiredarguments. Note that we also have to pass self as an arguments
    def __init__(self, name):
        _Mammal_.__init__(self)
    

    # Initialize the __order, __family, __genius, __species, __vulnerability, __resilience, and__status
        self.__name = name
        self.__order = "Carnivora"
        self.__family = "Felidae"
        self.__genus = "Panthera"
        self.__species = "P. uncia"
        self.__vulnerability = "Susceptible to indirect impacts of climate change, such as habitat encroachment by humans as a result of changing conditions in the region."
        self.__resilience = "High mobility across their large, mountainous range—not bound to a narrow altitude or region."
        self.__status = "Endangered"

  # methods for the mutators/setters for the attributes
    def set_name(self, name):
        self.__name = name
    def set_order(self, order):
        self.__order = order
    def set_family(self, family):
        self.__family = family
    def set_genus(self, genus):
        self.__genus = genus
    def set_species(self, species):
        self.__species = species
    def set_vulnerability(self, vulnerability):
        self.__vulnerability = vulnerability
    def set_resilience(self, resilience):
        self.__resilience = resilience
    def set_status(self, status):
        self.__status = status

  # methods for the accessors/getters for the attributes
    def get_name(self):
        return self.__name
    def get_order(self):
        return self.__order
    def get_family(self):
        return self.__family
    def get_genus(self):
        return self.__genus
    def get_species(self):
        return self.__species
    def get_vulnerability(self):
        return self.__vulnerability
    def get_resilience(self):
        return self.__resilience
    def get_status(self):
        return self.__status

  # method for class string
    def __str__(self):
        return f'''{_Mammal_.__str__(self)}-->{self.get_name()}-->{self.get_order()}-->{self.get_family()}-->{self.get_genus()}-->{self.get_species()}-->{self.get_vulnerability()}-->{self.get_resilience()}-->{self.get_status()}'''