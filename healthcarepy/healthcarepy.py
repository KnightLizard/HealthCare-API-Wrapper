import requests
import json

class HealthCarePY:
    def __init__(self):

        self.base_url = "https://data.healthcare.gov/api/1/"
        self.__format = "JSON"

    ##METADATA METHODS##
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
    
    def get_metadata_schema(self, schema_name='dataset'):
        """
        Returns a metadata schema.
        """
        url = self.base_url + f"metastore/schemas/{schema_name}"

        res = requests.get(url)
        data = res.json()

        return data
    
    def get_metadata_schema_items(self, schema_name='dataset'):
        """
        Returns a list of metadata schema items.
        """
        url = self.base_url + f"metastore/schemas/{schema_name}/items"

        res = requests.get(url)
        data = res.json()

        return data
    
    def get_metadata_schema_item_identifiers(self, schema_name='dataset', show_reference_ids=False):
        """
        Returns a list of metadata schema item identifiers.
        """
        call_string = f"metastore/schemas/{schema_name}?show_reference_ids={show_reference_ids}"
        url = self.base_url + call_string

        res = requests.get(url)
        data = res.json()

        return data
    
    def get_datastore_stats(self):
        pass

    ##QUERY METHODS##

    ##PRIVATE CLASS METHODS##
    def __repr__(self):
        """
        Returns a string representation of the object.
        """

        return "<HealthCare API Client>"
    

hcpy = HealthCarePY()

print(hcpy.get_metadata_schema_item_identifiers())