import os
import sqlite3


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def dbconnection(dbname):
    try:
        conn = sqlite3.connect(dbname)
        print(f"Connected to the '{dbname}' database.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


def ls_table(conn):
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]


def display_menu():
    menu = """
    1. List Tables
    2. Choose Table
    3. Execute Query
    4. Exit
    """
    print(menu)


def table_select(conn):
    tables = ls_table(conn)

    if not tables:
        print("No tables found in the database.")
        return None

    print("Tables in the database:")
    for index, table in enumerate(tables, start=1):
        print(f"{index}. {table}")

    try:
        choice = input("Choose a table (enter the number) or press Enter to return to the main menu: ")

        if choice == '':
            return None

        choice = int(choice)

        if 1 <= choice <= len(tables):
            return tables[choice - 1]
        else:
            print("Invalid choice. Please enter a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def query_executor(conn, table):
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        # Fetch all rows from the chosen table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        # Clear the terminal before displaying the content
        clear_terminal()

        # Display the content of the table
        if rows:
            print(f"Content of the '{table}' table:")
            for row in rows:
                print(row)
        else:
            print(f"The '{table}' table is empty.")

    except sqlite3.Error as e:
        print(f"Error executing query: {e}")


def user_query(conn):
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        custom_query = input("Enter your custom SQL query (or press Enter to return to the main menu): ")

        if custom_query == '':
            return

        cursor.execute(custom_query)
        rows = cursor.fetchall()

        # Clear the terminal before displaying the content
        clear_terminal()

        # Display the result of the custom query
        if rows:
            print("Result of the custom query:")
            for row in rows:
                print(row)
        else:
            print("No results for the custom query.")

    except sqlite3.Error as e:
        print(f"Error executing custom query: {e}")


def main():
    database_name = input("Enter the database name: ")
    conn = dbconnection(database_name)

    if conn is None:
        print("Exiting program.")
        return

    while True:
        clear_terminal()
        display_menu()

        choice = input("Enter your choice (1/2/3/4): ")
        clear_terminal()
        if choice == '1':
            tables = ls_table(conn)
            if tables:
                print("Tables in the database:")
                for table in tables:
                    print(table)
        elif choice == '2':
            chosen_table = table_select(conn)
            if chosen_table:
                # Display the content of the chosen table
                query_executor(conn, chosen_table)
        elif choice == '3':
            user_query(conn)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        input("Press Enter to continue...")

    conn.close()


if __name__ == "__main__":
    main()
