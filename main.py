from pyscript import display, document

# Predefined sets of members (Grade 7–10)
grade7 = {"Zeek Fernandez", "Cheree Mendoza", "Therese Reyes"}
grade8 = {"Zoey Ledres", "Princess Schwab", "Adrian Gavina"}
grade9 = {"Kevin Polillo", "Anton Vinzon", "Nelson Velasco"}
grade10 = {"Earl Aljo", "Elise Ramos", "Austin Ocampo"}

# Combine all sets into one master set
all_members = grade7 | grade8 | grade9 | grade10

def add_member(event):
    # Get input values
    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()
    full_name = f"{first} {last}"

    # Add new member using set union
    global all_members
    all_members = all_members | {full_name}

    # Sort and display results
    members_list = "<br>".join(sorted(all_members))
    output = f"""
    <h4>Full List of Members:</h4>
    <p>{members_list}</p>
    <h5>Total Members: {len(all_members)}</h5>
    """
    display(output, target="results")

