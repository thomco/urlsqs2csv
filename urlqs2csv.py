import csv
from urllib.parse import urlparse, parse_qs
from pathlib import Path

CONVERT_EVENT_PARAMS = {'conv', 'cvt', 'prog', 'vdur', 'vfbc', 'cpd', 'vq', 'isize', 'osize', 'ibr', 'obr', 'pd', 'v'}

URLS = [r'http://cache-download.real.com/free/windows/mrkt/log.txt?cvt=1&isize=3&osize=3&prog=100&st=0&vdur=3&vq=96&conv=success&cpd=3GP%20(older%20cell%20phones)&ibr=0.1&obr=0.0&vfbc=3gp_avc_aac&dc=T10HEAD&la=en&ld=1486503804&o=10.0.14393|SP0|en&oc=T10HEAD&od=1486503804&pd=realplayerconverter&rv=1.1&v=18.1.7.220&ustype=notsignedin&u=c13a79e175324a2fbad7bbcdc519136f&m=0a1bb8f1ed7e11e6e0792702eac5163d&d=ddec8721f8db629c8c6b8142bd370907\n',
 r'http://cache-download.real.com/free/windows/mrkt/log.txt?cvt=1&isize=3&osize=3&prog=100&st=0&vdur=3&vq=0&conv=success&cpd=AAC%20(Apple%20devices)&ibr=0.0&obr=0.0&vfbc=3gp_avc_aac&dc=T10HEAD&la=en&ld=1486503804&o=10.0.14393|SP0|en&oc=T10HEAD&od=1486503804&pd=realplayerconverter&rv=1.1&v=18.1.7.220&ustype=notsignedin&u=c13a79e175324a2fbad7bbcdc519136f&m=0a1bb8f1ed7e11e6e0792702eac5163d&d=ddec8721f8db629c8c6b8142bd370907\n',
]

def get_query_params(url, params=None):
    query = parse_qs(urlparse(url).query)
    if params:
        return {k:v for k, v in query.items() if k in params}
    else:
        return query

def main(filename, urls, params=None):
    url_params = [get_query_params(url, params) for url in urls]
    with open(filename, 'w') as csvfile:
        fieldnames = url_params[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(url_params)

if __name__ == "__main__":
    # execute only if run as a script
    main('test.csv', URLS, CONVERT_EVENT_PARAMS)