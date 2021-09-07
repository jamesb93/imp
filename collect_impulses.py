from pathlib import Path
import json

container = {}
data = {}

source = Path(
    "~/Cloud/Projects/reconstruction_error/analysis_data/clusters/outputs/AP_UMAP-7-1-ahc_250/ahc_250.json"
).expanduser()



with open(source, 'r') as f:
    data = json.load(f)


clusters = ['84', '127', '126', '191', '205', '162', '121']
temp = []

for cluster in clusters:
    for sound_file in data[cluster]:
        temp.append(sound_file)

container['clicks'] = temp

with open('click_samples.json', 'w') as f:
    json.dump(container, f)
