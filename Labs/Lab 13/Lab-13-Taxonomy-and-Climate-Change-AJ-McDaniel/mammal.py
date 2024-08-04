# create your Mammal class
class _Mammal_:

  # __init__ method accepts the arguments for the kindom, phylum,and class_type. It initiliazes the data attributes with these values

  def __init__(self):
    self.__domain = "Eukaryota"
    self.__kingdom = "Animalia"
    self.__phylum = "Chordata"
    self.__class_type = "Mammalia"
    self.__order = "order"



  # methods for the mutators/setters for the class's data attributes
  def set_domain(self, domain):
    self.__domain = domain
  def set_kingdom(self, kingdom):
    self.__kingdom = kingdom
  def set_phylum(self, phylum):
    self.__phylum = phylum
  def set_class_type(self, class_type):
    self.__class_type = class_type
  def set_order(self, order):
    self.__order = order

  # methods for the accessors/getters for the class's data attributes
  def get_domain(self):
    return self.__domain
  def get_kingdom(self):
    return self.__kingdom
  def get_phylum(self):
    return self.__phylum
  def get_class_type(self):
    return self.__class_type
  def get_order(self):
    return self.__order

  # method for class string
  def __str__(self):
    return f'''{self.get_domain()}-->{self.get_kingdom()}-->{self.get_phylum()}-->{self.get_class_type()}-->{self.get_order()}'''