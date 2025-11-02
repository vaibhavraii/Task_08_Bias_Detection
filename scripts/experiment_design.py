import json
from pathlib import Path
PROMPTS = Path(__file__).resolve().parents[1]/'prompts'/'prompt_templates.json'
OUT = Path(__file__).resolve().parents[1]/'prompts'/'rendered_prompts.json'

def main():
 with open(PROMPTS,'r') as f: data=json.load(f)
 with open(OUT,'w') as o: json.dump(data,o,indent=2)
 print('Rendered prompts ->',OUT)

if __name__=='__main__': main()