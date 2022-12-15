import arxiv
import re


def fetch_results():
    search = arxiv.Search(
    query = "artificial intelligence",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search.results()


def collect_data():
    papers = fetch_results()
    titles = []
    urls = []
    ids = []

    for result in papers:
        slashs = [m.start() for m in re.finditer('/', result.entry_id)]
        paper_id = result.entry_id[slashs[-1]+1:]
        titles.append(result.title)
        urls.append(result.pdf_url)
        ids.append(paper_id)
        
    return titles, urls, ids