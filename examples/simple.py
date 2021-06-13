# Modules
from termenu import PlainMenu

# Initialize our menu
menu = PlainMenu()

# Main option list
@menu.option("Check out GitHub!")
def check_github():
    print("You selected 'Check out GitHub!'.")

@menu.option("Read some documentation!")
def read_docs():
    print("You selected 'Read some documentation!'.")

@menu.option("Chill!")
def go_chill():
    print("You selected 'Chill!'.")

# Show menu
menu.display()
