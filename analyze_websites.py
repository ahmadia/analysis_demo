#!/usr/bin/env python
'''Analysis of word count in websites'''

import sys
import re
import urllib2
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

import websites

def get_counts(html):
    words = re.findall('\w+', html.lower())
    return Counter(words)

def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()

def simple_bar(data, labels, title):
    xrange = np.arange(1, len(data) + 1)
    width = 0.8
    ax = plt.subplot(111)
    plt.title(title)
    ax.bar(xrange, data, width=width)
    ax.set_xticks(xrange + width/2)
    ax.set_xticklabels(labels, rotation=45)

# needed for *both* import and 
# python analyze_websites.py to work
if __name__ == '__main__':
    websites_file = sys.argv[1]
    if len(sys.argv) > 2:
        search_term = sys.argv[2]
    else:
        search_term = 'basketball'
    sites = websites.read(websites_file)
    data = []
    labels = []
    for site, url in sites.iteritems():
        html = get_html(url)
        counts = get_counts(html)
        data.append(counts[search_term])
        labels.append(site)
    title = "Occurence of word '" + search_term + "' on major news sites"
    simple_bar(data, labels, title)
    plt.savefig('analysis.png')