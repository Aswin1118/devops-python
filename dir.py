import json
import os

script_dir = os.path.dirname(__file__)
script_absolute_path=os.path.join(script_dir, 'emp.json')

json=json.loads(open(script_absolute_path).read())
value=json['emp_name']
print(value)
