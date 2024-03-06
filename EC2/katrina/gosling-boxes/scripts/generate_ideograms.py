template_1 = '''
{
  "views": [
    {
      "layout": "linear",
      "xDomain": {"chromosome":"chr1"},
      "orientation": "vertical",
      "tracks": [
        {
          "alignment": "overlay",
          "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/cytogenetic_band.csv",
            "type": "csv",
            "chromosomeField": "Chr.",
            "genomicFields": [
              "ISCN_start",
              "ISCN_stop",
              "Basepair_start",
              "Basepair_stop"
            ]
          },
          "tracks": [
            {
              "mark": "rect",
              "dataTransform": [
                {
                  "type": "filter",
                  "field": "Stain",
                  "oneOf": ["acen-1", "acen-2"],
                  "not": true
                }
              ],
              "color": {
                "field": "Density",
                "type": "nominal",
                "domain": ["", "25", "50", "75", "100"],
                "range": ["white", "#D9D9D9", "#979797", "#636363", "black"]
              },
              "size": {"value": 20}
            },
            {
              "mark": "rect",
              "dataTransform": [
                {"type": "filter", "field": "Stain", "oneOf": ["gvar"]}
              ],
              "color": {"value": "#A0A0F2"},
              "size": {"value": 20}
            },
            {
              "mark": "triangleRight",
              "dataTransform": [
                {"type": "filter", "field": "Stain", "oneOf": ["acen-1"]}
              ],
              "color": {"value": "#B40101"},
              "size": {"value": 20}
            },
            {
              "mark": "triangleLeft",
              "dataTransform": [
                {"type": "filter", "field": "Stain", "oneOf": ["acen-2"]}
              ],
              "color": {"value": "#B40101"},
              "size": {"value": 20}
            }
          ],
          "x": {"field": "Basepair_start", "type": "genomic", "axis": "none"},
          "xe": {"field": "Basepair_stop", "type": "genomic"},
          "stroke": {"value": "black"},
          "strokeWidth": {"value": 1},
          "style": {"outlineWidth": 0},
          "width": 200,
          "height": 250
        }
      ]
    }
  ]
}
'''

template_2='''
{
  "orientation": "horizontal",
  "xDomain":{"chromosome":"chr3"},
  "tracks": [
    {
      "width": 800,
      "height": 50,
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      "mark": "rect",
      "dataTransform": [
        {"type": "filter", "field": "Stain", "oneOf": ["acen"], "not": true}
      ],
      "color": {
        "field": "Stain",
        "type": "nominal",
        "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
        "range": ["white", "#D9D9D9", "#979797", "#636363", "black", "#A0A0F2"]
      },
      "x": {
        "field": "chromStart",
        "type": "genomic",
        "axis": "top"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "size": {"value": 50},
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5},
      "style": {"outline": "white"}
    }
  ]
}
'''

template_3='''
{
  "orientation": "horizontal",
  "alignment": "overlay",
  "data": {
    "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
    "type": "csv",
    "chromosomeField": "Chromosome",
    "genomicFields": ["chromStart", "chromEnd"]
  },
  "xDomain": {"chromosome": "chr3"},
  "tracks": [
    {
      "mark": "rect",
      "dataTransform": [
        {"type": "filter", "field": "Stain", "oneOf": ["acen"], "not": true}
      ],
      "color": {
        "field": "Stain",
        "type": "nominal",
        "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
        "range": ["#C0C0C0", "#808080", "#404040", "black", "black", "black"]
      },
      "size": {"value": 20}
    },
    {
      "mark": "rect",
      "dataTransform": [
        {"type": "filter", "field": "Stain", "oneOf": ["acen"]}
      ],
      "size": {"value": 10},
      "color": {"value": "#B74780"}
    }
  ],
  "x": {"field": "chromStart", "type": "genomic"},
  "xe": {"field": "chromEnd", "type": "genomic"},
  "color": {"value": "black"},
  "stroke": {"value": "white"},
  "strokeWidth": {"value": 1},
  "style": {"outline": "white"},
  "width": 800,
  "height": 60
}
'''

CHR = ["chr"+str(i+1) for i in range(22)]+["chrX", "chrY"]
LONG = [400,600,800]
SIZE = [20,30, 50]
# ORIENT = ["horizontal", "vertical"]
ORIENT = ["horizontal"]

import json
import itertools
import os
import copy
import random

template_json = json.loads(template_1)
data_folder = "/new_mem/data/generated_specs_3/"
track_folder = data_folder+"ideogram_1/"
if not os.path.exists(track_folder):
    os.makedirs(track_folder)

def make_spec(template, vars):
    chr, l, s, o = vars
    spec = copy.deepcopy(template)
    if "views" in spec.keys():
        views = spec["views"][0]
    else:
        views = spec
    views["xDomain"]["chromosome"] = chr
    views["orientation"] = o
    tracks = views["tracks"][0]
    if "tracks" in tracks.keys():
        for t in tracks["tracks"]:
            # if "value" in t["color"].keys():
            #   t["size"]["value"] = s//2
            # else:
              t["size"]["value"] = s
    else:
        tracks["size"]["value"] = s
    if o == "horizontal":
        tracks["width"] = l
        tracks["height"] = l
    else:
        tracks["width"] = l
        tracks["height"] = s+5
    return spec

vars_list = itertools.product(CHR, LONG, SIZE, ORIENT)
for i, vars in enumerate(vars_list):
    print(i, vars)
    with open(track_folder+"ideogram_1_"+str(i)+".json", "w") as spec_file:
        spec = make_spec(template_json,vars)
        json.dump(spec, spec_file)

