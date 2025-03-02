from .pysecoda import PySecoda
from pprint import pprint

if __name__ == "__main__":
    api = PySecoda("API_KEY")

    print("Fetching groups...")
    groups = api.groups.get_groups()
    pprint(groups)
    
    #print("Creating a new tag...")
    #new_tag = api.create_tag("Urgent", "Indicates urgent items", "#FF0000")
    #pprint(new_tag)
    
    #tag_id = new_tag.get("id")
    #tag_id = '131e8267-e9ca-49b3-a7c5-861b22ce7da0'

    #if tag_id:
        #print("Updating the tag...")
        #updated_tag = api.update_tag(tag_id, color="#FFA500")
        #pprint(updated_tag)
        
        #print("Deleting the tag...")
        #delete_response = api.delete_tag(tag_id)
        #pprint(delete_response.text)
