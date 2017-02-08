import csv
from urllib.parse import urlparse, parse_qs
from pathlib import Path

CONVERT_EVENT_PARAMS = {'conv', 'prog', 'cvt', 'vfbc', 'isize', 'ibr', 'vq', 'vdur', 'cpd', 'osize', 'obr', 'pd', 'v'}
urls = 'urls_frommkv.txt'
CSV_FILE = 'urls_frommkv.csv'

def get_query_params(url, params=None):
    query = parse_qs(urlparse(url).query)
    if params:
        return {k:v for k, v in query.items() if k in params}
    else:
        return query

def urlqs2csv(urls, csvfile, params=None):

    urls_file = Path(urls)
    url_params = [get_query_params(url, params) for url in urls_file.open()]

    with open(csvfile, 'w') as f:
        if params:
            fieldnames = params
        else:
            fieldnames = url_params[0].keys()
        writer = csv.DictWriter(f, dialect='excel', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(url_params)

if __name__ == "__main__":
    # execute only if run as a script
    urlqs2csv(urls, CSV_FILE, CONVERT_EVENT_PARAMS)