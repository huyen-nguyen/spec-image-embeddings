 
# Gosling-Boxes

First, make sure you have installed node.js in your computer.

### how to run the node.js script

In the root folder (gosling-boxes),  
run `npm install`

Inside the script folder (gosling-boxes/scripts), run
`node gosling-boxes.js example.json tracks.json`  
example.json stores the visualization spec.  
tracks.json saves the outputs of api calls.  

**Update**: run 
`node gosling-boxes.js example.json`
will directly generate a file with bounding boxes information `example.json` in the `data/extracted/bounding_box` directory, a file with spec `example.json` in the `data/extracted/specs` directory, and a file with screenshot view of canvas `example.png` in the `data/extracted/screeshot` folder.

You can also run it with a directory of specs. For example,
`node gosling-boxes.js ./train_specs/`
which will extracted the data for all specs within the train specs folder.

### how to run the react app
`npm install`
`npm start`

### how to clear all files in data directory
In the scripts folder, run
`python clear_data_dir.py`

### how to generate new specs (in development)
Go to scripts folder and run
`python generate_specs.py <template_spec_file_path> -h`. to see usage and available flags. 


### how to draw bounding boxes (in development)
Go to the scripts folder and run `python draw_bound_box.py <input_file> <output_file>`.
