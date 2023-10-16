import csv
from yaml import load, dump, Loader, Dumper
from requests.structures import CaseInsensitiveDict as CID
from boiler_plate import HOME, HEADER, BODY_HEADER, NAVBAR, FOOTER, SKIP, JOURNALS,\
CONFERENCES, JC, PLAIN_NAMES, FANCY_NAMES, MONTHS, ADDRESS, BIO, \
PRESENTATIONS, DISSERTATION, WELCOME, make_header
from datetime import date
import os

TODAY = date.today()
CURRENT_YEAR = TODAY.year
CURRENT_MONTH = TODAY.month

def format_journal_conf(key, entry, is_journal):
    print(key)
    bib_authors = [PLAIN_NAMES[a] for a in entry['authors']]
    *all, last = [FANCY_NAMES[a] for a in entry['authors']]
    comma_and = ', and ' if len(all) > 2 else ' and '
    ieee_str = ', '.join(all) + comma_and + last + ', '
    if is_journal:
        bib_key = '@article'
        book_key = 'journal'
    else:
        bib_key = '@inproceedings'
        book_key = 'booktitle'

    bib_str =   bib_key + '{' + f'bairamkulov_{key},\n' + \
                'author = "' + ' and '.join(bib_authors) + '",\n'

    ieee_str += '"' + entry["title"] + '," '
    book = JC[entry['book']]
    
    doi = entry["doi"]
    if not doi:
        book = f"To appear in {book}"
    else:
        bib_str += f'doi = "{doi}",\n'
    
    ieee_str += f"<i>{book}</i>"
    bib_str += f'{book_key} = "' + book + '",\n'
    if not entry.get('published', True):
        ieee_str += " (in press)."
        bib_str += 'title = "' + entry["title"] + ' \\textup{(in press)}",'
        return ieee_str, bib_str.replace('\n','<br>&emsp;') + '<br>}'
    else:
        bib_str += 'title = "' + entry["title"] + '",\n'
        ieee_str += ", "
    year = entry['year']
    ieee_str += f"{year}."
    bib_str += f'year = "{year}",\n'
    print(ieee_str)
    print(bib_str.replace('\n','<br>&emsp;') + '<br>}')
    return ieee_str, bib_str.replace('\n','<br>&emsp;') + '<br>}'


def format_book(key, entry):
    print(key)
    bib_authors = [PLAIN_NAMES[a] for a in entry['authors']]
    *all, last = [FANCY_NAMES[a] for a in entry['authors']]
    comma_and = ', and ' if len(all) > 2 else ' and '
    ieee_str = ', '.join(all) + comma_and + last + ', '
    bib_key = '@book'
    book_key = 'publisher'
    book = JC[entry[book_key]]

    bib_str =   bib_key + '{' + f'bairamkulov_{key},\n' + \
                'author = "' + ' and '.join(bib_authors) + '",\n'

    ieee_str += '"' + entry["title"] + '," '
    ieee_str += f"<i>{book}</i>"
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
    year = entry['year']
    ieee_str += f"{year}."
    bib_str += f'year = "{year}",\n'
    isbn = entry["isbn"]
    ieee_str += f" ISBN # {isbn}."
    bib_str += f'isbn = "{isbn}",'
    return ieee_str, bib_str.replace('\n','<br>&emsp;') + '<br>}'

def format_entry(ieee_str, bib_str, entry):
    link = entry.get('url', f"https://doi.org/{entry.get('doi')}")
    if 'pdf' in entry:
        pdf_link = entry['pdf']
        return '<p>\n' + ieee_str + f'\n<details>\n<summary>\n<u>Bibtex</u> <a href="{link}">Publisher</a> <a href="{pdf_link}">PDF</a>\n</summary>\n<span>' + bib_str + '\n</span>\n</details>\n</p>'
    else:
        return '<p>\n' + ieee_str + f'\n<details>\n<summary>\n<u>Bibtex</u> <a href="{link}">Publisher</a>\n</summary>\n<span>' + bib_str + '\n</span>\n</details>\n</p>'

def format_list(file):
    with open(file) as f:
        data = load(f, Loader=Loader)
    jrnl = {}
    conf = {}
    book = {}
    for key, d in data.items():
        year = d.get('year', CURRENT_YEAR)
        month = d.get('month',CURRENT_MONTH)
        if d['type'] == 'journal':
            ieee, bib = format_journal_conf(key, d, True)
            formatted_entry = format_entry(ieee, bib, d)
            jrnl[formatted_entry] = year*12+month
        elif d['type'] == 'conf':
            ieee, bib = format_journal_conf(key, d, False)
            formatted_entry = format_entry(ieee, bib, d)
            conf[formatted_entry] = year*12+month
        elif d['type'] == 'book':
            ieee, bib = format_book(key, d)
            formatted_entry = format_entry(ieee, bib, d)
            book[formatted_entry] = year*12+month
    book_str = '<h2 id="book">Authored Book</h2>\n'  + '\n'.join(sorted(book, reverse=True, key=book.get))
    jrnl_str = '<h2 id="journal">Journal articles</h2>\n'  + '\n'.join(sorted(jrnl, reverse=True, key=jrnl.get))
    conf_str = '<h2 id="conference">Conference papers </h2><a href=#up>Return to top</a>\n' + '\n'.join(sorted(conf, reverse=True, key=conf.get))
    return book_str, jrnl_str, conf_str

def make_pub(home=HOME):
    book_str, jrnl_str, conf_str = format_list('papers/Paper_Config.yml')
    with open(os.path.join(HOME,'pub.html'),'w') as f:
        f.write(make_header("Publications"))
        f.write(NAVBAR)
        f.write(BODY_HEADER)
        f.write(SKIP)
        f.write(book_str)
        f.write(jrnl_str)
        f.write(conf_str)
        f.write(PRESENTATIONS)
        f.write(DISSERTATION)
        f.write(FOOTER)

def make_index(home=HOME):
    with open(os.path.join(HOME,'index.html'),'w') as f:
        f.write(make_header("Homepage"))
        f.write(NAVBAR)
        f.write(BODY_HEADER)
        f.write(WELCOME)
        f.write(ADDRESS)
        f.write(FOOTER)

if __name__ == '__main__':
    make_pub()
    make_index()
