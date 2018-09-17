import React from "react";
import { GeoJSON } from "react-leaflet";
const overpass = require("query-overpass");

export default class Castles extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      geojson: undefined
    };
  }

  componentDidMount() {
    const query = `[out:json];(way[historic=castle](around:10000, 48.873756,2.294946);\
                              relation[historic=castle](around:10000, 48.873756,2.294946););\
                              out body;>;out skel qt;`;
    const options = {
      flatProperties: true,
      overpassUrl: 'https://overpass-api.de/api/interpreter'
    };
    overpass(query, this.dataHandler, options);
  }

  dataHandler = (error, osmData) => {
    if (!error && osmData.features !== undefined) {
      this.setState({ geojson: osmData });
    }
  };

  render() {
    return this.state.geojson ? <GeoJSON data={this.state.geojson} /> : null;
  }
}
