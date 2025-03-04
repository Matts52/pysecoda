from .pysecoda import PySecoda
from pprint import pprint

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

if __name__ == "__main__":
    api = PySecoda(API_KEY)

    tables = api.tables.get_tables()
    print("Fetching data...")
    pprint(tables)

    #pprint(api.tags.get_user_by_id('18eb02a4-85ca-4594-8244-bbcf2571ec65'))

    #print("Creating a new tag...")
    #new_tag = api.tags.create_tag("Random Tag", "Indicates urgent items", "#FF0000")
    #pprint(new_tag)
    
    #tag_id = new_tag.get("id")
    #tag_id = '8b573e62-4a7e-45f6-a7b2-38a43b24a0f3'

    #if tag_id:
        #print("Updating the tag...")
        #updated_tag = api.tags.update_tag(tag_id, color="#FFA500")
        #pprint(updated_tag)
        
        #print("Deleting the tag...")
        #delete_response = api.tags.delete_tag(tag_id)
