#!/usr/bin/python

import urllib2
import json
from counthd import count_hd


def main():
    # Initialize variables
    more = True
    page_number = 1
    total_hd_true = 0
    total_hd_false = 0

    # Loop till more is False
    while more:
        print("Processing Page {0}".format(page_number))

        # Form URL string
        url = r"http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page={0}".format(page_number)

        # Get JSON object    
        try:
            url_request = urllib2.Request(url, headers={'User-Agent' : "My Browser"})        
            url_response = urllib2.urlopen(url_request)
            data = json.load(url_response)
        except:
            print("Problem with loading Page {0}".format(page_number))
            page_number += 1
            continue
                    
        # Get 'more' value
        more = data["more"]

        # Get array of 'response'
        responses = data["response"]
        hd_true, hd_false = count_hd(responses)
        total_hd_true += hd_true
        total_hd_false += hd_false

        # Go to next page
        page_number += 1

    print("There are {0} HD True and {1} HD False.".format(total_hd_true, total_hd_false))

if __name__ == '__main__':
    main()
