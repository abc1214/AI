#Write a program for to implement Rule based system

# Hypothesis that should be tested
def hypothesis(Disease):
    if Disease == 'cold':
        cold()
    elif Disease == 'flu':
        flu()
    elif Disease == 'typhoid':
        typhoid()
    elif Disease == 'measles':
        measles()
    elif Disease == 'malaria':
        malaria()
    else:
        print("Unknown")

# Hypothesis Identification Rules
def cold():
    if verify('headache') and verify('runny_nose') and verify('sneezing') and verify('sore_throat'):
        print('I believe that the patient has cold')
        print('Advices and Suggestions:')
        print('1: Tylenol/tab')
        print('2: panadol/tab')
        print('3: Nasal spray')
        print('Please wear warm clothes Because')
        undo()
    else:
        print("Unknown")

def flu():
    if verify('fever') and verify('headache') and verify('chills') and verify('body_ache'):
        print('I believe that the patient has flu')
        print('Advices and Suggestions:')
        print('1: Tamiflu/tab')
        print('2: panadol/tab')
        print('3: Zanamivir/tab')
        print('Please take a warm bath and do salt gargling Because')
        undo()
    else:
        print("Unknown")

def typhoid():
    if verify('headache') and verify('abdominal_pain') and verify('poor_appetite') and verify('fever'):
        print('I believe that the patient has typhoid')
        print('Advices and Suggestions:')
        print('1: Chloramphenicol/tab')
        print('2: Amoxicillin/tab')
        print('3: Ciprofloxacin/tab')
        print('4: Azithromycin/tab')
        print('Please do complete bed rest and take a soft Diet Because')
        undo()
    else:
        print("Unknown")

def measles():
    if verify('fever') and verify('runny_nose') and verify('rash') and verify('conjunctivitis'):
        print('I believe that the patient has measles')
        print('Advices and Suggestions:')
        print('1: Tylenol/tab')
        print('2: Aleve/tab')
        print('3: Advil/tab')
        print('4: Vitamin A')
        print('Please get rest and use more liquid Because')
        undo()
    else:
        print("Unknown")

def malaria():
    if verify('fever') and verify('sweating') and verify('headache') and verify('nausea') and verify('vomiting') and verify('diarrhea'):
        print('I believe that the patient has malaria')
        print('Advices and Suggestions:')
        print('1: Aralen/tab')
        print('2: Qualaquin/tab')
        print('3: Plaquenil/tab')
        print('4: Mefloquine')
        print('Please do not sleep in open air and cover your full skin Because')
        undo()
    else:
        print("Unknown")

# How to ask questions
def ask(Question):
    Response = input('Does the patient have the following symptom: ' + Question + '? ')
    if Response.lower() == 'yes' or Response.lower() == 'y':
        assert_yes(Question)
        return True
    else:
        assert_no(Question)
        return False

# How to verify something
def verify(S):
    if S in known_yes:
        return True
    elif S in known_no:
        return False
    else:
        return ask(S)

# Undo all yes/no assertions
def undo():
    global known_yes
    global known_no
    known_yes = set()
    known_no = set()

def assert_yes(Question):
    known_yes.add(Question)

def assert_no(Question):
    known_no.add(Question)

# Initialize knowledge base
known_yes = set()
known_no = set()

# Start the diagnosis
hypothesis('cold')
