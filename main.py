from pathlib import Path

def search_file(term):
  root_dir=Path('.')
  term = input("Enter search term: ")
  output=[]
  for file in root_dir.rglob("*"):
      if term in file.name:
        output.append(file.absolute())
  content='\n'.join(map(str, output))      
  return f'We found {len(output)} file(s) containing term {term}: \n{content}'
      
print(search_file(""))