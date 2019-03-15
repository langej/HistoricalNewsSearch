import json
import datetime

def write_log(query, results):
  """
    query -> str
    results -> [str] // IDs von den ersten 10 Dokumenten für die Query
  """
  log = {
    "date": datetime.datetime.utcnow().isoformat(),
    "query": query,
    "results": results
  }
  w = open("logs/log.txt", "a")
  w.write(json.dumps(log) + "\n")
