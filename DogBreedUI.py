import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('DogBreed.db')
cursor = conn.cursor()

def display_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Dog Breed Database Interface!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option:")
    print("1. Insert Data")
    print("2. Delete Data")
    print("3. Update Data")
    print("4. Search Data")
    print("5. Aggregate Functions")
    print("6. Sorting")
    print("7. Joins")
    print("8. Grouping")
    print("9. Subqueries")
    print("10. Transactions")
    print("11. Error Handling")
    print("12. Exit")

def table_menu():
    print("Please select an option:")
    print("1. compatibility")
    print("2. adaptability")
    print("3. grooming")
    print("4. health")
    print("5. exercise needs")
    print("6. appearance")
    print("7. trainability")

def columns(table_name):
        columns = []
        if table_name == '1':
            columns = "'breed_name', 'with_other_pets', 'with_children', 'with_seniors', 'lifestyle_type'"
        elif table_name == '2':
            columns = "'breed_name', 'temperament', 'adjustment', 'sociability'"
        elif table_name == '3':
            columns = "'breed_name, frequency, shedding_level, coat_type'"
        elif table_name == '4':
            columns = "'breed_name', 'lifespan', 'health_issues', 'genetic_disposition'"
        elif table_name == '5':
            columns = "'breed_name',  'mental_stimulation', 'exercise_requirements', 'activity_level', 'suitability'"
        elif table_name == '6':
            columns = "'breed_name',  'physical_features', 'breed_standards', 'size', 'color'"
        elif table_name == '7':
            columns = "'breed_name', 'intelligence_level', 'trainability_rating', 'training_methods'"
        else:
            print("Invalid choice. Please try again.")
        return columns

#insert record
def insert_data():
    breed_name = input("Enter breed name to insert: ")
    table_menu()
    table_name = input("Enter your choice (1-7): ")

    if table_name == '1':
        insert_compatibility_data(breed_name)
    elif table_name == '2':
        insert_adaptability_data(breed_name)
    elif table_name == '3':
        insert_grooming_data(breed_name)
    elif table_name == '4':
        insert_health_data(breed_name)
    elif table_name == '5':
        insert_exercise_needs_data(breed_name)
    elif table_name == '6':
        insert_appearance_data(breed_name)
    elif table_name == '7':
        insert_trainability_data(breed_name)
    else:
        print("Invalid choice. Please try again.")

#insert record into table
def insert_compatibility_data(breed_name):
    try:
        with_other_pets = input("Compatible with other pets? (yes/no): ").lower() == 'yes'
        with_children = input("Compatible with children? (yes/no): ").lower() == 'yes'
        with_seniors = input("Compatible with seniors? (yes/no): ").lower() == 'yes'
        lifestyle_type = input("Enter lifestyle type: ")

        cursor.execute("INSERT INTO compatibility (breed_name, with_other_pets, with_children, with_seniors, lifestyle_type) VALUES (?, ?, ?, ?, ?)",
                    (breed_name, with_other_pets, with_children, with_seniors, lifestyle_type))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        # print("Error inserting record:", e)
        error_handling(e)
def insert_adaptability_data(breed_name):
    try:
        temperament = input("Enter temperament: ")
        adjustment = input("Enter adjustment: ")
        sociability = input("Enter sociability: ")

        cursor.execute("INSERT INTO adaptability (breed_name, temperament, adjustment, sociability) VALUES (?, ?, ?, ?)",
                    (breed_name, temperament, adjustment, sociability))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def insert_grooming_data(breed_name):
    try:
        frequency = input("Enter frequency: ")
        shedding_level = input("Enter shedding level: ")
        coat_type = input("Enter coat type: ")

        cursor.execute("INSERT INTO grooming (breed_name, frequency, shedding_level, coat_type) VALUES (?, ?, ?, ?)",
                    (breed_name, frequency, shedding_level, coat_type))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def insert_health_data(breed_name):
    try:
        lifespan = input("Enter lifespan: ")
        health_issues = input("Enter health issues: ")
        genetic_disposition = input("Enter genetic disposition: ")

        cursor.execute("INSERT INTO health (breed_name, lifespan, health_issues, genetic_disposition) VALUES (?, ?, ?, ?)",
                    (breed_name, lifespan, health_issues, genetic_disposition))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def insert_exercise_needs_data(breed_name):
    try:
        mental_stimulation = input("Enter mental stimulation: ")
        exercise_requirements = input("Enter exercise requirements: ")
        activity_level = input("Enter activity level: ")
        suitability = input("Enter suitability: ")

        cursor.execute("INSERT INTO exercise_needs (breed_name, mental_stimulation, exercise_requirements, activity_level, suitability) VALUES (?, ?, ?, ?, ?)",
                    (breed_name,  mental_stimulation, exercise_requirements, activity_level, suitability))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def insert_appearance_data(breed_name):
    try:
        physical_features = input("Enter physical features: ")
        breed_standards = input("Enter breed_standards: ")
        size = input("Enter size: ")
        color = input("Enter color: ")

        cursor.execute("INSERT INTO appearance (breed_name, physical_features, breed_standards, size, color) VALUES (?, ?, ?, ?, ?)",
                    (breed_name,  physical_features, breed_standards, size, color))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def insert_trainability_data(breed_name):
    try:
        intelligence_level = input("Enter intelligence level: ")
        trainability_rating = input("Enter trainability rating: ")
        training_methods = input("Enter training methods: ")

        cursor.execute("INSERT INTO trainability (breed_name, intelligence_level, trainability_rating, training_methods) VALUES (?, ?, ?, ?)",
                    (breed_name, intelligence_level, trainability_rating, training_methods))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        error_handling(e)

