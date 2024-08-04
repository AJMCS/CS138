'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
from vaccine_record import _VaccineRecord_

def main():
    # Test constructor and getters
    record = _VaccineRecord_("John", "Doe", "01/01/1990",
        "Pfizer", "03/15/2021", "City Hospital",
        "Moderna", "04/15/2021", "Community Clinic"
    )

    print("Testing constructor and getters:")
    print(f"First Name: {record.get_first_name()}")
    print(f"Last Name: {record.get_last_name()}")
    print(f"Date of Birth: {record.get_dob()}")
    print(f"Dose 1 Manufacturer: {record.get_d1_manufacturer()}")
    print(f"Dose 1 Date: {record.get_d1_date()}")
    print(f"Dose 1 Location: {record.get_d1_location()}")
    print(f"Dose 2 Manufacturer: {record.get_d2_manufacturer()}")
    print(f"Dose 2 Date: {record.get_d2_date()}")
    print(f"Dose 2 Location: {record.get_d2_location()}")

    # Test setters
    print("\nTesting setters:")
    record.set_first_name("Jane")
    record.set_last_name("Smith")
    record.set_dob("02/15/1985")
    record.set_d1_manifacturer("Johnson & Johnson")
    record.set_d1_date("05/01/2021")
    record.set_d1_location("Pharmacy")
    record.set_d2_manifacturer("Johnson & Johnson")
    record.set_d2_date("06/01/2021")
    record.set_d2_location("Pharmacy")

    # Test __str__ method
    print("\nTesting __str__ method:")
    print(str(record))

    # Test format_date method
    print("\nTesting format_date method:")
    formatted_date = record.format_date(3, 15, 2000)
    print(f"Formatted date: {formatted_date}")

    # Test single-digit month and day
    single_digit_date = record.format_date(3, 5, 2021)
    print(f"Single-digit month and day: {single_digit_date}")

if __name__ == "__main__":
    main()