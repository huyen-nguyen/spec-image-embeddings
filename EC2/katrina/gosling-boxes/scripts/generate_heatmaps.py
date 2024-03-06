template_chart='''
{
  "width": 600,
  "height": 600,
  "xDomain": {"interval": [800000000, 1800000000]},
  "tracks": [
    {
      "data": {
        "url": "https://higlass.io/api/v1/tileset_info/?d=CQMd6V_cRw6iCI_-Unl3PQ",
        "type": "matrix"
      },
      "mark": "rect",
      "x": {"field": "xs", "type": "genomic", "axis": "none"},
      "xe": {"field": "xe", "type": "genomic", "axis": "none"},
      "y": {"field": "ys", "type": "genomic", "axis": "none"},
      "ye": {"field": "ye", "type": "genomic", "axis": "none"},
      "color": {"field": "value", "type": "quantitative", "range": "grey"}
    }
  ]
}
'''

COLOR_RANGE = ["viridis", "grey", "hot", "warm", "pink", "spectral", "cividis", "bupu", "rdbu"]
AXIS_RANGE = [0,30]
AXIS_SIZE = 100000000
AXIS_LEN = [1,2,5,10, 15, 20, 30]
HEIGHT_WIDTH = [(400,400),(400,600),(400,800), (600,600),(600,400),(600,800),(800,400),(800,600), (800,800)]

import json
import os
import itertools
import copy
import random

template_json = json.loads(template_chart)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"heatmaps/"
if not os.path.exists(track_folder):
    os.makedirs(track_folder)

def make_spec(template, vars):
    color_range, hw, axs = vars
    new_spec = copy.deepcopy(template)
    ax_start = random.randint(0,30-axs)
    new_spec["xDomain"]["interval"] = [ax_start*AXIS_SIZE, (ax_start+axs)*AXIS_SIZE]
    new_spec["width"] = hw[0]
    new_spec["height"] = hw[1]
    new_spec["tracks"][0]["color"]["range"] = color_range
    return new_spec





vars_list = itertools.product(COLOR_RANGE, HEIGHT_WIDTH, AXIS_LEN)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+"heatmap_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)
