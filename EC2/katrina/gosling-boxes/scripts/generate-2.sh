#!/bin/sh
SCALE="0.5;0.7;1.0;1.2;2.0"
SCALEWIDTH="0.5;0.7;1.0;1.2;2.0"
python generate_specs.py -f train-batch-2/basic_two_horizontal_orient.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/breast_cancer_circular.json -s $SCALE
python generate_specs.py -f train-batch-2/breast_cancer.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/circos.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_multi_row_area.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_multi_row_bar.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_multi_row_line.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_multi_row_point.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_multi_row_rect.json -s $SCALE
python generate_specs.py -f train-batch-2/circular_no_row_bar.json -cm -s $SCALE
python generate_specs.py -f train-batch-2/circular_no_row_point.json -s $SCALE
python generate_specs.py -f train-batch-2/gene_annotation_simple.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/gray_heatmap.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/hic_matrix.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/lollipop_simple.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_layer_circular.json -s $SCALE -cm
python generate_specs.py -f train-batch-2/multiple_ideograms.json -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_row_area.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_row_bar.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_row_line.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_row_point.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_row_rect.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_view_circular_ideograms.json -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_view_link.json -cm -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/multi_view_multi_track.json -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/no_row_bar.json -cm -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/no_row_point.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/pink_heatmap.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/simple_multi_view.json -cm -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/simple_withinLink.json -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/single_cell_epi_simple.json -cm -pv -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/three_composite.json -cm -pv -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/three_composite_v.json -cm -pv -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_by_two.json -cm -s $SCALE -c -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_by_two_sq_uneven_h.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_by_two_uneven_h.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_by_two_uneven_w.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_horizontal.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/two_vertical.json -cm -c -s $SCALE -sw $SCALEWIDTH
python generate_specs.py -f train-batch-2/warm_heatmap.json -s $SCALE -sw $SCALEWIDTH