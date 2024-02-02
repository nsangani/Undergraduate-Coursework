
# Neel Sangani
# INFO-B201 - Midterm

#----------------------------------------------------------------------------------------Excercise 1----------------------------------------------------------------------

import csv
import pickle

filename = 'XVIRUS.csv'

def create_dict(filename):
    """Takes the csv file and copies the info to dmxvirus.db file
        where keys are the first column and the value is a dictionary
        where each key is the column header and the value is the row column value.

    Inputs:
    filename: string (input filename)

    Output:
    dict: dictionary
    """
    reader = csv.DictReader(open(filename))
    i = 0
    data_dict = {}
    for row in reader:
        data_dict[str(i)] = pickle.dumps(row)
        i += 1
    return data_dict

data_dict = create_dict('XVIRUS.csv')

import dbm

db = dbm.open('dmxvirus.db', 'c')
values = data_dict.keys()
for i in values:
    db[i] = data_dict[i]
db.close()

#-------------------------------------------------------------------------------------------Exercise 2--------------------------------------------------------------------------

def overall_attack():
    """Calculates the overall attack rate of XVIRUS for the population, and prints the attack rate.

    Outputs:
    string: Overall Attack Rate
    """
    population = 981  # given
    db = dbm.dumb.open('dmxvirus.db', 'r')
    i = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        if 'XVIRUS' in g:
            if '1/1/2030' not in d:
                i += 1
    result = i / population * 100
    db.close()
    return f'Overall Attack Rate: {result:.2f}%'

print(overall_attack())
print('\n')

#----------------------------------------------------------------------------Exercise 3------------------------------------------------------------------------------------

def secondary_attack():
    """Calculate the secondary attack rate of XVIRUS for the population, and prints it.

    Outputs:
    string: Secondary Attack Rate
    """
    total_contacts = 200  # given
    db = dbm.dumb.open('dmxvirus.db', 'r')
    i = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        if 'XVIRUS' in g:
            if '1/1/2030' not in d:
                i += 1
    result = i / total_contacts
    db.close()
    return f'Secondary Attack Rate: {result:.2f}'

print(secondary_attack())
print('\n')

#--------------------------------------------------------------------------------Exercise 4-------------------------------------------------------------------------------------

def death_rate():
    """Calculates how many people died from XVIRUS and
        calculates the case fatality rate (per 100,000) for XVIRUS.

    Outputs:
    string: Death Rate
    """
    db = dbm.dumb.open('dmxvirus.db', 'r')
    i = 0
    xvirus_patients = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        if 'XVIRUS' in g:
            xvirus_patients += 1
            if f != 'None':
                i += 1
    result = i / xvirus_patients * 100000
    db.close()
    return f'People died from XVIRUS: {result:.2f} per 100,000 patients'

print(death_rate())
print('\n')

#------------------------------------------------------------------------------------Exercise 5-----------------------------------------------------------------------------------

def ratio(a, b):
    """Calculates ratios
        Ex: input (210, 199) output '1.055: 1'.
    
    Inputs:
    a: int
    b: int

    Output:
    string: Ratio
    """
    c = round(a / b, 2)
    ratio_str = f'{c:.3f}:1'
    return ratio_str

def gender_ratio():
    """Calculate the ratio between male patients and female patients for XVIRUS.

    Outputs:
    string: Gender Ratio
    """
    db = dbm.dumb.open('dmxvirus.db', 'r')
    male = 0
    female = 0
    xvirus_patients = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        if 'XVIRUS' in g:
            if 'M' in c:
                male += 1
            if 'F' in c:
                female += 1
    result = ratio(male, female)
    db.close()
    return f'{result} is the ratio between male patients and female patients for XVIRUS'

print(gender_ratio())
print('\n')

