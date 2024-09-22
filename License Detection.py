import psycopg2

conn = psycopg2.connect(
    host="localhost",  
    database="stolen_vehicles_db",  
    user="your_username",  
    password="your_password"  
)
cursor = conn.cursor()

def check_license_plate(license_plate):
    query = "SELECT * FROM stolen_vehicles WHERE plate_number = %s"
    cursor.execute(query, (license_plate,))
    result = cursor.fetchone()

    if result:
        print(f"License plate {license_plate} is found in the database.")
    else:
        print(f"License plate {license_plate} is NOT found in the database.")

license_plate_input = input("Enter the license plate to check: ")

check_license_plate(license_plate_input)

conn.close()
