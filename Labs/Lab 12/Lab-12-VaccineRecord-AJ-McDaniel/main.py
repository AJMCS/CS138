'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
import vaccine_record

def main():
  # Create a new VaccineRecord instance
      record = vaccine_record._VaccineRecord_()

      # Test setters
      record.set_first_name("John")
      record.set_last_name("Doe")
      record.set_dob("01/01/1990")
      record.set_d1_manifacturer("Pfizer")
      record.set_d1_date("03/15/2021")
      record.set_d1_location("City Hospital")
      record.set_d2_manifacturer("Pfizer")
      record.set_d2_date("04/05/2021")
      record.set_d2_location("City Hospital")

      # Test getters
      print("Testing getters:")
      print(f"First Name: {record.get_first_name()}")
      print(f"Last Name: {record.get_last_name()}")
      print(f"Date of Birth: {record.get_dob()}")
      print(f"Dose 1 Manufacturer: {record.get_d1_manufacturer()}")
      print(f"Dose 1 Date: {record.get_d1_date()}")
      print(f"Dose 1 Location: {record.get_d1_location()}")
      print(f"Dose 2 Manufacturer: {record.get_d2_manufacturer()}")
      print(f"Dose 2 Date: {record.get_d2_date()}")
      print(f"Dose 2 Location: {record.get_d2_location()}")

      # Test __str__ method
      print("\nTesting __str__ method:")
      print(str(record))

      # Test format_date method
      print("\nTesting format_date method:")
      formatted_date = record.format_date(3, 15, 2000)
      print(f"Formatted date: {formatted_date}")

if __name__ == "__main__":
      main()