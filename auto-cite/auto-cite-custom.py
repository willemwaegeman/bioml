from scholarly import scholarly
from tqdm import tqdm
import json
import os

def get_publications_by_name(name):
    """Fetch publications by researcher name."""
    search_query = scholarly.search_author(name)
    try:
        author = next(search_query)
        pubs = scholarly.fill(author)['publications']
        return pubs
    except StopIteration:
        print(f"No author found with name: {name}")
        return []

def get_detailed_info(pub):
    """Fetch detailed information for a publication to get co-authors."""
    detailed_pub = scholarly.fill(pub)
    # pub['coauthors'] = [coauthor['name'] for coauthor in detailed_pub['coauthors']]
    return detailed_pub

def read_from_json(filename):
    """Read data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Problem with accessing json file')
        print('The current directory is: '+str(os.getcwd()))
        return []

def save_to_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def pubs_equal(pub_a, pub_b):
    keys_to_compare_on = set(pub_a.keys()).intersection(set(pub_b.keys()))
    for k in keys_to_compare_on:
        if pub_a[k] != pub_b[k]:
            return False
    return True

def update_publications(researcher_name, filename="publications.json"):
    # Read existing publications from the file
    print('Loading publications... ', end='')
    existing_pubs = read_from_json(filename)
    print('Done ('+str(len(existing_pubs))+' found)')

    # Fetch the latest publications using scholarly
    print('Loading publications from Google scholar... ', end='')
    new_pubs = get_publications_by_name(researcher_name)
    print('Done ('+str(len(new_pubs))+' found)')

    # Identify new publications by comparing bib entries
    existing_bibs = [pub['bib']['title'] for pub in existing_pubs]
    pubs_to_add = [pub for pub in new_pubs if pub['bib']['title'] not in existing_bibs]

    # For only the new publications, fetch detailed information to get co-authors
    print('Found '+str(len(pubs_to_add))+' new publications. ',end='')
    enriched_pubs_to_add = []
    if len(pubs_to_add) != 0:
        print(' Extracting detailed info...')
        enriched_pubs_to_add = [get_detailed_info(pub) for pub in tqdm(pubs_to_add)]
        print('Done')
    # Combine existing and new publications
    if enriched_pubs_to_add:
        updated_pubs = existing_pubs + enriched_pubs_to_add
        # Save the combined list back to the JSON file
        save_to_json(updated_pubs, filename)

def main():
  # Tracking only Willem's publications. In a future version, the scholarly.search_author_id function can be used to pull publications from every PhD (though it makes sense that they only have publications with Willem as a co-author)
  # Dimitris: j2T4koYAAAAJ
  # Gaetan: FyaHiDAAAAAJ
  # Natan: 
  # Mira: 
  # Lauren: 
  # Thomas: FLlm6dQAAAAJ
  # Nicolas: tY98NeQAAAAJ
  researcher_name = 'Willem Waegeman'
  update_publications(researcher_name, filename="_data/publications.json")

if __name__ == "__main__":
    main()
