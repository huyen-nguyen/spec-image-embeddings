import React, { useState, useEffect } from 'react';
import { GoslingComponent } from 'gosling.js';

import * as specs from './specs';


function App() {
	const keys = Object.keys(specs)

	const [key, setKey] = useState(keys[0]);

	const gosRef = React.useRef(null)

	useEffect(() => {
		if (gosRef.current) {
		//   gosRef.current.api.exportPng(false)
		const canvas = gosRef.current.api.getCanvas()
		const tracks = gosRef.current.api.getTracks()
		console.info(tracks.map(track=>track['shape']), canvas['canvas'])
		}
		return ()=>{}
	  }, [gosRef.current, key]);

	return (
		<div className="App">
			<select value={key} onChange={(k)=>setKey(k.target.value)}>
				{keys.map(k=>(<option value={k} key={k}> {specs[k]['title'] ?? k} </option>))}
			</select>
			<GoslingComponent
				spec={specs[key]}
				ref = {gosRef}
			/>
		</div>
	);
}

export default App;