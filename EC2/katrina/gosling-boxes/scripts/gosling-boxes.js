import puppeteer from "puppeteer";
import * as fs from "node:fs/promises";
import path from "node:path";
import * as fss from "node:fs";



/**
 * @param {string} spec
 * @param {{ reactVersion: string, pixijsVersion: string, higlassVersion: string, goslingVersion: string }} pkgOptions
 * @returns {string}
 */
function html(spec, {
    reactVersion = "17",
    pixijsVersion = "6",
    higlassVersion = "1.11",
    goslingVersion = "0.9.22",
} = {}) {
    let baseUrl = "https://unpkg.com";
    return `\
<!DOCTYPE html>
<html>
	<link rel="stylesheet" href="${baseUrl}/higlass@${higlassVersion}/dist/hglib.css">
	<script src="${baseUrl}/react@${reactVersion}/umd/react.production.min.js"></script>
	<script src="${baseUrl}/react-dom@${reactVersion}/umd/react-dom.production.min.js"></script>
	<script src="${baseUrl}/pixi.js@${pixijsVersion}/dist/browser/pixi.min.js"></script>
	<script src="${baseUrl}/higlass@${higlassVersion}/dist/hglib.js"></script>
	<script src="${baseUrl}/gosling.js@${goslingVersion}/dist/gosling.js"></script>
<body>
	<div id="vis"></div>
	<script>
		let api = gosling.embed(document.getElementById("vis"), JSON.parse(\`${spec}\`))
		window.tracks = api.then(a=>a.getTracks())
        window.canvas = api.then(a=>a.getCanvas())
        
	</script>
</body>
</html>`;
}


function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }

const DEFAULT_COLOR = ['#E79F00', '#029F73', '#0072B2', '#CB7AA7', '#D45E00', '#57B4E9', '#EFE441', '#d60000',
    '#018700', '#b500ff', '#05acc6', '#97ff00', '#ffa52f', '#ff8ec8', '#79525e', '#00fdcf', '#afa5ff',]


/**
 * @param {string} spec
 * @param {string} apiName
 * @returns {Promise<Buffer>}
 */
async function callAPI(spec, output_dir) {

    let browser = await puppeteer.launch({
        headless: true,
        args: ["--use-gl=egl"], // more consistent rendering of transparent elements
    });

    let page = await browser.newPage();
    await page.setContent(html(spec), { waitUntil: "networkidle0" });
    //let comp = await page.waitForSelector(".gosling-component");
    
    let canvas_elem = await page.$("canvas");
    await canvas_elem.screenshot({ path: output_dir["screenshots"], type: "png", omitBackground: true });

    let trackInfos = await page.evaluate(() => tracks)
    //console.log(trackInfos)
    //console.log(trackInfos.map(d=>d['spec']['color']))

    trackInfos = trackInfos.filter(function(d){return d["spec"]["mark"] != "header" && (d["spec"]["mark"]!=null || d["spec"]["overlay"]!=null)})
    fs.writeFile(output_dir["tracks"], JSON.stringify(trackInfos.map(d => d['shape'])));
    fs.writeFile(output_dir["specs"], JSON.stringify(trackInfos.map(d => d['spec'])));
    fs.writeFile(output_dir["marks"], JSON.stringify(trackInfos.map(d=>{
        if ("overlay" in d["spec"]) return d["spec"]["overlay"].map(o=>{
            if (o["mark"] == null) return d["spec"]["mark"];
            else return o["mark"];
        }
            );
        else return [d["spec"]["mark"]];
    })))
    fs.writeFile(output_dir["layouts"], JSON.stringify(trackInfos.map(d=>d["spec"]["layout"])))
    fs.writeFile(output_dir["orientations"], JSON.stringify(trackInfos.map(d=>d["spec"]["orientation"])))
    fs.writeFile(output_dir["chart"], JSON.stringify(trackInfos.map(d=>{
        if ("overlay" in d["spec"]){ 
            let res = d["spec"]["overlay"].map(o=>{
                if (o["mark"] == "rect"){
                    if (o["ye"] != null) return "heatmap";
                    // if (o["color"] != null && o["color"]["range"] != null && o["color"]["range"].includes("black")) console.log(o["color"]["range"])
                    else if (o["color"] != null && o["color"]["range"] != null && o["color"]["range"].includes("black")) return "ideogram";
                    else return "rect";
                }
                else if (o["mark"] == null) return d["spec"]["mark"];
                else return o["mark"];
            });
            if (res.includes("heatmap")) return ["heatmap"];
            else if (res.includes("ideogram")) return ["ideogram"];
            else return res;
        }
        else if (d["spec"]["mark"] == "rect"){
            // if (d["spec"]["color"]["range"]!=null) console.log("white" in d["spec"]["color"]["range"])
            if ("ye" in d["spec"]) return ["heatmap"];
            else if (d["spec"]["color"] != null && d["spec"]["color"]["range"] != null &&  d["spec"]["color"]["range"].includes("black")) return ["ideogram"];
            else return ["rect"];
        } else return [d["spec"]["mark"]];
    })))

    // Extract rows
    fs.writeFile(output_dir["row"], JSON.stringify(trackInfos.map(d=>{
        if ("row" in d["spec"]) {
            if ("domain" in d["spec"]["row"]) return d["spec"]["row"]["domain"];
            else return d["spec"]["data"]["categories"];
        }
        if ("overlay" in d["spec"]){
            return d["spec"]["overlay"].map(o=>{
                if ("row"in o){
                    if ("domain" in o["row"]) return o["row"]["domain"];
                    else return d["spec"]["data"]["categories"];
                }
                return [];
            })[0];
        }
        else return [];
    })))

    // Extract colors
    fs.writeFile(output_dir["color"], JSON.stringify(trackInfos.map(d=>{
        if ("color" in d['spec']){
            if ("value" in d["spec"]["color"]) return [d["spec"]["color"]["value"]];
            else if ("range" in d["spec"]["color"]) return d["spec"]["color"]["range"];

        } 
        if ("overlay" in d["spec"]){
            return d["spec"]["overlay"].map((o,i)=>{
                if ("color" in o){
                    if ("value" in o["color"]) return [o["color"]["value"]];
                    else if ("range" in o["color"]) return o["color"]["range"];
                } else {
                    if ("categories" in d["spec"]["data"]){
                        return d["spec"]["data"]["categories"].map((o,i)=>DEFAULT_COLOR[i]);
                    }
                    if ("row" in d["spec"]) {
                        if ("domain" in d["spec"]["row"]) return d["spec"]["row"]["domain"].map((o,i)=>DEFAULT_COLOR[i]);
                    }
                    else return [DEFAULT_COLOR[0]];
                }
            })
        } else {
            if ("categories" in d["spec"]["data"]){
                return d["spec"]["data"]["categories"].map((o,i)=>DEFAULT_COLOR[i]);
            }
            if ("row" in d["spec"]) {
                if ("domain" in d["spec"]["row"]) return d["spec"]["row"]["domain"].map((o,i)=>DEFAULT_COLOR[i]);
            }
            else return [DEFAULT_COLOR[0]];
        }
    })))

    await browser.close();
}

