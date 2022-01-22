from unittest import result
from bs4 import BeautifulSoup
import requests


def main():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    #job_elements = results.find_all("div", class_="card-content")
    
    # Selezionare gli elementi h2 del codice HTML che contengono
    # La parola python senza case sensitivity
    python_jobs = results.find_all(
            "h2", string=lambda text: "python" in text.lower()
            )
    
    # Comprehension list che opera sugli elementi di classe superiore
    # ad h2 (3 livelli sopra nella gerarchia)
    python_jobs_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]
    
    for job_element in python_jobs_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        
        # Snippet per link delle singole proposte lavorative di python
        links = job_element.find_all("a")
        for link in links:
            link_url = link["href"]
            if link_url != "https://www.realpython.com":
                print(f"Apply here: {link_url} \n")
        print()


if __name__== '__main__':
    main()

