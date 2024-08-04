from tkinter import * # gui module
from vaccine_record import VaccineRecord

#this method should be called when "Submit"   button is clicked
def process():
  record = VaccineRecord(first_name_e.get(), last_name_e.get(), dob_e.get(), d1_manufacturer_e.get(), d1_batch_e.get(), d1_date_e.get(), d1_location_e.get(), d2_manufacturer_e.get(), d2_batch_e.get(), d2_date_e.get(), d2_location_e.get())

  print(record)
  

#this method should be called when checkbox is ticked/unticked. Have an IF for off, ELSE for on
def checkbox_process():
  if no_dose.get() == 1:
    
    d2_manufacturer_l.grid_remove()
    d2_batch_l.grid_remove()
    d2_date_l.grid_remove()
    d2_location_l.grid_remove()

    d2_manufacturer_e.grid_remove()
    d2_batch_e.grid_remove()
    d2_date_e.grid_remove()
    d2_location_e.grid_remove()

    d2_manufacturer_e.delete(0,100)
    d2_batch_e.delete(0,100)
    d2_date_e.delete(0,100)
    d2_location_e.delete(0,100)
  
  else:
    d2_manufacturer_l.grid(row= 8, column= 0)
    d2_batch_l.grid(row= 9, column= 0)
    d2_date_l.grid(row= 10, column= 0)
    d2_location_l.grid(row= 7, column= 0)

    d2_manufacturer_e.grid(row= 9, column= 1)
    d2_batch_e.grid(row= 10, column= 1)
    d2_date_e.grid(row= 11, column= 1)
    d2_location_e.grid(row= 12, column= 1)

#begin code for GUI 

#__LAYOUT__
window = Tk()
window.title("Vaccine Entry")
window.geometry("800x800")



#__LABELS__
first_name_l = Label(window, text="First Name")
last_name_l = Label(window, text="Last Name")
dob_l = Label(window, text="Date of Birth")

section1_l = Label(window, text="First Dose Information")

d1_manufacturer_l = Label(window, text="Manufacturer")
d1_batch_l = Label(window, text="Batch")
d1_date_l = Label(window, text="Date (mm/dd/yyyy)")
d1_location_l = Label(window, text="Location")

section2_l = Label(window, text="Second Dose Information")

d2_manufacturer_l = Label(window, text="Manufacturer")
d2_batch_l = Label(window, text="Batch")
d2_date_l = Label(window, text="Date (mm/dd/yyyy)")
d2_location_l = Label(window, text="Location")



#__ENTRIES__
first_name_e = Entry(window, bd= 5)
last_name_e = Entry(window, bd= 5)
dob_e = Entry(window, bd= 5)

d1_manufacturer_e = Entry(window, bd= 5)
d1_batch_e = Entry(window, bd= 5)
d1_date_e = Entry(window, bd= 5)
d1_location_e = Entry(window, bd= 5)

d2_manufacturer_e = Entry(window, bd= 5)
d2_batch_e = Entry(window, bd= 5)
d2_date_e = Entry(window, bd= 5)
d2_location_e = Entry(window, bd= 5)



#__BUTTONS__
submit_b = Button(window, text="submit", command=process)
no_dose = IntVar()
check_b = Checkbutton(window, text="No Second Dose", variable=no_dose, onvalue= 1, offvalue= 0, command= checkbox_process)





#__GRID__

#Column 0
first_name_l.grid(row= 0, column= 0)
last_name_l.grid(row= 1, column= 0)
dob_l.grid(row= 2, column= 0)

d1_manufacturer_l.grid(row= 4, column= 0)
d1_batch_l.grid(row= 5, column= 0)
d1_date_l.grid(row= 6, column= 0)
d1_location_l.grid(row= 7, column= 0)

d2_manufacturer_l.grid(row= 9, column= 0)
d2_batch_l.grid(row= 10, column= 0)
d2_date_l.grid(row= 11, column= 0)
d2_location_l.grid(row= 12, column= 0)

#Column 1
first_name_e.grid(row= 0, column= 1)
last_name_e.grid(row= 1, column= 1)
dob_e.grid(row= 2, column= 1)

section1_l.grid(row= 3, column= 1)

d1_manufacturer_e.grid(row= 4, column= 1)
d1_batch_e.grid(row= 5, column= 1)
d1_date_e.grid(row= 6, column= 1)
d1_location_e.grid(row= 7, column= 1)

section2_l.grid(row= 8, column= 1)

d2_manufacturer_e.grid(row= 9, column= 1)
d2_batch_e.grid(row= 10, column= 1)
d2_date_e.grid(row= 11, column= 1)
d2_location_e.grid(row= 12, column= 1)

#Column 2
check_b.grid(row= 8, column= 2)
submit_b.grid(row= 10, column= 2)