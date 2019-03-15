import json

def load_from_file():
  with open('logs/evaluation.json') as json_file:
    data = json.load(json_file)
    return data

def append_data(old_data, new_data):
  return old_data.append(new_data)

def write_to_file(data):
  with open('logs/evaluation.json', 'w') as outfile:  
    json.dump(data, outfile, sort_keys=True, indent=4)

def persist_evaluation_data(data):
  data = json.loads(data)
  old = load_from_file()
  append_data(old, data)
  write_to_file(old)



if __name__ == "__main__":
  data = load_from_file()
  append_data(data, [{"abc": 42},{"qwe": 23.5}])
  append_data(data, [{"abc": "guck mal an"},{"qwe": "was ein scheiß"}])
  write_to_file(data)
  print(json.dumps(data[1]))