import urllib.request

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
    # Record result in sql