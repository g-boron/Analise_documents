import arxiv
import re
from progress.bar import Bar


def fetch_results():
    search = arxiv.Search(
    query = "artificial intelligence",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search.results()


def collect_data():
    print()
    print('Collecting data..')

    papers = fetch_results()
    titles = []
    urls = []
    ids = []

    with Bar('Processing...', max=10, suffix='%(percent)d%%') as bar:
        for _, result in enumerate(papers, 1):
            slashs = [m.start() for m in re.finditer('/', result.entry_id)]
            paper_id = result.entry_id[slashs[-1]+1:]
            titles.append(result.title)
            urls.append(result.pdf_url)
            ids.append(paper_id)
            bar.next()

    return titles, urls, ids


def download_pdf(ids):
    print()
    print('Downloading papers..')

    with Bar('Processing...', max=10, suffix='%(percent)d%%') as bar:
        for idx, paper_id in enumerate(ids, 1):
            paper = next(arxiv.Search(id_list=[paper_id]).results())
            paper.download_pdf(dirpath='./pdfs', filename=f'paper{idx}.pdf')
            bar.next()
