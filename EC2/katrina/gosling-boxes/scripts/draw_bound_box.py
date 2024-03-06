from traceback import print_tb
from turtle import width
from PIL import Image, ImageDraw
import json
import math
import numpy as np
import sys
import os

IMG_DIR = "../data/extracted/screenshot/"
BOX_DIR = "../data/extracted/bounding_box/"
CIR_KEYS = {"cx", "cy", "innerRadius", "outerRadius", "startAngle", "endAngle"}
BOX_KEYS = {"x", "y", "width", "height"}


def load_boxes(box_file):
    f = open(box_file)
    data = json.load(f)
    f.close()
    return data


def adjust_angle(ang):
    return ang-90


def draw_rect(dr, box):
    box_info = [box["x"], box["y"], box["x"] +
                box["width"], box["y"]+box["height"]]
    dr.rectangle(box_info, outline="red", width=3)


def draw_circular(dr, box, width=3):
    dr.line([0, 100, ])
    inner_arc_bb = [box["cx"]-box["innerRadius"], box["cy"]-box["innerRadius"],
                    box["cx"]+box["innerRadius"], box["cy"]+box["innerRadius"]]
    dr.arc(inner_arc_bb, adjust_angle(box["startAngle"]), adjust_angle(
        box["endAngle"]), fill="red", width=3)
    outer_arc_bb = [box["cx"]-box["outerRadius"], box["cy"]-box["outerRadius"],
                    box["cx"]+box["outerRadius"], box["cy"]+box["outerRadius"]]
    dr.arc(outer_arc_bb, adjust_angle(box["startAngle"]), adjust_angle(
        box["endAngle"]), fill="red", width=3)
    edge_start_inner_x = box["cx"] + box["innerRadius"] * \
        np.cos(np.deg2rad(adjust_angle(box["startAngle"])))
    edge_start_inner_y = box["cy"] + box["innerRadius"] * \
        np.sin(np.deg2rad(adjust_angle(box["startAngle"])))
    edge_start_outer_x = box["cx"] + box["outerRadius"] * \
        np.cos(np.deg2rad(adjust_angle(box["startAngle"])))
    edge_start_outer_y = box["cy"] + box["outerRadius"] * \
        np.sin(np.deg2rad(adjust_angle(box["startAngle"])))
    dr.line([edge_start_inner_x, edge_start_inner_y, edge_start_outer_x,
            edge_start_outer_y], fill="red", width=width)
    edge_end_inner_x = box["cx"] + box["innerRadius"] * \
        np.cos(np.deg2rad(adjust_angle(box["endAngle"])))
    edge_end_inner_y = box["cy"] + box["innerRadius"] * \
        np.sin(np.deg2rad(adjust_angle(box["endAngle"])))
    edge_end_outer_x = box["cx"] + box["outerRadius"] * \
        np.cos(np.deg2rad(adjust_angle(box["endAngle"])))
    edge_end_outer_y = box["cy"] + box["outerRadius"] * \
        np.sin(np.deg2rad(adjust_angle(box["endAngle"])))
    dr.line([edge_end_inner_x, edge_end_inner_y, edge_end_outer_x,
            edge_end_outer_y], fill="red", width=width)


def draw_circular_box(dr, box, width=3):
    box_info = [box["cx"]-box["outerRadius"], box["cy"]-box["outerRadius"],
                box["cx"]+box["outerRadius"], box["cy"]+box["outerRadius"]]
    dr.rectangle(box_info, outline="red", width=width)


def draw_track_boxes(img_file, box_file, output_file):
    box_data = load_boxes(box_file)
    print(box_data)
    with Image.open(img_file) as im:
        draw = ImageDraw.Draw(im)
        for box in box_data:
            if box.keys() == BOX_KEYS:
                draw_rect(draw, box)
            elif box.keys() == CIR_KEYS:
                draw_circular_box(draw, box)

        im.save(output_file, "PNG")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python draw_bound_box.py <input_file> <output_file>")
    else:
        name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
        output_file = sys.argv[2]
        draw_track_boxes(IMG_DIR+name+".png", BOX_DIR +
                         name+".json", output_file)
