# import Mammal class
from mammal import _Mammal_


# create your PolarBear class that extends from the Mammal class


class _PolarBear_(_Mammal_):
    
    # Call the superclass's __init__ method and pass the required arguments. Note that we also have to pass self as an argument
    def __init__(self, name):
        _Mammal_.__init__(self)
    

    # Initialize the __order, __family, __genius, __species, __vulnerability, __resilience, and __status
        self.__name = name
        self.order = "Carnivora"
        self.__family = "Ursidae"
        self.__genus = "Ursus"
        self.__species = "U. maritimus"
        self.__vulnerability = "Habitat specialists, rely almost entirely on the sea-ice environment."
        self.__resilience = "Opportunistic eaters, prefer seals, but will feed on whale carcasses and even hunt walrus and beluga. Will prey on land animals when necessary."
        self.__status = "Vulnerable"
 
    
  # methods for the mutators/setters for the attributes
    def set_name(self, name):
        self.name = name
    def set_order(self, order):
        self.order = order
    def set_family(self, family):
        self.family = family
    def set_genus(self, genus):
        self.genus = genus
    def set_species(self, species):
        self.species = species
    def set_vulnerability(self, vulnerability):
        self.vulnerability = vulnerability
    def set_resilience(self, resilience):
        self.__resilience = resilience
    def set_status(self, status):
        self.__status = status

  # methods for the accessors/getters for the attributes
    def get_name(self):
        return self.name
    def get_order(self):
        return self.order
    def get_family(self):
        return self.family
    def get_genus(self):
        return self.genus
    def get_species(self):
        return self.species
    def get_vulnerability(self):
        return self.vulnerability
    def get_resilience(self):
        return self.__resilience
    def get_status(self):
        return self.__status


  # method for class string
    def __str__(self):
        return f'''{_Mammal_.__str__(self)}-->{self.get_name()}-->{self.get_order()}-->{self.get_family()}-->{self.get_genus()}-->{self.get_species()}-->{self.get_vulnerability()}-->{self.get_resilience()}-->{self.get_status()}'''