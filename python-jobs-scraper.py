import requests
import argparse
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser(description="Scrape jobs listings from Python Jobs")
parser.add_argument("--keyword", type=str, help="search keyword", default="")
args = parser.parse_args()
keyword = args.keyword.lower()

URL = "https://www.python.org/jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_='row')

jobs = results.find_all('h2', class_='listing-company')

for job in jobs:

    title = job.find('a'[0])
    title = title.text.strip()

    if keyword in title.lower():
        company = job.find('br')
        company = company.next_sibling.strip()
        location = job.find('span', class_='listing-location')
        location = location.find('a'[0].strip())
        job_type = job.parent.find('span', class_='listing-job-type')
        job_type = job_type.find('a'[0].strip())
        posted = job.parent.find('span', class_='listing-posted')
        posted = posted.next + posted.next.next.text
        category = job.parent.find('span', class_='listing-company-category')
        category = category.find('a'[0].strip())

        print(title)
        print(company)
        print(location.text)
        print(job_type.text)
        print(posted)
        print(category.text)
        print()

