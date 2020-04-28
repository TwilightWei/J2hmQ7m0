import urllib.request

from bs4 import BeautifulSoup

from django.utils import timezone

from app.config import TasksConfig

from .models import Record

# Parse html from url, and then record keyword number and time into db
def crawl():
    config = TasksConfig()
    url = config.get_url()
    keyword = config.get_keyword()
    keyword_num = 0
    r = urllib.request.urlopen(url)
    doc_bytes = r.read()
    doc = doc_bytes.decode("utf8")
    r.close()
    # Count keyword number in HTML
    soup = BeautifulSoup(doc, 'html.parser')
    a_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a'], text=True)
    for tag in a_tags:
        s = str(tag.string)
        keyword_num += s.count(keyword)
    # Record result in sql
    record = Record(keyword_number=keyword_num, crwal_time=timezone.now())
    record.save()