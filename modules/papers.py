import arxiv
import re
from progress.bar import Bar
import os
from time import time


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

    with open('keyword.txt', 'w') as f:
        f.write(keyword)

    papers = fetch_results(amount, keyword)
    ids = []

    with Bar('Processing...', max=int(amount), suffix='%(percent)d%%') as bar:
        for _, result in enumerate(papers, 1):
            slashs = [m.start() for m in re.finditer('/', result.entry_id)]
            paper_id = result.entry_id[slashs[-1]+1:]
            ids.append(paper_id)
            bar.next()

    return ids


def download_pdf(ids, dir):
    start_time = time()
    print()
    print('Downloading papers..')

    with Bar('Processing...', max=len(ids), suffix='%(percent)d%%') as bar:
        for _, paper_id in enumerate(ids, 1):
            paper = next(arxiv.Search(id_list=[paper_id]).results())
            paper.download_pdf(dirpath=dir)
            bar.next()

    print(f'Time spent: {round(time()-start_time, 2)}s')
