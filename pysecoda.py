from .api_client import APIClient
from .endpoints.tags import TagsEndpoint
from .endpoints.groups import GroupsEndpoint

class PySecoda(APIClient):
    """
    An API wrapper for the Secoda platform API.
    """
    
    def __init__(self, api_key: str):
        """
        Initializes the Secoda API client.
        
        :param api_key: Bearer token for authentication.
        """
        super().__init__("https://api.secoda.co/", api_key)
        self.tags = TagsEndpoint(self)
        self.groups = GroupsEndpoint(self)
