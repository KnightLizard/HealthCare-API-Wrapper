import requests
import json

##To-Do:##
##Error Code Exception Handling##
##Create Additional Classes for CMS, Public Payment Data, and Medicaid Data APIs##

class HealthCarePY:
    def __init__(self):

        base_url = "https://data.healthcare.gov/api/1/"
        page_size = 100 #Maximum page size supported by API

        search_url = base_url + f"search"
        response = requests.get(search_url)

        num_results = int(response.json()['total'])
        iterations = num_results // page_size + (num_results % page_size > 0)

        def dataset_metadata_handling(response_json, key, item):
            """
            Helper function for __init__ method
            """
            try:
                return response_json[key][item]
            except KeyError:
                return None


        self.datasets = []
        self.searchable_keywords = []
        for i in range(iterations):
            search_url = base_url + f"search?page={i+1}&page_size={page_size}"
            response = requests.get(search_url)

            response_json = response.json()['results']
            
            for result in response_json.keys():
                self.searchable_keywords.extend(response_json[result]['keyword'])
                self.datasets.append({
                    "dataset": result,
                    "title": dataset_metadata_handling(response_json, result, 'title'),
                    "description": dataset_metadata_handling(response_json, result, 'description'),
                    "issue date": dataset_metadata_handling(response_json, result, 'issued'),
                    "modified date": dataset_metadata_handling(response_json, result, 'modified')
                })
            
        self.searchable_keywords = list(set(self.searchable_keywords)).sort()

    def get_searchable_keywords(self):
        return self.searchable_keywords

    ##METADATA METHODS##
    def search(self, search_text, page=None, page_size=None):
        """
        Returns a list of search results for the given search term.
        """
        ##To-Do:##
        ##Add page and page_size parameters##
        ##Add sort_by parameter##
        ##Add sort_order parameter##
        ##Init Object to store search able keywords and available database metadata upon class init##

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
def print_json_tree(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + str(key))
            print_json_tree(value, indent + 1)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print('  ' * indent + str(i))
            print_json_tree(item, indent + 1)
    else:
        print('  ' * indent + str(data))

hcpy = HealthCarePY()
print_json_tree(hcpy.search('Brokers'))