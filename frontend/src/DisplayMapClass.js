import * as React from 'react';

export class DisplayMapClass extends React.Component {
  mapRef = React.createRef();

  state = {
    map: null
  };

  componentDidMount() {

    const H = window.H;
    const platform = new H.service.Platform({
        apikey: "{enter api key}"
    });

    const defaultLayers = platform.createDefaultLayers();
 const map = new H.Map(
      this.mapRef.current,
      defaultLayers.vector.normal.map,
      {
        center: { lat: 50, lng: 5 },
        zoom: 4,
        pixelRatio: window.devicePixelRatio || 1
      }
    );
    const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
    const ui = H.ui.UI.createDefault(map, defaultLayers); 
    this.setState({ map });
  }

  componentWillUnmount() {
    this.state.map.dispose();
  }

  render() {
    return (
 <div ref={this.mapRef} style={{ height: "500px" }} />
    );
  }
}
