import papers

if __name__ == '__main__':
    list_of_titles, list_of_urls, list_of_ids = papers.collect_data()
    papers.download_pdf(list_of_ids)
    