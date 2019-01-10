import json

def load_from_file():
  f = open("logs/evaluation.json", "r")
  data = f.read()
  return data

def append_data(old_data, new_data):
  return old_data.append(new_data)

def write_to_file(data):
  w = open("logs/evaluation.json", "w")
  w.write(json.dumps(data))

def persist_evaluation_data(data):
  old = load_from_file()
  new = append_data(old, data)
  write_to_file(new)