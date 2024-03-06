#!/bin/sh
SCALE="0.7;1.0;1.2"
SCALEWIDTH="0.7;1.0;1.2"
python generate_specs.py -f train_specs/basic_two_horizontal.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/basic_two_vertical.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/breast_cancer.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/circos.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/comp_heatmap.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/complex_hierarchy.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/example_sim_layout.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/example.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/gene_annotation.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/heatmap.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/hic.json -s $SCALE -sw $SCALEWIDTH
#python generate_specs.py -f train_specs/lollipop.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/multi_circular.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/multi_layer_circular.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/multiple_view.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/simple_circular.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/single_cell_epi.json -pv -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/three_composite_v.json -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/three_composite.json -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/two_by_two_sq_uneven_h.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/two_by_two_uneven_h.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/two_by_two_uneven_w.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train_specs/two_by_two.json -pv -cm -s $SCALE -sw $SCALEWIDTH
#python generate_specs.py -f train_specs/two_heatmap.json -s $SCALE -sw $SCALEWIDTH
