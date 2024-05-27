import re
from collections import defaultdict

# Function to read the file content
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Function to parse the project details and count projects by country
def parse_and_count_projects(data):
    # Dictionary to store the count of projects by country
    country_counts = defaultdict(int)
    
    # Regular expression to extract student names and their countries
    student_country_re = re.compile(r'<li>.*?, ([^,]+), ([^,]+), ([^<]+)</li>')
    
    # Find all student entries in the dataset
    students = student_country_re.findall(data)
    
    # Function to extract country from the location
    def extract_country(location):
        # Split the location by commas and take the last part as the country
        parts = location.split(',')
        country = parts[-1].strip()
        
        # Handle special cases and common variations
        if 'United States' in country:
            return 'United States of America'
        if 'China' in country and 'Taipei' not in country:
            return 'China'
        if 'Hong Kong' in country:
            return 'Hong Kong Special Administrative Region'
        if 'Macao' in country:
            return 'Macao Special Administrative Region'
        if 'Chinese Taipei' in country or 'Taipei' in country:
            return 'Chinese Taipei'
        return country
    
    # Increment the project count for each country
    for student in students:
        country = extract_country(student[2])
        country_counts[country] += 1

    return country_counts

# Main function to execute the script
def main():
    # Read the file content
    filename = './data.txt'
    data = read_file(filename)
    
    # Parse the data and count projects by country
    country_counts = parse_and_count_projects(data)
    
    # Print the results
    for country, count in sorted(country_counts.items()):
        print(f'{country}: {count} projects')

if __name__ == '__main__':
    main()
