# 7 common colors: red, green, blue, lightblue, purple, yellow, orange, grey
COLOR = ["#FF0000","#00FF00","#0000FF", "#00FFFF", "#FF00FF", "#FFFF00","#FF9900", "#808080"]
# 7 different heights, widths
HEIGHT_WIDTH = [(400,600), (400,800), (600,600), (800,400), (800,600)]
#HEIGHT_WIDTH = [(400,100), (500,100), (600,100), (700,100), (800,100)] # Circular
# 3 different mark size
#MARK_SIZE = [1,10] # area
#MARK_SIZE = [5,10] # bar
#MARK_SIZE = [1,2] # line
MARK_SIZE = [2,5] # point
# 3 different opacity
OPACITY = [0.2, 0.5, 1]
# orientations
ORIENT = ["vertical", "horizontal"]
#ORIENT = ["horizontal"] # circular
# # layouts
# LAYOUT = ["linear", "circular"]
# bounding box
OUTLINE = [0,1]
#OUTLINE = [0]
# axis
# AXIS = [True, False]
AXIS_RANGE = [500000, 100000, 50000]
AXIS_MAX = 100000000

template_chart='''
{
  "orientation": "horizontal",
  "tracks": [
    {
      "layout": "linear",
      "width": 800,
      "height": 180,
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "multivec",
        "row": "sample",
        "column": "position",
        "value": "peak",
        "categories": ["sample 1"],
        "binSize": 10
      },
      "mark": "area",
      "color":{"value": "#eb4034"},
      "size": {"value":3},
      "opacity":{"value":1},
      "style": {"outlineWidth":1},
      "x": {"field": "position", "type": "genomic", "axis": "bottom", "domain": {"interval": [2900000, 3000000]}},
      "y": {"field": "peak", "type": "quantitative", "axis": "left"}      
    }
  ]
}
'''

template_circular = '''
{
    "layout": "circular",
  "orientation": "horizontal",
  "tracks": [
    {
      "width": 800,
      "height": 80,
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "multivec",
        "row": "sample",
        "column": "position",
        "value": "peak",
        "categories": ["sample 1"],
        "binSize": 1
      },
      "mark": "area",
      "color":{"value": "#eb4034"},
      "size": {"value":3},
      "opacity":{"value":1},
      "style": {"outlineWidth":0},
      "x": {"field": "position", "type": "genomic", "axis": "bottom", "domain": {"interval": [2900000, 3000000]}},
      "y": {"field": "peak", "type": "quantitative", "axis": "none"}      
    }
  ]
}
'''

#mark = "area"
#mark = "bar"
#mark = "line"
mark = "point"

import json
import itertools
import os
import copy
import random

template_json = json.loads(template_chart)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"single_"+mark+"/"

if not os.path.exists(track_folder):
    os.makedirs(track_folder)
template_json["tracks"][0]["mark"] = mark



def make_spec(template, vars):
    color , hw, m, a, o, b, ar = vars
    spec = copy.deepcopy(template)
    spec["orientation"] = o
    track = spec["tracks"][0]
    track["color"]["value"] = color
    track["width"] = hw[0]
    track["height"] = hw[1]
    track["size"]["value"] = m
    if mark=="bar" or mark=="area":
        track["data"]["binSize"] = m
    track["opacity"]["value"] = a
    track["style"]["outlineWidth"] = b
    if o == "vertical":
        track["x"]["axis"] = "left"
        track["y"]["axis"] = "none"
    bins = AXIS_MAX//ar
    bin_choice = random.randint(0,bins-1)
    axis_start = bin_choice*ar
    axis_end = (bin_choice+1)*ar
    track["x"]["domain"]["interval"] = [axis_start, axis_end]
    return spec


#print(make_spec(template_json, ["red", (600,600), 2, 1, "vertical", 1, 10000]))

    

vars_list = itertools.product(COLOR, HEIGHT_WIDTH, MARK_SIZE, OPACITY, ORIENT, OUTLINE,AXIS_RANGE)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+mark+"_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)


