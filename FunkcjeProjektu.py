import folium



def show_list(companies):
    print("Firmy sprzątające: ")
    for company in companies:
        print(f" {company['name']}")

def add_company(companies):
    company = input("Podaj nazwę firmy sprzątającej do dodania: ")
    companies.append({"name": company, "clients": [], "workers": []})
    print(f" {company} został(a) pomyślnie dodana do listy.")
    show_list(companies)

def remove_company(companies):
    company_name = input("Podaj nazwę firmy sprzątającej do usunięcia: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            companies.remove(company)
            company_found = True
            print(f"{company_name} został(a) pomyślnie usunięta z listy.")
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")
    show_list(companies)

def update_company(companies):
    old_name = input("Podaj nazwę firmy sprzątającej do aktualizacji: ")
    company_found = False
    for company in companies:
        if company['name'] == old_name:
            new_name = input(f"Podaj nową nazwę dla {old_name}: ")
            company['name'] = new_name
            company_found = True
            print(f"Nazwa firmy została zmieniona z {old_name} na {new_name}.")
            break
    if not company_found:
        print(f"{old_name} nie znaleziono takiej firmy na liście.")
    show_list(companies)

def show_clients(companies):
    company_name = input("Podaj nazwę firmy, której lista klientów ma zostać wyświetlona: ")
    company_found = False
    for company in companies:
        if company["name"] == company_name:
            print(f"Lista klientów firmy {company_name}:")
            for client in company['clients']:
                print(f" - {client['name']}")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def add_client(companies):
    company_name = input("Podaj nazwę firmy, do której chcesz dodać klienta: ")
    company_found = False
    for company in companies:
        if company["name"] == company_name:
            client_name = input(f"Podaj imię i nazwisko klienta do dodania do {company_name}: ")
            company['clients'].append({"name": client_name})
            print(f"{client_name} został(a) dodany(a) do listy klientów firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def remove_client(companies):
    company_name = input("Podaj nazwę firmy, z której chcesz usunąć klienta: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            client_name = input(f"Podaj imię i nazwisko klienta do usunięcia z {company_name}: ")
            client_found = False
            for client in company['clients']:
                if client['name'] == client_name:
                    company['clients'].remove(client)
                    print(f"{client_name} został(a) usunięty(a) z listy klientów firmy {company_name}.")
                    client_found = True
                    break
            if not client_found:
                print(f"{client_name} nie znaleziono na liście klientów firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def update_client(companies):
    company_name = input("Podaj nazwę firmy, w której chcesz zaktualizować dane klienta: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            old_client_name = input(f"Podaj imię i nazwisko klienta do zaktualizowania w {company_name}: ")
            client_found = False
            for client in company['clients']:
                if client['name'] == old_client_name:
                    new_client_name = input(f"Podaj nowe imię i nazwisko dla {old_client_name}: ")
                    client['name'] = new_client_name
                    print(f"Dane klienta zostały zmienione z {old_client_name} na {new_client_name}.")
                    client_found = True
                    break
            if not client_found:
                print(f"{old_client_name} nie znaleziono na liście klientów firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def show_workers(companies):
    company_name = input("Podaj nazwę firmy, której lista pracowników ma zostać wyświetlona: ")
    company_found = False
    for company in companies:
        if company["name"] == company_name:
            print(f"Lista pracowników firmy {company_name}: ")
            for worker in company['workers']:
                print(f" - {worker['name']}")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def add_worker(companies):
    company_name = input("Podaj nazwę firmy, do której chcesz dodać pracownika: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            worker_name = input(f"Podaj imię i nazwisko pracownika do dodania do {company_name}: ")
            company['workers'].append({"name": worker_name})
            print(f"{worker_name} został dodany do listy pracowników firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def remove_worker(companies):
    company_name = input("Podaj nazwę firmy, z której chcesz usunąć pracownika: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            worker_name = input(f"Podaj nazwę pracownika do usunięcia z {company_name}: ")
            worker_found = False
            for worker in company['workers']:
                if worker['name'] == worker_name:
                    company['workers'].remove(worker)
                    print(f"{worker_name} został(a) usunięty(a) z listy pracowników firmy {company_name}.")
                    worker_found = True
                    break
            if not worker_found:
                print(f"{worker_name} nie znaleziono na liście pracowników firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def update_worker(companies):
    company_name = input("Podaj nazwę firmy, w której chcesz zaktualizować dane pracownika: ")
    company_found = False
    for company in companies:
        if company['name'] == company_name:
            old_worker_name = input(f"Podaj dane pracownika do zaktualizowania w {company_name}: ")
            worker_found = False
            for worker in company['workers']:
                if worker['name'] == old_worker_name:
                    new_worker_name = input(f"Podaj nowe dane dla {old_worker_name}: ")
                    worker['name'] = new_worker_name
                    print(f"Dane pracownika zostały zmienione z {old_worker_name} na {new_worker_name}.")
                    worker_found = True
                    break
            if not worker_found:
                print(f"{old_worker_name} nie znaleziono na liście pracowników firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

