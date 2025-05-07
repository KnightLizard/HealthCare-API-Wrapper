import requests
import json

class HealthCarePY:
    def __init__(self):
        self.base_url = "https://data.healthcare.gov/api/1/"

    def search(self, search_text, page=None, page_size=None, ):
        """
        Returns a list of search results for the given search term.
        """

        url = self.base_url + "search?fulltext=\"" + search_text + "\""
        return requests.get(url).json()
    
    def get_metadata_schemas_list(self):
        """
        Returns a list of metadata schemas.
        """
        url = self.base_url + "metastore/schemas"

        res = requests.get(url)
        data = res.json()

        return list(data.keys())

    def __repr__(self):
        """
        Returns a string representation of the object.
        """

        return "<HealthCare API Client>"