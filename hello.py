
def group_by_owners(files):
    new_dict = {}
    values = []
     
    for file, owner in files.items():
        if owner == 'Randy':
            new_dict['Randy'] = values.append(file)
        elif owner == 'Stan':
            new_dict['Stan'] = values.append(file)
     
    return new_dict

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))