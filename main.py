import arxiv


def fetch_results():
    search = arxiv.Search(
    query = "artificial intelligence",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )

    return search.results()
