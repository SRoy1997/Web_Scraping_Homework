from os import times
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# job_titles = soup.find_all('h2')

# for job in job_titles:
#   print(job.text)

card_content_tags = soup.find_all('div', class_='card-content')

for job in card_content_tags:
  job_title = job.find('h2')

  if job_title:
    job_title = job_title.text.strip()

  # print(job_title)

  company = job.find('h3', class_='company')

  if company:
    company = company.text.strip()

  location = job.find(class_='location')

  if location:
    location = location.text.strip()

  time_stamp = job.find('time')

  if time_stamp:
    time_stamp = time_stamp.text.strip()

  print(job_title + ' ..... ' + company + ' ..... ' + location + ' ..... ' + time_stamp)