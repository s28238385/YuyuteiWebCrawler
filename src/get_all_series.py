import requests
from bs4 import BeautifulSoup


class GetAllSeries:
    def __init__(self, url):
        self.url = url
        self.series_links = []

    def get_all_sereies_links(self):
        class_name = "accordion-button opened"
        response = requests.get(url=self.url)
        soup = BeautifulSoup(response.text, 'html5lib')
        links = soup.find_all('button', class_=class_name)
        for i in links:
            if 'onclick' in i.attrs:
                self.string_modify(i)
        
        unique_data = list({tuple(d.items()) for d in self.series_links})
        unique_data = [dict(item) for item in unique_data]
        return unique_data

    def string_modify(self, s):
        if 'sell' in s['onclick']:
            series_link_info = {}
            s_split = s['onclick'].split('\'')
            series_name = s.string
            series_link_info['name'] = series_name
            series_link_info['link'] = s_split[1]
            self.series_links.append(series_link_info)
