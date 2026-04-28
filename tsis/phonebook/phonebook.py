import psycopg2
import json

def connection():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="max",
        password=""
    )
conn = connection()

def filter_by_group(conn):
    group_name = input("Enter group: ")
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_by_email(conn):
    email = input("Enter email: ")
    cur = conn.cursor()
    cur.execute("""
        SELECT name, email
        FROM contacts
        WHERE email ILIKE %s
    """, ('%' + email + '%',))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results")

def sort_contacts(conn):
    print("Sort by:")
    print("1. Name")
    print("2. Birthday")
    choice = input("Choose: ")
    cur = conn.cursor()
    if choice == "1":
        cur.execute("SELECT name, email, birthday FROM contacts ORDER BY name")
    elif choice == "2":
        cur.execute("SELECT name, email, birthday FROM contacts ORDER BY birthday")
    else:
        print("Invalid choice")
        return
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts")

def paginate(conn):
    limit = 5
    offset = 0
    while True:
        cur = conn.cursor()
        cur.execute(
            "SELECT name, email FROM contacts LIMIT %s OFFSET %s",
            (limit, offset)
        )
        rows = cur.fetchall()
        if not rows:
            print("No more data")
            break
        print("\n--- PAGE ---")
        for row in rows:
            print(row)
        cmd = input("next / prev / quit: ")
        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        elif cmd == "quit":
            break

def export_json(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append({
            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })
    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Exported to contacts.json")

def import_json(conn):
    cur = conn.cursor()
    with open("contacts.json", "r") as f:
        data = json.load(f)
    for item in data:
        name = item.get("name")
        email = item.get("email")
        birthday = item.get("birthday")
        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        exists = cur.fetchone()
        if exists:
            choice = input(f"{name} already exists. skip / overwrite: ")
            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
            else:
                print("Invalid choice, skipping...")
                continue
        cur.execute(
            "INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s)",
            (name, email, birthday)
        )
    conn.commit()
    print("Import finished!")

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Filter by group")
    print("4. Search by email")
    print("5. Sort contacts")
    print("6. Pagination")
    print("7. Export JSON")
    print("8. Import JSON")
    print("9. Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contacts(name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        print("Added!")

    elif choice == "2":
        query = input("Search: ")
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif choice == "3":
        filter_by_group(conn)
    elif choice == "4":
        search_by_email(conn)
    elif choice == "5":
        sort_contacts(conn)
    elif choice == "6":
        paginate(conn)
    elif choice == "7":
        export_json(conn)
    elif choice == "8":
        import_json(conn)
    elif choice == "9":
        break