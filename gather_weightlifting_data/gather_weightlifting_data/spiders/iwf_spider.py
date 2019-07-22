import csv
import json
import os

import scrapy


class IWFSpider(scrapy.Spider):
    name = "iwf"
    start_urls = [
        'https://www.iwf.net/new_bw/results_by_events/?event_year=2018',
        'https://www.iwf.net/results/results-by-events/?event_year=1998'
    ]

    def parse(self, response):
        """ Pull html info from the events page for each calendar year, follow links to each event, and go to next
            calendar year
        """
        # follow links to each event within the calendar year
        for a in response.css('td:nth-child(1) a'):
            yield response.follow(a, callback=self.parse_event)

        # go to next year's events
        for a in response.css('#next_year a'):
            yield response.follow(a, callback=self.parse)

    def parse_event(self, response):
        """ Pull html info from each individual event page """
        # go to the url that contains the actual meet result data
        for src in response.css('iframe::attr(src)'):
            yield response.follow(src, callback=self.parse_result)

    def parse_result(self, response):
        """ Extract meet result data, which is stored as part of the html file """
        data = json.loads(response.css('textarea::text').get().strip())  # data is a list of dicts
        filename = "all_data.csv"
        no_header = False  # default situation, no need to write extra header
        if not os.path.exists(filename):
            no_header = True
        with open(filename, 'a') as csvfile:
            fieldnames = ['gender', 'rank', 'rank_s', 'rank_cj', 'name', 'born', 'nation',
                          'category', 'bweight', 'snatch1', 'snatch2', 'snatch3', 'snatch',
                          'jerk1', 'jerk2', 'jerk3', 'jerk', 'total', 'event', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            if no_header:
                writer.writeheader()
            for d in data:
                writer.writerow(d)
