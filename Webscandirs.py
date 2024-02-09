import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import time

# Inizializza colorama
init(autoreset=True)

while True:
    # Chiedi all'utente di inserire il dominio o "exit" per uscire
    print(Fore.GREEN + "Inserisci il dominio (senza http/https) o scrivi 'exit' per uscire: ", end="")
    domain = input().strip()

    if domain.lower() == 'exit':
        print(Fore.LIGHTYELLOW_EX + "Grazie per aver provato il tool.t.me/Rapid85")
        break

    url = f"http://{domain}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Esempio: Trova tutti i link nella pagina
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href:
                print(Fore.CYAN + href)
                time.sleep(0.1)  # Aggiungi un ritardo per l'effetto macchina da scrivere
    else:
        print(Fore.RED + f"Errore nella richiesta: {response.status_code}")
