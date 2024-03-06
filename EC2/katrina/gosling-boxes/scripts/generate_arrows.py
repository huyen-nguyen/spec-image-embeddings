template_chart_with_rule = '''
{
  "layout": "linear",
  "xDomain": {"chromosome": "chr3", "interval": [52168000, 52890000]},
  "arrangement": "horizontal",
    "views": [
      {
        "alignment": "overlay",
        "data": {
          "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=gene-annotation",
          "type": "beddb",
          "genomicFields": [
            {"index": 1, "name": "start"},
            {"index": 2, "name": "end"}
          ],
          "valueFields": [
            {"index": 5, "name": "strand", "type": "nominal"},
            {"index": 3, "name": "name", "type": "nominal"}
          ],
          "exonIntervalFields": [
            {"index": 12, "name": "start"},
            {"index": 13, "name": "end"}
          ]
        },
        "tracks": [
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["+"]}
            ],
            "mark": "triangleRight",
            "x": {"field": "end", "type": "genomic", "axis": "none"},
            "size": {"value": 15}
          },
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["-"]}
            ],
            "mark": "triangleLeft",
            "x": {"field": "start", "type": "genomic"},
            "size": {"value": 15},
            "style": {"align": "right"}
          },
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["+"]}
            ],
            "mark": "rule",
            "x": {"field": "start", "type": "genomic"},
            "strokeWidth": {"value": 3},
            "xe": {"field": "end", "type": "genomic"}
          },
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["-"]}
            ],
            "mark": "rule",
            "x": {"field": "start", "type": "genomic"},
            "strokeWidth": {"value": 3},
            "xe": {"field": "end", "type": "genomic"}
          }
        ],
        "row": {"field": "strand", "type": "nominal", "domain": ["+", "-"]},
        "color": {
          "field": "strand",
          "type": "nominal",
          "domain": ["+", "-"],
          "range": ["#7585FF", "#FF8A85"]
        },
        "opacity": {"value": 1},
        "width": 350,
        "height": 100,
        "style": {"outlineWidth":1}
      }
    ]
}
'''

template_chart = '''
{
  "layout": "linear",
  "xDomain": {"chromosome": "chr3", "interval": [52168000, 52890000]},
  "arrangement": "horizontal",
    "views": [
      {
        "alignment": "overlay",
        "data": {
          "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=gene-annotation",
          "type": "beddb",
          "genomicFields": [
            {"index": 1, "name": "start"},
            {"index": 2, "name": "end"}
          ],
          "valueFields": [
            {"index": 5, "name": "strand", "type": "nominal"},
            {"index": 3, "name": "name", "type": "nominal"}
          ],
          "exonIntervalFields": [
            {"index": 12, "name": "start"},
            {"index": 13, "name": "end"}
          ]
        },
        "tracks": [
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["+"]}
            ],
            "mark": "triangleRight",
            "x": {"field": "end", "type": "genomic", "axis": "none"},
            "size": {"value": 15}
          },
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["-"]}
            ],
            "mark": "triangleLeft",
            "x": {"field": "start", "type": "genomic"},
            "size": {"value": 15},
            "style": {"align": "right"}
          }
        ],
        "row": {"field": "strand", "type": "nominal", "domain": ["+", "-"]},
        "color": {
          "field": "strand",
          "type": "nominal",
          "domain": ["+", "-"],
          "range": ["#7585FF", "#FF8A85"]
        },
        "opacity": {"value": 1},
        "width": 350,
        "height": 300,
        "style": {"outlineWidth":1}
      }
    ]
}
'''

template_right = '''
{
  "layout": "linear",
  "xDomain": {"chromosome": "chr6"},
  "orientation": "horizontal",
    "views": [
      {
        "alignment": "overlay",
        "data": {
          "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=gene-annotation",
          "type": "beddb",
          "genomicFields": [
            {"index": 1, "name": "start"},
            {"index": 2, "name": "end"}
          ],
          "valueFields": [
            {"index": 5, "name": "strand", "type": "nominal"},
            {"index": 3, "name": "name", "type": "nominal"}
          ],
          "exonIntervalFields": [
            {"index": 12, "name": "start"},
            {"index": 13, "name": "end"}
          ]
        },
        "tracks": [
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["+"]}
            ],
            "mark": "triangleRight",
            "x": {"field": "end", "type": "genomic", "axis": "top"},
            "size": {"value": 15}
          }
        ],
        "color": {
          "value":"#7585FF"
        },
        "opacity": {"value": 1},
        "width": 350,
        "height": 100,
        "style": {"outlineWidth":1}
      }
    ]
}
'''

template_left = '''
{
  "layout": "linear",
  "xDomain": {"chromosome": "chr3"},
  "arrangement": "horizontal",
    "views": [
      {
        "alignment": "overlay",
        "data": {
          "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=gene-annotation",
          "type": "beddb",
          "genomicFields": [
            {"index": 1, "name": "start"},
            {"index": 2, "name": "end"}
          ],
          "valueFields": [
            {"index": 5, "name": "strand", "type": "nominal"},
            {"index": 3, "name": "name", "type": "nominal"}
          ],
          "exonIntervalFields": [
            {"index": 12, "name": "start"},
            {"index": 13, "name": "end"}
          ]
        },
        "tracks": [
          {
            "dataTransform": [
              {"type": "filter", "field": "type", "oneOf": ["gene"]},
              {"type": "filter", "field": "strand", "oneOf": ["-"]}
            ],
            "mark": "triangleLeft",
            "x": {"field": "start", "type": "genomic"},
            "size": {"value": 15},
            "style": {"align": "right"}
          }
        ],
        "color": {
          "value":"#FF8A85"
        },
        "opacity": {"value": 1},
        "width": 350,
        "height": 300,
        "style": {"outlineWidth":1}
      }
    ]
}
'''

HEIGHT_WIDTH = [(300,100), (400,100),(500,150), (700,200)]
MARK_SIZE = [10, 20]
OPACITY = [0.5, 1]
ORIENT = ["horizontal"]
OUTLINE = [0,1]
CHR = ["chr3","chr4", "chr6", "chr7", "chr10","chr11", "chr12","chr16", "chr17","chr19", "chr20"] # right
#CHR = ["chr1","chr3", "chr6", "chr12", "chr13", "chr14", "chr16"]
COLOR = ["#FF0000","#00FF00","#0000FF", "#00FFFF", "#FF00FF", "#FFFF00","#FF9900", "#808080"]

import json
import itertools
import os
import copy

template_json = json.loads(template_right)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"arrow_right/"
if not os.path.exists(track_folder):
    os.makedirs(track_folder)

def make_spec(template, vars):
    color , hw, m, a, o, b, chr = vars
    spec = copy.deepcopy(template)
    spec["orientation"] = o
    spec["xDomain"]["chromosome"] = chr
    view = spec["views"][0]
    track = view["tracks"][0]
    view["color"]["value"] = color
    view["width"] = hw[0]
    view["height"] = hw[1]
    track["size"]["value"] = m
    view["opacity"]["value"] = a
    view["style"]["outlineWidth"] = b
    return spec

vars_list = itertools.product(COLOR, HEIGHT_WIDTH, MARK_SIZE, OPACITY, ORIENT, OUTLINE,CHR)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+"arrow_right_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)
