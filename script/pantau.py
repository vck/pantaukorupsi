#!/usr/bin/python

__author__ = 'vickydasta'

from urllib2 import urlopen
import lxml.html

host = 'http://www.pekanbaruexpress.com/korupsi.html'

def geturl():
    '''
    parser url bersentimen korupsi
    '''

    try:
        html_data = urlopen(host).read()
    except:
        raise Exception('something were wrong...')

    parser = lxml.html.fromstring(html_data)

    urls = []

    for url in parser.xpath('//a/@href'):
        if 'korupsi' in url:
            urls.append(url.split('/'))

    clean = []

    for item in urls:
        clean.append(item[-1])

    url_ = []
    for i in range(len(clean)):
        if i > 2:
            url_.append(clean[i])

    return url_

def newtitle(url):
    form = url.split('-') # deform url form
    id = int(form[0]) # get news id
    form.pop(0) # remove id
    # rm html
    title = ' '.join(form) # join all words
    return {id:title}

def getdata():
    return [newtitle(url) for url in geturl()]
