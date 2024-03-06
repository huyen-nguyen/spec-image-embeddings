template_chart = '''
{
  "tracks": [
    {
      "width": 800,
      "height": 180,
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "multivec",
        "row": "base",
        "column": "position",
        "value": "count",
        "categories": ["A", "T", "G", "C"],
        "start": "start",
        "end": "end",
        "binSize": 16
      },
      "mark": "text",
      "y": {"field": "count", "type": "quantitative", "axis":"none"},
      "style": {"textStrokeWidth": 0, "outlineWidth":1},
      "stretch": true,
      "x": {"field": "start", "type": "genomic", "axis": "top", "domain":{"chromosome":"chr1"}},
      "xe": {"field": "end", "type": "genomic"},
      "color": {
        "field": "base",
        "type": "nominal",
        "domain": ["A", "T", "G", "C"],
        "range":["#FF0000","#00FF00","#0000FF", "#00FFFF"]
      },
      "text": {"field": "base", "type": "nominal"}
    }
  ]
}
'''

COLOR = ["#FF0000","#00FF00","#0000FF", "#00FFFF", "#FF00FF", "#FFFF00","#FF9900", "#808080"]
HEIGHT_WIDTH = [(400,100), (600,200), (800,200)]
OUTLINE = [0,1]
CHR = ["chr"+str(i+1) for i in range(22)]+["chrX", "chrY"]

import json
import itertools
import os
import copy
import random


template_json = json.loads(template_chart)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"info_logo/"
if not os.path.exists(track_folder):
    os.makedirs(track_folder)


def make_spec(template, vars):
    cr, hw, b, chr = vars
    spec = copy.deepcopy(template)
    track = spec["tracks"][0]
    track["width"] = hw[0]
    track["height"] = hw[1]
    track["x"]["domain"]["chromosome"] = chr
    track["color"]["range"] = cr
    track["style"]["outlineWidth"] = b
    if b == 0:
        track["x"]["axis"] = "none"
    return spec


    

COLOR_COMB = itertools.permutations(COLOR, 4)
COLOR_COMB = random.sample(list(COLOR_COMB), 40)
print(len(COLOR_COMB))
vars_list = itertools.product(COLOR_COMB, HEIGHT_WIDTH, OUTLINE,CHR)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+"single_text_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)