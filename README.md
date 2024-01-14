# csv-search

The motivation for this mini project arose when an email address was going to be deactivated. The password manager in use contained nearly 500 records, and going through the entire database one by one would be a daunting task. This repo saved time by locating every record containing "emailAddress@institutionName.com."

Instructions: <br>

1. Export your passwords from your password manager as a CSV file.
2. Place the CSV file in the root directory of this project after cloning.
3. Run the script 'column_counter.py.' Depending on your file, it is possible that there is not a uniform number of columns. This script is needed to determine which record has the maximum number of columns and what the number is.
4. Run the cells in the Jupyter notebook titled 'search.ipynb.' The expected result is a CSV file containing only the records with the desired search term. For example, you may be looking for every record using a specific email address. At the top of this notebook, set 'string_search = 'yahoo''. This will pull every record that has 'yahoo' anywhere in the file.