def month_ratio():
    """Calculate the ratio between XVIRUS patients in January and XVIRUS patients in February.

    Outputs:
    string: Month Ratio
    """
    db = dbm.dumb.open('dmxvirus.db', 'r')
    jan = 0
    feb = 0
    xvirus_patients = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        if 'XVIRUS' in g:
            if '1/12/2030' in d:
                jan += 1
            if '2/12/2030' in d:
                feb += 1
            if '2/13/2030' in d:
                feb += 1
    result = ratio(jan, feb)
    db.close()
    return f'{result} is the ratio between XVIRUS patients in January and XVIRUS patients in February'

print(month_ratio())
print('\n')

def virus_Y_Z_ratio():
    """Calculate the ratio between YVIRUS and ZVIRUS over all months.

    Outputs:
    string: Virus Y to Z Ratio
    """
    db = dbm.dumb.open('dmxvirus.db', 'r')
    y = 0
    z = 0
    xvirus_patients = 0
    for k, v in db.items():
        a = pickle.loads(v)['patient_id']
        b = pickle.loads(v)['birthdate']
        c = pickle.loads(v)['Gender']
        d = pickle.loads(v)['admit_date']
        e = pickle.loads(v)['discharge_date']
        f = pickle.loads(v)['death_date']
        g = pickle.loads(v)['disease_code']
        
        if 'YVIRUS' in g:
            y += 1
        if 'ZVIRUS' in g:
            z += 1

    result = ratio(y, z)
    db.close()
    return f'{result} is the ratio between YVIRUS and ZVIRUS over all months in our data'

print(virus_Y_Z_ratio())
print('\n')

#-----------------------------------------------------------------------------------------Exercise 6------------------------------------------------------------------------

# XVIRUS CSV Files is used directly for this part instead of dmxvirus.db file

def LOS(admit, discharge):
    """Takes two dates and return the change between them
        Format: ('2/12/2030','2/14/2030')
        Output: 2

    Inputs:
    admit: string (admission date)
    discharge: string (discharge date)

    Output:
    int: length of stay
    """
    a = admit.split("/")
    d = discharge.split("/")

    for i in range(0, len(a)):
        a[i] = int(a[i])

    for i in range(0, len(d)):
        d[i] = int(d[i])

    if d[1] > a[1]:
        length_of_stay = d[1] - a[1]
    else:
        length_of_stay = (d[1] + a[1]) - a[1]

    return length_of_stay

def average_LOS(x):
    """Takes a list with admit and discharge dates and calculates the average length of stay of patients.

    Inputs:
    x: list (contains tuples of admit and discharge dates)

    Output:
    float: average length of stay
    """
    total_LOS = 0
    total_discharge = len(x)

    for a, d in x:
        total_LOS += LOS(a, d)

    average = round(total_LOS / total_discharge, 2)
    return average

def total_average_LOS():
    """Selects admit and discharge dates and save them in tuple format within a list.
    Example: x = [("'1/12/2030'", "'1/13/2030'"),("'1/12/2030'", "'1/13/2030'"),....]
    Next, feeds this list to the average_LOS function to get the average length of stay."""
    x = list()
    file = open("XVIRUS.csv")
    csv_dictionary = csv.DictReader(file)

    for line in csv_dictionary:
        admit = line.get("admit_date")
        discharge = line.get("discharge_date")

        if line.get("death_date") == "None":
            x.append((admit, discharge))
    
    print("For surviving patients, the average length of stay is", average_LOS(x), "days")

def XVIRUS_average_LOS():
    """Avg. length of stay for just XVIRUS patients."""
    x = list()
    file = open("XVIRUS.csv")
    csv_dictionary = csv.DictReader(file)

    for line in csv_dictionary:
        admit = line.get("admit_date")
        discharge = line.get("discharge_date")

        if line.get("death_date") == "NULL" and line.get("disease_code") == "XVIRUS":
            x.append((admit, discharge))

    print("For surviving patients with XVIRUS, the average length of stay is", average_LOS(x), "days")

total_average_LOS()
XVIRUS_average_LOS()































