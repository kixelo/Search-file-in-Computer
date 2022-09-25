from pathlib import Path

def search_file(term):
  root_dir=Path('destination')
  term = input("Enter search term: ")
  output=[]
  for file in root_dir.rglob("*"):
      if term in file.name:
        results = file.absolute()
        output.append(results)
  content='\n'.join(map(str,output))      
  return f'We found {len(output)} file(s) containg term {term}: \n{content}'
      
print(search_file(""))