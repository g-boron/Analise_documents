import arxiv
import re
from progress.bar import Bar
import os


def fetch_results(amount, keyword):
    search = arxiv.Search(
    query = keyword,
    max_results = int(amount),
    sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search.results()


def collect_data(amount, keyword):
    print()
    print('Collecting data..')

    papers = fetch_results(amount, keyword)
    titles = []
    urls = []
    ids = []

    with Bar('Processing...', max=int(amount), suffix='%(percent)d%%') as bar:
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

    #max=len([entry for entry in os.listdir('./pdfs/') if os.path.isfile(os.path.join('./pdfs/', entry))])
    with Bar('Processing...', max=len(ids), suffix='%(percent)d%%') as bar:
        for idx, paper_id in enumerate(ids, 1):
            paper = next(arxiv.Search(id_list=[paper_id]).results())
            paper.download_pdf(dirpath='./pdfs', filename=f'paper{idx}.pdf')
            bar.next()