#delete record
def delete_data():
    breed_name = input("Enter breed name to delete: ")
    table_menu()
    table_name = input("Enter your choice (1-7): ")

    if table_name == '1':
        delete_compatibility_data(breed_name)
    elif table_name == '2':
        delete_adaptability_data(breed_name)
    elif table_name == '3':
        delete_grooming_data(breed_name)
    elif table_name == '4':
        delete_health_data(breed_name)
    elif table_name == '5':
        delete_exercise_needs_data(breed_name)
    elif table_name == '6':
        delete_appearance_data(breed_name)
    elif table_name == '7':
        delete_trainability_data(breed_name)
    else:
        print("Invalid choice. Please try again.")

#delete record from table
def delete_compatibility_data(breed_name):
    try:
        cursor.execute("DELETE FROM compatibility WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def delete_adaptability_data(breed_name):
    try:
        cursor.execute("DELETE FROM adaptability WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def delete_grooming_data(breed_name):
    try:
        cursor.execute("DELETE FROM grooming WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def delete_health_data(breed_name):
    try:
        cursor.execute("DELETE FROM health WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        error_handling(e)
    except sqlite3.Error as e:
        print("Error deleting record:", e)
def delete_exercise_needs_data(breed_name):
    try:
        cursor.execute("DELETE FROM exercise_needs WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        error_handling(e)
    except sqlite3.Error as e:
        error_handling(e)
def delete_appearance_data(breed_name):
    try:
        cursor.execute("DELETE FROM appearance WHERE breed_name = ?",
                    (breed_name,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def delete_trainability_data(breed_name):
        try:
            cursor.execute("DELETE FROM trainability WHERE breed_name = ?",
                        (breed_name,))
            conn.commit()
            print("Record deleted successfully.")
        except sqlite3.Error as e:
            error_handling(e)

#update record
def update_data():
    breed_name = input("Enter breed name to update: ")
    table_menu()
    table_name = input("Enter your choice (1-7)")

    if table_name == '1':
        update_compatibility_data(breed_name)
    elif table_name == '2':
        update_adaptability_data(breed_name)
    elif table_name == '3':
        update_grooming_data(breed_name)
    elif table_name == '4':
        update_health_data(breed_name)
    elif table_name == '5':
        update_exercise_needs_data(breed_name)
    elif table_name == '6':
        update_appearance_data(breed_name)
    elif table_name == '7':
        update_trainability_data(breed_name)
    else:
        print("Invalid choice. Please try again.")

#update record in table
def update_compatibility_data(breed_name):
    try:
        new_with_other_pets = input("Compatible with other pets? (yes/no): ").lower() == 'yes'
        new_with_children = input("Compatible with children? (yes/no): ").lower() == 'yes'
        new_with_seniors = input("Compatible with seniors? (yes/no): ").lower() == 'yes'
        new_lifestyle_type = input("Enter new lifestyle type: ")

        cursor.execute("UPDATE compatibility SET with_other_pets = ?, with_children = ?, with_seniors = ?, lifestyle_type = ? WHERE breed_name = ?", 
                        (new_with_other_pets, new_with_children, new_with_seniors, new_lifestyle_type, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_adaptability_data(breed_name):
    try:
        new_temperament = input("Enter new temperament: ")
        new_adjustment = input("Enter new adjustment: ")
        new_sociability = input("Enter new sociability: ")

        cursor.execute("UPDATE adaptability SET temperament = ?, adjustment = ?, sociability = ? WHERE breed_name = ?", (new_temperament, new_adjustment, new_sociability, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_grooming_data(breed_name):
    try:
        new_frequency = input("Enter new grooming frequency: ")
        new_shedding_level = input("Enter new shedding level: ")
        new_coat_type = input("Enter new coat type: ")

        cursor.execute("UPDATE grooming SET frequency = ?, shedding_level = ?, coat_type = ? WHERE breed_name = ?", 
                        (new_frequency, new_shedding_level, new_coat_type, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_health_data(breed_name):
    try:
        new_lifespan = input("Enter new lifespan: ")
        new_health_issues = input("Enter new health issues: ")
        new_genetic_disposition = input("Enter new genetic disposition: ")

        # Execute the SQL UPDATE statement
        cursor.execute("UPDATE health SET lifespan = ?, health_issues = ?, genetic_disposition = ? WHERE breed_name = ?", 
                        (new_lifespan, new_health_issues, new_genetic_disposition, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_exercise_needs_data(breed_name):
    try:
        new_mental_stimulation = input("Enter new mental stimulation: ")
        new_exercise_requirements = input("Enter new exercise requirements: ")
        new_activity_level = input("Enter new activity level: ")
        new_suitability = input("Enter new suitability: ")

        cursor.execute("UPDATE exercise_needs SET mental_stimulation = ?, exercise_requirements = ?, activity_level = ?, suitability = ? WHERE breed_name = ?", 
                        (new_mental_stimulation, new_exercise_requirements, new_activity_level, new_suitability, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_appearance_data(breed_name):
    try:
        new_physical_features = input("Enter new physical features: ")
        new_breed_standards = input("Enter new breed standards: ")
        new_size = input("Enter new size: ")
        new_color = input("Enter new color: ")

        cursor.execute("UPDATE appearance SET physical_features = ?, breed_standards = ?, size = ?, color = ? WHERE breed_name = ?", 
                        (new_physical_features, new_breed_standards, new_size, new_color, breed_name))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        error_handling(e)
def update_trainability_data(breed_name): 
        try:
            new_intelligence_level = input("Enter new intelligence level: ")
            new_trainability_rating = input("Enter new trainability rating: ")
            new_training_methods = input("Enter new training methods: ")

            cursor.execute("UPDATE trainability SET intelligence_level = ?, trainability_rating = ?, training_methods = ? WHERE breed_name = ?", 
                            (new_intelligence_level, new_trainability_rating, new_training_methods, breed_name))
            conn.commit()
            print("Record updated successfully.")
        except sqlite3.Error as e:
            error_handling(e)

#search record
def search_data():
    breed_name = input("Enter breed name to search: ")
    table_menu()
    table_name = input("Enter your choice (1-7):")

    if table_name == '1':
        search_compatibility_data(breed_name)
    elif table_name == '2':
        search_adaptability_data(breed_name)
    elif table_name == '3':
        search_grooming_data(breed_name)
    elif table_name == '4':
        search_health_data(breed_name)
    elif table_name == '5':
        search_exercise_needs_data(breed_name)
    elif table_name == '6':
        search_appearance_data(breed_name)
    elif table_name == '7':
        search_trainability_data(breed_name)
    else:
        print("Invalid choice. Please try again.")
    
#search record in table
def search_compatibility_data(breed_name):
    try:
        function = input("Aggregate function? (yes/no): ")
        group = input("Group commands? (yes/no): ")
        if function == 'yes' and group == 'yes':
            cursor.execute(f"SELECT {aggfunc_compatibility} FROM compatibility GROUP BY {group_compatibility}")
        elif function == 'yes':
            cursor.execute(f"SELECT {aggfunc_compatibility} FROM compatibility WHERE breed_name = ?", (breed_name,))
        elif group == 'yes':
            cursor.execute(f"SELECT * FROM compatibility GROUP BY {group_compatibility}, (breed_name,)")
        else:
            cursor.execute("SELECT * FROM compatibility WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("With Other Pets:", "Yes" if record[2] else "No")
            print("With Children:", "Yes" if record[3] else "No")
            print("With Seniors:", "Yes" if record[4] else "No")
            print("Lifestyle Type:", record[5])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_adaptability_data(breed_name):
    try:
        cursor.execute("SELECT * FROM adaptability WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("Temperament:", record[2])
            print("Adjustment:", record[3])
            print("Sociability:", record[4])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_grooming_data(breed_name):
    try:
        cursor.execute("SELECT * FROM grooming WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("Frequency:", record[2])
            print("Shedding Level:", record[3])
            print("Coat Type:", record[4])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_health_data(breed_name):
    try:
        cursor.execute("SELECT * FROM health WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("Lifespan:", record[2])
            print("Health Issues:", record[3])
            print("Genetic Disposition:", record[4])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_exercise_needs_data(breed_name):
    try:
        cursor.execute("SELECT * FROM exercise_needs WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("Mental Stimulation:", record[2])
            print("Exercise Requirements:", record[3])
            print("Activity Level:", record[4])
            print("Suitability:", record[5])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_appearance_data(breed_name):
    try:
        cursor.execute("SELECT * FROM appearance WHERE breed_name = ?", (breed_name,))
        record = cursor.fetchone()

        if record:
            print("Record found:")
            print("Breed Name:", record[1])
            print("Physical Features:", record[2])
            print("Breed Standards:", record[3])
            print("Size:", record[4])
            print("Color:", record[5])
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        error_handling(e)
def search_trainability_data(breed_name):
        try:
            cursor.execute("SELECT * FROM trainability WHERE breed_name = ?", (breed_name,))
            record = cursor.fetchone()

            if record:
                print("Record found:")
                print("Breed Name:", record[1])
                print("Intelligence Level:", record[2])
                print("Trainability Rating:", record[3])
                print("Training Methods:", record[4])
                # Print other columns as needed
            else:
                print("Record not found.")
        except sqlite3.Error as e:
            error_handling(e)

#aggregate functions
def aggregate_functions():
    table_menu()
    table_name = input("Enter your choice (1-7): ")

    if table_name == '1':
        aggfunc_compatibility()
    elif table_name == '2':
        aggfunc_adaptability()
    elif table_name == '3':
        aggfunc_grooming()
    elif table_name == '4':
        aggfunc_health()
    elif table_name == '5':
        aggfunc_exercise_needs()
    elif table_name == '6':
        aggfunc_appearance()
    elif table_name == '7':
        aggfunc_trainability()
    else:
        print("Invalid choice. Please try again.")

#aggregate function in table
def aggfunc_compatibility():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name, with_other_pets, with_children, with_seniors, lifestyle_type)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name', 'with_other_pets', 'with_children', 'with_seniors', 'lifestyle_type']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM compatibility")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_adaptability():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name, temperament, adjustment, sociability)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name', 'temperament', 'adjustment', 'sociability']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM adaptability")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_grooming():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name, frequency, shedding_level, coat_type)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name, frequency, shedding_level, coat_type']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM grooming")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_health():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name, lifespan, health_issues, genetic_disposition)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name', 'lifespan', 'health_issues', 'genetic_disposition']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM health")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_exercise_needs():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name,  mental_stimulation, exercise_requirements, activity_level, suitability)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name',  'mental_stimulation', 'exercise_requirements', 'activity_level', 'suitability']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM exercise_needs")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_appearance():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name,  physical_features, breed_standards, size, color)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name',  'physical_features', 'breed_standards', 'size', 'color']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM appearance")

    except sqlite3.Error as e:
        error_handling(e)
def aggfunc_trainability():
    try:
        function = input("Select the function: (SUM, COUNT, AVG, MIN, MAX") 
        column = input("Select the column that you want to put in order: (breed_name, intelligence_level, trainability_rating, training_methods)")

        if function not in ['SUM', 'COUNT', 'AVG', 'MIN', 'MAX']:
            raise ValueError("Invalid function.")
        if column not in ['breed_name', 'intelligence_level', 'trainability_rating', 'training_methods']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT {function}({column}) FROM trainability")

    except sqlite3.Error as e:
        error_handling(e)


#sorting
def sorting():
    table_menu()
    table_name = input("Enter your choice (1-7): ")

    if table_name == '1':
        sort_compatibility()
    elif table_name == '2':
        sort_adaptability()
    elif table_name == '3':
        sort_grooming()
    elif table_name == '4':
        sort_health()
    elif table_name == '5':
        sort_exercise_needs()
    elif table_name == '6':
        sort_appearance()
    elif table_name == '7':
        sort_trainability()
    else:
        print("Invalid choice. Please try again.")

#sorting for each table
def sort_compatibility():
    try:
        order = input("Select the order of the column: (ASC/DESC): ")
        column = input("Select the column that you want to put in order: (breed_name, with_other_pets, with_children, with_seniors, lifestyle_type): ")

        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name', 'with_other_pets', 'with_children', 'with_seniors', 'lifestyle_type']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM compatibility ORDER BY {column} {order}")

        sorted_records = cursor.fetchall()

        if sorted_records:
            print("Sorted Compatibility Records:")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("With Other Pets:", record[2])
                print("With Children:", record[3])
                print("With Seniors:", record[4])
                print("Lifestyle Type:", record[5])
                print()
        else:
            print("No compatibility records found.")

    except sqlite3.Error as e:
        error_handling(e)
def sort_adaptability():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name, temperament, adjustment, sociability)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name', 'temperament', 'adjustment', 'sociability']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM adaptability ORDER BY {column} {order}")

        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Adaptability Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Temperament:", record[2])
                print("Adjustment:", record[3])
                print("Sociability:", record[4])
                print()
        else:
            print("No adaptability records found.")

    except sqlite3.Error as e:
        error_handling(e)
def sort_grooming():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name, frequency, shedding_level, coat_type)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name, frequency, shedding_level, coat_type']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM grooming ORDER BY {column} {order}")
        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Grooming Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Frequency:", record[2])
                print("Shedding Level:", record[3])
                print("Coat Type:", record[4])
                print() 
        else:
            print("No grooming records found.")
    except sqlite3.Error as e:
        error_handling(e)
def sort_health():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name, lifespan, health_issues, genetic_disposition)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name', 'lifespan', 'health_issues', 'genetic_disposition']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM health ORDER BY {column} {order}")
        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Health Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Lifespan:", record[2])
                print("Health Issues:", record[3])
                print("Genetic Disposition:", record[4])
                print()  # Print an empty line for readability
        else:
            print("No health records found.")

    except sqlite3.Error as e:
        error_handling(e)
def sort_exercise_needs():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name,  mental_stimulation, exercise_requirements, activity_level, suitability)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name',  'mental_stimulation', 'exercise_requirements', 'activity_level', 'suitability']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM exercise_needs ORDER BY {column} {order}")

        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Exercise Needs Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Mental Stimulation:", record[2])
                print("Exercise Requirements:", record[3])
                print("Activity Level:", record[4])
                print("Suitability:", record[5])
                print()  # Print an empty line for readability
        else:
            print("No exercise needs records found.")

    except sqlite3.Error as e:
        error_handling(e)
def sort_appearance():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name,  physical_features, breed_standards, size, color)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name',  'physical_features', 'breed_standards', 'size', 'color']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM appearance ORDER BY {column} {order}")
        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Appearance Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Physical Features:", record[2])
                print("Breed Standards:", record[3])
                print("Size:", record[4])
                print("Color:", record[5])
                print()  # Print an empty line for readability
        else:
            print("No appearance records found.")
    except sqlite3.Error as e:
        error_handling(e)
def sort_trainability():
    try:
        order = input("Select the order of the column: (ASC/DESC)").lower() == 'ASC'
        column = input("Select the column that you want to put in order: (breed_name, intelligence_level, trainability_rating, training_methods)")
        if order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order. Please enter either 'ASC' or 'DESC'.")
        if column not in ['breed_name', 'intelligence_level', 'trainability_rating', 'training_methods']:
            raise ValueError("Invalid column.")
        cursor.execute(f"SELECT * FROM trainability ORDER BY {column} {order}")
        sorted_records = cursor.fetchall()

        if sorted_records:
            print(f"Sorted Trainability Records by {column} ({order}):")
            for record in sorted_records:
                print("Breed Name:", record[1])
                print("Intelligence Level:", record[2])
                print("Trainability Rating:", record[3])
                print("Training Methods:", record[4])
                print()  # Print an empty line for readability
        else:
            print("No trainability records found.")

    except sqlite3.Error as e:
        error_handling(e)

#joins
def joins():
    table_menu()
    table_name1 = input("Enter your choice for the first table (1-7): ")
    table_menu()
    table_name2 = input("Enter your choice for the second table (1-7): ")
    if table_name1 == table_name2:
        print("Invalid choice. Please try again.")
    else:
        try:
            first1 = table_name1[0]
            first2 = table_name2[0]
            cursor.execute(f"SELECT * FROM {table_name1} {first1} INNER JOIN {table_name2} {first2} ON {first1}.breed_name = {first2}.breed_name")
        except sqlite3.Error as e:
            error_handling(e)   


#grouping
def grouping():
    table_menu()
    table_name = input("Enter your choice (1-7): ")

    if table_name == '1':
        group_compatibility()
    elif table_name == '2':
        group_adaptability()
    elif table_name == '3':
        group_grooming()
    elif table_name == '4':
        group_health()
    elif table_name == '5':
        group_exercise_needs()
    elif table_name == '6':
        group_appearance()
    elif table_name == '7':
        group_trainability()
    else:
        print("Invalid choice. Please try again.")

def group_compatibility():
    column = input("Select the column that you want to put in order: (breed_name, with_other_pets, with_children, with_seniors, lifestyle_type)")

    if column not in ['breed_name', 'with_other_pets', 'with_children', 'with_seniors', 'lifestyle_type']:
        raise ValueError("Invalid column.")
def group_adaptability():
    column = input("Select the column that you want to put in order: (breed_name, temperament, adjustment, sociability)")

    if column not in ['breed_name', 'temperament', 'adjustment', 'sociability']:
        raise ValueError("Invalid column.")
def group_grooming():
    column = input("Select the column that you want to put in order: (breed_name, frequency, shedding_level, coat_type)")
    
    if column not in ['breed_name, frequency, shedding_level, coat_type']:
        raise ValueError("Invalid column.")
def group_health():
    column = input("Select the column that you want to put in order: (breed_name, lifespan, health_issues, genetic_disposition)")

    if column not in ['breed_name', 'lifespan', 'health_issues', 'genetic_disposition']:
        raise ValueError("Invalid column.")
def group_exercise_needs():
    column = input("Select the column that you want to put in order: (breed_name,  mental_stimulation, exercise_requirements, activity_level, suitability)")
    
    if column not in ['breed_name',  'mental_stimulation', 'exercise_requirements', 'activity_level', 'suitability']:
        raise ValueError("Invalid column.") 
def group_appearance():
    column = input("Select the column that you want to put in order: (breed_name,  physical_features, breed_standards, size, color)")
    
    if column not in ['breed_name',  'physical_features', 'breed_standards', 'size', 'color']:
        raise ValueError("Invalid column.")
def group_trainability():
    column = input("Select the column that you want to put in order: (breed_name, intelligence_level, trainability_rating, training_methods)")

    if column not in ['breed_name', 'intelligence_level', 'trainability_rating', 'training_methods']:
        raise ValueError("Invalid column.")

#subqueries
def subqueries():
    try:
        table_menu()
        main_table = input("Enter your choice for the first table (1-7): ")
        main_column = input(f"Enter the name of the column in {columns(main_table)}")
        table_menu()
        sub_table = input("Enter your choice for the second table (1-7): ")
        sub_column = input(f"Enter the name of the column in {columns(sub_table)}")

        cursor.execute(f"SELECT * FROM {main_table} WHERE {main_column} IN (SELECT {sub_column} FROM {sub_table})")
        records = cursor.fetchall()
        
        for record in records:
            print(record)
    except sqlite3.Error as e:
        error_handling(e)   


#transactions
def transactions():
    try:
        conn.execute("START TRANSACTION")

        while True:
            display_menu()
            choice = input("Enter your choice (1-12): ")
            if choice == '1':
                insert_data()
            elif choice == '2':
                delete_data()
            elif choice == '3':
                update_data()
            elif choice == '4':
                search_data()
            elif choice == '5':
                aggregate_functions()
            elif choice == '6':
                sorting()
            elif choice == '7':
                joins()
            elif choice == '8':
                grouping()
            elif choice == '9':
                subqueries()
            elif choice == '11':
                error_handling()
            elif choice == '12':
                exit = input("are you sure that you want to exit transactions? (yes/no): ").lower == 'yes'
                if exit == "yes":
                    break
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")

        conn.commit()
        print("Transactions committed successfully.")

    except sqlite3.Error as e:
        conn.rollback()
        print("Error performing transactions. Rolling back changes:", e)

#error handling
def error_handling(e):
        print("Error:", e)
   
#main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-12): ")

    if choice == '1':
        insert_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        search_data()
    elif choice == '5':
        aggregate_functions()
    elif choice == '6':
        sorting()
    elif choice == '7':
        joins()
    elif choice == '8':
        grouping()
    elif choice == '9':
        subqueries()
    elif choice == '10':
        transactions()
    elif choice == '11':
        error_handling()
    elif choice == '12':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
