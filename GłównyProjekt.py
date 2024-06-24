from Lista import companies
from FunkcjeProjektu import show_list, add_company, remove_company, update_company, show_clients, add_client, remove_client, update_client, show_workers, add_worker, remove_worker, update_worker, show_company_map, show_worker_map, show_client_map

correct_password = "SprzątaćKażdyMoże123"
logged_in = False

while not logged_in:
    password = input("Wprowadź hasło: ")
    if password == correct_password:
        print("Pomyślnie zalogowano.")
        logged_in = True
    else:
        print("Hasło niepoprawne.")

if logged_in:
    if __name__ == '__main__':
        print("Witaj w systemie zarządzania firmami sprzątającymi.")
        while True:
            print("Menu:")
            print("0. Zakończ pracę")
            print("1. Firmy sprzątające")
            print("2. Klienci")
            print("3. Pracownicy")
            menu_option = input("Wybierz opcję: ")
            if menu_option == '0':
                break
            elif menu_option == '1':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę firm sprzątających")
                    print("2. Dodaj firmę do listy")
                    print("3. Usuń firmę z listy")
                    print("4. Aktualizuj nazwę firmy")
                    print("5. Wyświetl lokalizację firmy")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_list(companies)
                    elif opcja == '2':
                        add_company(companies)
                        show_list(companies)
                    elif opcja == '3':
                        remove_company(companies)
                        show_list(companies)
                    elif opcja == '4':
                        update_company(companies)
                        show_list(companies)
                    elif opcja == '5':
                        show_company_map(companies)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
            elif menu_option == '2':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę klientów danej firmy")
                    print("2. Dodaj klienta do firmy")
                    print("3. Usuń klienta z firmy")
                    print("4. Aktualizuj dane klienta")
                    print("5. Wyświetl lokalizację klienta")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_clients(companies)
                    elif opcja == '2':
                        add_client(companies)
                    elif opcja == '3':
                        remove_client(companies)
                    elif opcja == '4':
                        update_client(companies)
                    elif opcja == '5':
                        show_client_map(companies)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
            elif menu_option == '3':
                while True:
                    print("0. Powrót do menu głównego")
                    print("1. Wyświetl listę pracowników danej firmy")
                    print("2. Dodaj pracownika do firmy")
                    print("3. Usuń pracownika z firmy")
                    print("4. Aktualizuj dane pracownika")
                    print("5. Wyświetl lokalizację pracownika")
                    opcja = input("Wybierz opcję: ")
                    if opcja == '0':
                        break
                    elif opcja == '1':
                        show_workers(companies)
                    elif opcja == '2':
                        add_worker(companies)
                    elif opcja == '3':
                        remove_worker(companies)
                    elif opcja == '4':
                        update_worker(companies)
                    elif opcja == '5':
                        show_client_map(companies)
                    else:
                        print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
        print("Dziękujemy za skorzystanie z systemu. Do widzenia!")