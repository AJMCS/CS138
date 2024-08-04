from mammal import _Mammal_
from polarbear import _PolarBear_
from snowleopard import _SnowLeopard_

def test_mammal():
    print("Testing Mammal class:")
    mammal = _Mammal_()

    # Test default constructor
    print("\nMammal before changes:")
    print(mammal)

    # Test getters
    print(f"Domain: {mammal.get_domain()}")
    print(f"Kingdom: {mammal.get_kingdom()}")
    print(f"Phylum: {mammal.get_phylum()}")
    print(f"Class: {mammal.get_class_type()}")
    print(f"Order: {mammal.get_order()}")

    # Test setters
    mammal.set_domain("Test Domain")
    mammal.set_kingdom("Test Kingdom")
    mammal.set_phylum("Test Phylum")
    mammal.set_class_type("Test Class")
    mammal.set_order("Test Order")

    # Test __str__
    print("\nMammal after changes:")
    print(mammal)

def test_polar_bear():
    print("\nTesting PolarBear class:")
    polar_bear = _PolarBear_("Poley")
    
    # Test setters
    polar_bear.set_name("Polo")
    polar_bear.set_order("Test Carnivora")
    polar_bear.set_family("Test Ursidae")
    polar_bear.set_genus("Test Ursus")
    polar_bear.set_species("Test Ursus maritimus")
    polar_bear.set_vulnerability("High")
    polar_bear.set_resilience("Low")
    polar_bear.set_status("Vulnerable")

    # Test getters
    print(f"Name: {polar_bear.get_name()}")
    print(f"Order: {polar_bear.get_order()}")
    print(f"Family: {polar_bear.get_family()}")
    print(f"Genus: {polar_bear.get_genus()}")
    print(f"Species: {polar_bear.get_species()}")
    print(f"Vulnerability: {polar_bear.get_vulnerability()}")
    print(f"Resilience: {polar_bear.get_resilience()}")
    print(f"Status: {polar_bear.get_status()}")

    # Test __str__
    print("\nPolar Bear:")
    print(polar_bear)

def test_snow_leopard():
    print("\nTesting SnowLeopard class:")
    snow_leopard = _SnowLeopard_("Leppo")

    # Test setters
    snow_leopard.set_name("Leo")
    snow_leopard.set_order("Carnivora")
    snow_leopard.set_family("Felidae")
    snow_leopard.set_genus("Panthera")
    snow_leopard.set_species("Panthera uncia")
    snow_leopard.set_vulnerability("Medium")
    snow_leopard.set_resilience("Medium")
    snow_leopard.set_status("Vulnerable")

    # Test getters
    print(f"Name: {snow_leopard.get_name()}")
    print(f"Order: {snow_leopard.get_order()}")
    print(f"Family: {snow_leopard.get_family()}")
    print(f"Genus: {snow_leopard.get_genus()}")
    print(f"Species: {snow_leopard.get_species()}")
    print(f"Vulnerability: {snow_leopard.get_vulnerability()}")
    print(f"Resilience: {snow_leopard.get_resilience()}")
    print(f"Status: {snow_leopard.get_status()}")

    # Test __str__
    print("\nSnow Leopard:")
    print(snow_leopard)


def main():
    test_mammal()
    test_polar_bear()
    test_snow_leopard()


if __name__ == "__main__":
    main()