template_within = '''
{
  "layout": "circular",
  "tracks": [
    {
      "width": 800,
      "height": 180,
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/circos-segdup-edited.txt",
        "type": "csv",
        "chromosomeField": "c2",
        "genomicFields": ["s1", "e1", "s2", "e2"]
      },
      "mark": "withinLink",
      "x": {
        "field": "s1",
        "type": "genomic",
        "domain": {"interval": [0, 3100000000]},
        "axis": "top"
      },
      "xe": {"field": "e1", "type": "genomic"},
      "x1": {
        "field": "s2",
        "type": "genomic",
        "axis": "top"
      },
      "x1e": {"field": "e2", "type": "genomic"},
      "stroke": {"value": "steelblue"},
      "style": {"outlineWidth":0},
      "opacity":{"value":0.5}
    }
  ]
}
'''

template_between = '''
{
  "layout": "circular",
  "tracks": [
    {
      "data": {
        "type": "csv",
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/circos-segdup-edited.txt",
        "chromosomeField": "c2",
        "genomicFields": ["s1", "e1", "s2", "e2"]
      },
      "mark": "betweenLink",
      "x": {"field": "s1", "type": "genomic", "axis":"top","domain":{"chromosome":"chr1","interval": [103900000, 104100000]}},
      "xe": {"field": "e1", "type": "genomic"},
      "x1": {"field": "s2", "type": "genomic","axis":"top"},
      "x1e": {"field": "e2", "type": "genomic"},
      "stroke": {"value": "#4C6629"},
      "strokeWidth": {"value": 0.8},
      "opacity": {"value": 0.15},
      "color": {"value": "#85B348"},
      "style": {"outlineWidth": 0},
      "width": 500,
      "height": 100
    }
  ]
}
'''

#HEIGHT_WIDTH = [(400,100), (400,150), (600,150), (600,200), (800,200), (800,250)]
HEIGHT_WIDTH = [(400,150), (600,200), (800,250)]
COLOR = ["#FF0000","#00FF00","#0000FF", "#00FFFF", "#FF00FF", "#FFFF00","#FF9900", "#808080"]
OPACITY = [0.2, 0.5, 1]
OUTLINE = [0]
AXIS_RANGE = [500000,1000000, 5000000]
AXIS_MAX = 3100000000

#AXIS_RANGE = [("chr1",[103900000, 104100000]),("chr14",[105000000, 1055000000])]


import json
import itertools
import os
import copy
import random


template_json = json.loads(template_within)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"single_circular_within_links/"

if not os.path.exists(track_folder):
    os.makedirs(track_folder)

def make_spec(template, vars):
    color , hw, a, b, ar = vars
    spec = copy.deepcopy(template)
    track = spec["tracks"][0]
    track["width"] = hw[0]
    track["height"] = hw[1]
    track["stroke"]["value"] = color
    if "color" in track.keys():
        track["color"]["value"] = color
    track["opacity"]["value"] = a
    track["style"]["outlineWidth"] = b
    if b == 0:
        track["x"]["axis"] = "none"
        track["x1"]["axis"] = "none"
    bins = AXIS_MAX//ar
    bin_choice = random.randint(0,bins-1)
    axis_start = bin_choice*ar
    axis_end = (bin_choice+1)*ar
    track["x"]["domain"]["interval"] = [axis_start, axis_end]
    # track["x"]["domain"]["chromosome"] = ar[0]
    # track["x"]["domain"]["interval"] = ar[1]
    return spec


vars_list = itertools.product(COLOR, HEIGHT_WIDTH, OPACITY, OUTLINE, AXIS_RANGE)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+"circular_within_link_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)