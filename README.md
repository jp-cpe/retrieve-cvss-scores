# retrieve-cvss-scores
Retrieve CVSS scores for each CVE-ID listed in Apple's security content documentation for OS updates.

# Project Description:
This script is designed to scrape CVE identifiers from a given webpage, fetch their CVSS v3 scores from the OpenCVE API, and then analyze and summarize the collected data. It outputs the CVSS v3 score for each CVE, counts of CVEs with and without scores, identifies the CVE with the highest score, and provides a qualitative rating for the highest score.

The script was designed specifically for retrieving CVSS scores for Apple updates by scraping the "about the security content of X update" support articles found on the Apple security releases details page: https://support.apple.com/en-us/HT201222. (Example URL for scraping: https://support.apple.com/en-us/HT213844.)

# Purpose:
The script was created to address the need for defining an SLA for macOS updates in accordance with the highest CVSS score addressed within the update.

Some organizations have a patching process that includes a timeline for completion that is based on the CVSS score of that update. Example: Updates with a CVSS score of "High" must have the patch process initiated within 1 week and the patch most be completed and operational within 30 calendar days of the patch release.

To determine the highest CVSS score addressed within a specific update an admin might have to manually go through the list of CVE-ID's addressed within the update and then check the CVSS score on a separate website. Furthermore, CVSS scores are not always assigned to CVE-ID's at the time that an update is released, meaning admins have to constantly go back and check CVE-ID's for their CVSS scores. This script can be used to quickly gather available CVSS scores instead of searching and scrolling and going back and forth on different webpages.

# Note: 
This method of assessing an update's criticality based solely on the highest CVSS score addressed by the update is not necessarily the best or most effective way of managing update deadlines. The risk of a vulnerability should always be assessed within the context of an environment. It can however, be used to help provide general guidance on the criticality of an update if CVSS scores are accepted as general guidance within an environment.

# Instructions for Use:
### Set up OpenCVE API credentials:
1. Obtain an OpenCVE username and password (https://www.opencve.io/welcome).
	○ Add these credentials as environment variables in your shell configuration file (e.g., .bashrc or .zshrc):
		
		    export OPENCVE_USERNAME="your_username"
		    export OPENCVE_PASSWORD="your_password"
		
	○ Restart your terminal or run 'source ~/.zshrc' to apply the changes.
3. Download and run the script:
	○ Download the script and save it as a .py file (e.g., retrieve-cvss-scores.py).
	○ Open a terminal and navigate to the directory containing the script.
	○ Run the script using the command: python3 retrieve-cvss-scores.py.
4. Follow the prompts:
	○ When prompted, enter the URL of the webpage you want to scrape for CVEs.
	○ The script will display the CVSS v3 scores for each CVE, count the number of CVEs with and without scores, 		identify the highest scoring CVE, and provide a qualitative rating.

# Example Output:
    Enter the URL to scrape for CVEs: https://support.apple.com/en-us/HT213844
    Number of CVEs found on the webpage: 35
    
    CVEs found on the webpage:
    {'CVE-2023-36495', 'CVE-2023-34241', 'CVE-2023-32441', 'CVE-2023-38565', 'CVE-2023-32443', 'CVE-2023-38603', 'CVE-2023-  38258', 'CVE-2023-32381', 'CVE-2023-38593', 'CVE-2023-38259', 'CVE-2023-32364', 'CVE-2023-38598', 'CVE-2023-28321', 'CVE-2023-36854', 'CVE-2023-34425', 'CVE-2023-2953', 'CVE-2023-38604', 'CVE-2023-35983', 'CVE-2023-32429', 'CVE-2023-38421', 'CVE-2023-38571', 'CVE-2023-35993', 'CVE-2023-28319', 'CVE-2023-32418', 'CVE-2023-38601', 'CVE-2023-32416', 'CVE-2023-28322', 'CVE-2023-28320', 'CVE-2023-32433', 'CVE-2023-38590', 'CVE-2023-32442', 'CVE-2023-37285', 'CVE-2023-38606', 'CVE-2023-32444', 'CVE-2023-38602'}
    OpenCVE data for CVEs:
    CVSS v3 for CVE CVE-2023-36495: 9.8
    CVSS v3 for CVE CVE-2023-34241: 7.1
    CVSS v3 for CVE CVE-2023-32441: 7.8
    CVSS v3 for CVE CVE-2023-38565: 7.8
    CVSS v3 for CVE CVE-2023-32443: 8.1
    CVSS v3 for CVE CVE-2023-38603: 7.5
    CVSS v3 for CVE CVE-2023-38258: 5.5
    CVSS v3 for CVE CVE-2023-32381: 7.8
    CVSS v3 for CVE CVE-2023-38593: 5.5
    CVSS v3 for CVE CVE-2023-38259: 5.5
    CVSS v3 for CVE CVE-2023-32364: 8.6
    CVSS v3 for CVE CVE-2023-38598: 9.8
    CVSS v3 for CVE CVE-2023-28321: 5.9
    CVSS v3 for CVE CVE-2023-36854: 7.8
    CVSS v3 for CVE CVE-2023-34425: 9.8
    CVSS v3 for CVE CVE-2023-2953: 7.5
    CVSS v3 for CVE CVE-2023-38604: 9.8
    CVSS v3 for CVE CVE-2023-35983: 5.5
    CVSS v3 for CVE CVE-2023-32429: 5.5
    CVSS v3 for CVE CVE-2023-38421: 5.5
    CVSS v3 for CVE CVE-2023-38571: 7.5
    CVSS v3 for CVE CVE-2023-35993: 7.8
    CVSS v3 for CVE CVE-2023-28319: 7.5
    CVSS v3 for CVE CVE-2023-32418: 7.8
    CVSS v3 for CVE CVE-2023-38601: 7.5
    CVSS v3 for CVE CVE-2023-32416: 5.5
    CVSS v3 for CVE CVE-2023-28322: 3.7
    CVSS v3 for CVE CVE-2023-28320: 5.9
    CVSS v3 for CVE CVE-2023-32433: 7.8
    CVSS v3 for CVE CVE-2023-38590: 8.8
    CVSS v3 for CVE CVE-2023-32442: 5.5
    CVSS v3 for CVE CVE-2023-37285: 9.8
    CVSS v3 for CVE CVE-2023-38606: 5.5
    CVSS v3 for CVE CVE-2023-32444: 7.5
    CVSS v3 for CVE CVE-2023-38602: 5.5
    
    Number of CVEs with scores: 35
    Number of CVEs without scores: 0
    
    CVE with the highest CVSS v3 score: CVE-2023-36495
    Highest CVSS v3 score: 9.8
    Qualitative rating: Critical

# Future Considerations:
- Slack Bot?
- Alerts?
- More details?
