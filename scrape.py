import re 
from collections import defaultdict

def read_file(filename): 
  with open(filename, 'r', encoding='utf-8') as file: 
    return file.read() 
  
def parseAndCount(data): 
  # Regex expression to extract project 
  # project_blocks = re.findall(r'<p><strong>[^<]+</strong></p>(.*?)<p><strong>',data,re.DOTALL)
  # Dictionary to store the count of projects by country 
  country_counts = defaultdict(int)
  # Regex extract students name and countries 
  student_country_re = re.compile(r'<li>.*?, ([^,]+), ([^,]+), ([^<]+)</li>')
  students = student_country_re.findall(data)

  def extract_country(location): 
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
  
  for student in students: 
    country = extract_country(student[2])
    country_counts[country] += 1 

  return country_counts 

def main(): 
  filename = './data.txt'
  data=read_file(filename)

  country_counts=parseAndCount(data) 

  for country, count in sorted(country_counts.items()): 
    print(f'{country}: {count} projects')

if __name__=='__main__':
  main() 