#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup


# get: HTTP GET
def get_text(url):
    return requests.get(url).text


def parse_to_url_gen(text):
    # soup is bs4.BeautifulSoup
    # a_tag is bs4.element.Tag
    soup = BeautifulSoup(text, 'html.parser')
    return (a_tag.get('href', '') for a_tag in soup.find_all('a'))


# it: iterator
def keep_external_url_gen(url_it):
    for url in url_it:
        if url.startswith('http'):
            yield url


count = 0


def inc_count():
    global count
    count += 1
    return count


if __name__ == '__main__':

    print('Testing get_text ...', end=' ')
    text = get_text('https://tw.pycon.org')
    print(repr(text[:40]))

    print('Testing parse_to_url_gen ...', end=' ')
    url_gen = parse_to_url_gen(text)
    print(repr(list(url_gen)[:3]))

    print('Testing keep_external_url_gen ...')
    urls = [
        '/2017/en-us',
        'https://www.facebook.com/pycontw'
    ]
    assert list(keep_external_url_gen(urls)) == \
        ['https://www.facebook.com/pycontw']

    print('Testing inc_counter ...')
    assert inc_count() == 1
    assert inc_count() == 2
