import json
import datetime
import time
import sys
import requests

def check_url(url: str) -> int:
    """
    Returns status code of url

    -> url
    """
    try:
        headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        r = requests.get(url, stream=True, headers=headers)
    except:
        return 404
    return r.status_code

def dossier_valid(dossier: dict, dossiernr: int) -> tuple:
    """
    Checks if a dossier passes some basic checks.
    """

    errors = []
    valid_check = json.load(open('valid_scheme.json'))
    valid_publishers = json.load(open('publishers.json'))

    # Check required
    for attr in valid_check['generic_required_attributes']:
        if attr not in dossier:
            errors.append(f"Error in dossier {dossiernr}: please provide a '{attr}' for every dossier!")

    if 'dc_type' in dossier:

        if dossier['dc_type'] not in valid_check['dossier_valid_types']:
            errors.append(f"Error in dossier {dossiernr}: unknown/unsupported dossier type {dossier['dc_type']}!")

    # Check if publisher exists
    if 'dc_publisher' in dossier:

        publisher_codes = [publisher['dc_publisher'] for publisher in valid_publishers]
        if dossier['dc_publisher'] not in publisher_codes:
            errors.append(f"Error in dossier {dossiernr}: unknown/unsupported publisher {dossier['dc_publisher']}!")

    # Check for a date
    if 'dc_date_year' not in dossier and 'foi_requestDate' not in dossier and 'foi_decisionDate' not in dossier and 'foi_publishedDate' not in dossier:
        errors.append(f"Error in dossier {dossiernr}: please provide at least a 'dc_date_year' for every dossier!")

    # Check if attributes are valid
    for attr in dossier:

        if attr not in valid_check['generic_valid_attributes']:
            
            if dossier['dc_type'] in valid_check['dossier_valid_types']:
                if attr not in valid_check[f'{dossier["dc_type"]}_valid_attributes']:
                    errors.append(f"Error in dossier {dossiernr}: '{attr}' is not a valid attribute for a dossier of type {dossier['dc_type']}!")

    # Document attributes
    if 'foi_files' in dossier:

        if 'foi_documenten' in dossier['foi_files']:
            for i, bijlage in enumerate(dossier['foi_files']['foi_documenten'], start=1):

                # Check required
                for attr in valid_check['document_required_attributes']:
                    if attr not in bijlage:
                        errors.append(f"Error in dossier {dossiernr} - document {i}: please provide a '{attr}' for every document!")
                
                # Check if valid
                for attr in bijlage:
                    if attr not in valid_check['document_valid_attributes']:
                        errors.append(f"Error in dossier {dossiernr} - document {i}: '{attr}' is not a valid attribute for an attached document!")

                # Source is required
                if 'dc_source' in bijlage and dossier['dc_type'] != '1e-i':
                    # Check accesibility of url
                    status = check_url(bijlage['dc_source'])
                    while status == 429:
                        time.sleep(20)
                        status = check_url(bijlage['dc_source'])
                    if status >= 400:
                        errors.append( f"Error in dossier {dossiernr} - document {i}: {bijlage['dc_source']} is not accessible (HTTP-status = {status})!")

    # Check date formats
    dates = ['foi_requestDate', 'foi_decisionDate', 'foi_publishedDate']
    for date_attr in dates:
        if date_attr in dossier:
            try: 
                # datetime.date.fromisoformat(dossier[date_attr])
                datetime.datetime.strptime(dossier[date_attr], "%Y-%m-%d")
            except:
                errors.append(f"""Error in dossier {dossiernr}: '{date_attr}' ('{dossier[date_attr]}') is not in the right format (right format: YYYY-MM-DD)""")

    return (len(errors) == 0, errors)

if __name__ == "__main__":

    file_to_check = sys.argv[1]
    dossiers = json.load(open(file_to_check))
    if isinstance(dossiers, dict):
        dossiers = [dossiers]

    for i, dossier in enumerate(dossiers, start=1):
        valid, errors = dossier_valid(dossier, 1)

        if not valid:
            print(f"Errors in dossier {i}:")
            for error in errors:
                print(error)
        else:
            print(f"Dossier {i} is valid!")
