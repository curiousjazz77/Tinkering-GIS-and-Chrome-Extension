import React from "react";
import { Map, TileLayer, Marker } from "react-leaflet";
import Castles from "./Castles";

export default class MyMap extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      // lat: 50.0874654,
      // lng: 14.4212535,
      // lat: 41.69310000,
      // lng: -87.67187932,
      lat: 48.873756,
      lng: 2.294946,
      zoom: 16
    };
  }

  render() {
    const position = [this.state.lat, this.state.lng];
    return (
      <Map center={position} zoom={this.state.zoom}>
        <TileLayer
          attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={position} />
        <Castles />
      </Map>
    );
  }
}