function mkdir_if_not_exist(dir){
    if (!fss.existsSync(dir)){
        fss.mkdirSync(dir);
    }
}

function mkdirs(dirs){
    for (const dir of dirs){
        mkdir_if_not_exist(dir);
    }
}

const DATA_FOLDER = "/new_mem/data/extracted-3/"
const OUTPUT_DIR = DATA_FOLDER+"bounding_box/"
const SPEC_DIR = DATA_FOLDER+"specs/"
const SCNS_DIR = DATA_FOLDER+"screenshot/"
const MARK_DIR = DATA_FOLDER+"marks/"
const LAYOUT_DIR = DATA_FOLDER+"layouts/"
const ORIENT_DIR = DATA_FOLDER+"orientations/"
const CHART_DIR = DATA_FOLDER+"chart/"
const ROW_DIR = DATA_FOLDER+"row/"
const COLOR_DIR = DATA_FOLDER+"color/"

mkdir_if_not_exist(DATA_FOLDER)
mkdirs([OUTPUT_DIR,SPEC_DIR,SCNS_DIR,MARK_DIR,LAYOUT_DIR,ORIENT_DIR,CHART_DIR, ROW_DIR,COLOR_DIR])


async function runExamplePath(fp) {
    let name = path.parse(fp).name;
    let output = name + ".json";
    let output_spec = name + ".json";
    let screenshot_output = name + ".png";
    let mark_output = name +".json";
    let layout_output = name+".json";
    let orient_output = name+".json";
    let chart_output = name+".json";
    let row_output = name+".json";
    let color_output = name+".json";
    const output_dir = {
        "tracks": OUTPUT_DIR+output,
        "specs":SPEC_DIR+output_spec,
        "screenshots": SCNS_DIR+screenshot_output,
        "marks": MARK_DIR+mark_output,
        "layouts": LAYOUT_DIR+layout_output,
        "orientations": ORIENT_DIR+orient_output,
        "chart": CHART_DIR+chart_output,
        "row":ROW_DIR+row_output,
        "color":COLOR_DIR+color_output
    }
    let spec = await fs.readFile(fp, "utf8");
    await callAPI(spec, output_dir);
}

let input = process.argv[2];

if (!input) {
    console.error(
        "Usage: node gosling-boxes.js <input.json> <output.json>",
    );
    process.exit(1);
}

const stat = await fs.lstat(input)
if (stat.isFile()) {
    runExamplePath(input);
} else {
    var files = await (fs.readdir(input))
    console.log(files);
    for (const f of files){
        console.log(f);
        await runExamplePath(path.join(input, f));
    }
}
