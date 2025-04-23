import psycopg2
import csv

# 1. Подключение к базе данных
conn = psycopg2.connect(
    dbname="lab11",         # Название твоей БД
    user="postgres",        # Имя пользователя
    password="12345678",# Пароль
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 2. Создание таблицы (если ещё не создана)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(15)
);
""")
conn.commit()

# 3. Добавление контакта с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added.")

# 4. Добавление из CSV
def insert_from_csv(list1):
    with open(list1, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cursor.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Contacts loaded from CSV.")

# 5. Обновление записи
def update_contact(old_name, new_name=None, new_phone=None):
    if new_name:
        cursor.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    if new_phone:
        cursor.execute("UPDATE contacts SET phone = %s WHERE first_name = %s", (new_phone, old_name))
    conn.commit()
    print("Contact updated.")

# 6. Поиск контактов
def search_contacts(filter_name=None, filter_phone=None):
    query = "SELECT * FROM contacts WHERE true"
    values = []
    if filter_name:
        query += " AND first_name ILIKE %s"
        values.append(f"%{filter_name}%")
    if filter_phone:
        query += " AND phone LIKE %s"
        values.append(f"%{filter_phone}%")
    cursor.execute(query, values)
    results = cursor.fetchall()
    print("Search results:")
    for row in results:
        print(row)

# 7. Удаление контакта
def delete_contact(name=None, phone=None):
    if name:
        cursor.execute("DELETE FROM contacts WHERE first_name = %s", (name,))
    elif phone:
        cursor.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    conn.commit()
    print("Contact deleted.")

# 8. Меню
def main():
    while True:
        print("\n==== PhoneBook Menu ====")
        print("1. Add contact (console)")
        print("2. Load contacts (CSV)")
        print("3. Update contact")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            list1 = input("Enter CSV list1: ")
            insert_from_csv(list1)
        elif choice == '3':
            name = input("Old name: ")
            new_name = input("New name (Enter to skip): ")
            new_phone = input("New phone (Enter to skip): ")
            update_contact(name, new_name or None, new_phone or None)
        elif choice == '4':
            name = input("Search by name: ")
            phone = input("Search by phone: ")
            search_contacts(name or None, phone or None)
        elif choice == '5':
            name = input("Delete by name (Enter to skip): ")
            phone = input("Delete by phone (Enter to skip): ")
            delete_contact(name or None, phone or None)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

    # Закрытие соединения
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
