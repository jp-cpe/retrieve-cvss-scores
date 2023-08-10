#!/usr/bin/env python3

import requests
import time
from bs4 import BeautifulSoup
import os

# Add your OpenCVE API credentials here
OPENCVE_USERNAME = os.environ.get('OPENCVE_USERNAME')
OPENCVE_PASSWORD = os.environ.get('OPENCVE_PASSWORD')

def scrape_cve_from_webpage(url):
    cve_set = set()  # Using a set to store CVEs and automatically avoid duplicates
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the webpage. Status code: {response.status_code}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        for paragraph in soup.find_all('p'):
            if 'CVE' in paragraph.text:
                cve_list = [cve.strip() for cve in paragraph.text.split() if 'CVE-' in cve and 'CVE-ID' not in cve]
                cve_set.update(cve_list)
        
        # Remove colon from each CVE value
        cve_set = {cve.replace(':', '') for cve in cve_set}
        
        # Print the count of CVEs found on the webpage
        print(f"Number of CVEs found on the webpage: {len(cve_set)}")
        
        # Print the cve_set within the function
        print("CVEs found on the webpage:")
        print(cve_set)

        return list(cve_set)
    
    except Exception as e:
        print(f"Error occurred while scraping: {e}")
        return None

def get_opencve_data(cve_list):
    opencve_data = {}
    base_url = "https://www.opencve.io/api/cve/"
    
    try:
        for cve in cve_list:
            api_url = f"{base_url}{cve}"
            
            response = requests.get(api_url, auth=(OPENCVE_USERNAME, OPENCVE_PASSWORD))
            if response.status_code == 200:
                data = response.json()
                opencve_data[cve] = data
            else:
                print(f"Failed to fetch OpenCVE data for CVE: {cve}. Status code: {response.status_code}")
            
            # Adding a delay to avoid overwhelming the API
            time.sleep(2)

        return opencve_data
    
    except Exception as e:
        print(f"Error occurred while fetching OpenCVE data: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL to scrape for CVEs: ")
    
    cve_list = scrape_cve_from_webpage(url)
    if cve_list:
        opencve_data = get_opencve_data(cve_list)
        print("OpenCVE data for CVEs:")
        for cve, data in opencve_data.items():
            print(f"CVSS v3 for CVE {cve}: {data['cvss']['v3']}")
        
        num_cves_with_scores = sum(1 for cve in opencve_data.values() if cve['cvss']['v3'] != "N/A")
        num_cves_without_scores = len(opencve_data) - num_cves_with_scores

        print(f"\nNumber of CVEs with scores: {num_cves_with_scores}")
        print(f"Number of CVEs without scores: {num_cves_without_scores}")

        highest_score_cve = max(opencve_data, key=lambda cve: float(opencve_data[cve]['cvss']['v3']) if opencve_data[cve]['cvss']['v3'] != "N/A" else 0)
        highest_score = opencve_data[highest_score_cve]['cvss']['v3']

        print(f"\nCVE with the highest CVSS v3 score: {highest_score_cve}")
        print(f"Highest CVSS v3 score: {highest_score}")

        if highest_score == "N/A":
            print("Qualitative rating: No score available")
        elif float(highest_score) >= 9.0:
            print("Qualitative rating: Critical")
        elif 7.0 <= float(highest_score) < 9.0:
            print("Qualitative rating: High")
        elif 4.0 <= float(highest_score) < 7.0:
            print("Qualitative rating: Medium")
        else:
            print("Qualitative rating: Low")
    else:
        print("No CVEs found on the webpage.")
