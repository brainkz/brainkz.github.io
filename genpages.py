import csv
from yaml import load, dump, Loader, Dumper
from requests.structures import CaseInsensitiveDict as CID
from boiler_plate import HOME, HEADER, BODY_HEADER, NAVBAR, FOOTER, \
JOURNALS, CONFERENCES, JC, PLAIN_NAMES, FANCY_NAMES, MONTHS, ADDRESS, BIO
from datetime import date
import os

TODAY = date.today()
CURRENT_YEAR = TODAY.year
CURRENT_MONTH = TODAY.month

def format(key, entry, is_journal):
    print(key)
    bib_authors = [PLAIN_NAMES[a] for a in entry['authors']]
    *all, last = [FANCY_NAMES[a] for a in entry['authors']]
    comma_and = ', and ' if len(all) > 2 else ' and '
    ieee_str = ', '.join(all) + comma_and + last + ', '

    bib_str =   '@article{' + f'bairamkulov_{key},\n' + \
                'author = "' + ' and '.join(bib_authors) + '",\n'

    ieee_str += '"' + entry["title"] + '," '
    book = JC[entry['book']]
    ieee_str += f"<i>{book}</i>"
    if is_journal:
        book_key = 'journal'
    else:
        book_key = 'booktitle'
    bib_str += f'{book_key} = "' + book + '",\n'
    if not entry.get('published', True):
        ieee_str += " (in press)."
        bib_str += 'title = "' + entry["title"] + ' \\textup{(in press)}",'
        return ieee_str, bib_str.replace('\n','<br>&emsp;') + '<br>}'
    else:
        bib_str += 'title = "' + entry["title"] + '",\n'
        ieee_str += ", "
    vol = entry.get('vol', '')
    num = entry.get('num', '')
    pp  = entry.get('pp', None)
    if vol:
        ieee_str += f"Vol. {vol}, "
        bib_str += f'volume = "{vol}",\n'
    if num:
        ieee_str += f"No. {num}, "
        bib_str += f'number = "{num}",\n'
    if isinstance(pp, int):
        ieee_str += f"p. {pp}, "
        bib_str += f'pages = "{pp}",\n'
    elif isinstance(pp, list):
        assert(len(pp) == 2)
        ieee_str += f"pp. {pp[0]}&ndash;{pp[1]}, "
        bib_str += f'pages = "{pp[0]}--{pp[1]}",\n'
    month = MONTHS[entry['month']]
    year = entry['year']
    ieee_str += f"{month} {year}."
    bib_str += f'month = "{month}",\nyear = "{year}",\n'
    doi = entry["doi"]
    bib_str += f'doi = "{doi}",'
    return ieee_str, bib_str.replace('\n','<br>&emsp;') + '<br>}'

def format_entry(ieee_str, bib_str, entry):
    return '<p>\n' + ieee_str + '\n<details>\n<summary>\n<u>Bibtex</u>\n<a href="' + entry['pdf'] + '">PDF</a> <a href="https://doi.org/' + entry['doi'] + '">Publisher</a>\n</summary>\n<span>' + bib_str + '\n</span>\n</details>\n</p>'

def format_list(file):
    with open(file) as f:
        data = load(f, Loader=Loader)
    jrnl = {}
    conf = {}
    for key, d in data.items():
        year = d.get('year',CURRENT_YEAR)
        month = d.get('month',CURRENT_MONTH)
        if d['book'] in JOURNALS:
            ieee, bib = format(key, d, True)
            formatted_entry = format_entry(ieee, bib, d)
            jrnl[formatted_entry] = year*12+month
        elif d['book'] in CONFERENCES:
            ieee, bib = format(key, d, False)
            formatted_entry = format_entry(ieee, bib, d)
            conf[formatted_entry] = year*12+month
    jrnl_str = '<h2>Journal articles</h2>\n'  + '\n'.join(sorted(jrnl, reverse=True, key=jrnl.get))
    conf_str = '<h2>Conference papers</h2>\n' + '\n'.join(sorted(conf, reverse=True, key=conf.get))
    return jrnl_str, conf_str

def make_pub(home=HOME):
    jrnl_str, conf_str = format_list('papers/Paper_Config.yml')
    with open(os.path.join(HOME,'pub.html'),'w') as f:
        f.write(HEADER)
        f.write(NAVBAR)
        f.write(BODY_HEADER)
        f.write(jrnl_str)
        f.write(conf_str)
        f.write(FOOTER)

def make_index(home=HOME):
    with open(os.path.join(HOME,'index.html'),'w') as f:
        f.write(HEADER)
        f.write(NAVBAR)
        f.write(BODY_HEADER)
        f.write(ADDRESS)
        f.write(FOOTER)

if __name__ == '__main__':
    make_pub()
    make_index()
