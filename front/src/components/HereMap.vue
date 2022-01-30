<template>
  <div id="map">
    <div id="mapContainer" style="height:600px;width:100%" ref="hereMap"></div>
  </div>
</template>

<script>
export default {
  name: "HereMap",
  props: {
    center: Object,
    // zoom: String,
    // latitude: String,
    // longitude: String
    // center object { lat: 43.6124203, lng: 1.4289301 }
  },
  data() {
    return {
      // H: window.H,
      map: {},
      geocoder: {},
      platform: null,
      apikey: "Qe4qjarfX-UGou2haKF8YC83z4tZFZANgiHpBEKAcgs",
      routingService: {},
      start: {
        lat: "43.6124203",
        lng: "1.4289301"
      },
      finish: {
        lat: "53.6124203",
        lng: "3"
      }
    };
  },
  // created() {
  //   this.platform = new window.H.service.Platform({
  //     apikey: this.apikey
  //   });
  // },
  mounted() {
    // Initialize the platform object:
    const platform = new window.H.service.Platform({
      apikey: this.apikey
    });
    this.platform = platform;
    this.geocoder = this.platform.getGeocodingService();

    // let maptypes = this.platform.createDefaultLayers();
    // const mapContainer = this.$refs.hereMap;
    // this.map = new window.H.Map(
    //   mapContainer,
    //   maptypes.vector.normal.normal.map,
    //   {
    //     zoom: this.zoom,
    //     center: this.center
    //   }
    // )
    this.routingService = this.platform.getRoutingService();

    console.log(this.routingService)
    
    this.initializeHereMap();
    // this.drawRoute(this.start, this.finish);
    
  },
  methods: {
    initializeHereMap() { // rendering map
      const mapContainer = this.$refs.hereMap;
      const H = window.H;
      // Obtain the default map types from the platform object
      let maptypes = this.platform.createDefaultLayers();

      // Instantiate (and display) a map object:
      this.map = new H.Map(
        mapContainer, 
        maptypes.vector.normal.map, 
        {
          zoom: 10,
          center: this.center
          // center object { lat: 40.730610, lng: -73.935242 }
        }
      );

      addEventListener("resize", () => this.map.getViewPort().resize());

      // add behavior control
      new H.mapevents.Behavior(new H.mapevents.MapEvents(this.map));

      // add UI
      H.ui.UI.createDefault(this.map, maptypes);
      // End rendering the initial map
    },
    drawRoute(start, finish) {
      console.log('start, finish', start, finish);
      this.routingService.calculateRoute(
        {
          "mode": "fastest;car;traffic:enabled",
          "waypoint0": `${start.lat},${start.lng}`,
          "waypoint1": `${finish.lat},${finish.lng}`,
          "representation": "display"
        },
        data => {
          // console.log(data);
          if (data.response.route.length > 0) {
            const H = window.H;
            let lineString = new this.H.geo.LineString();
            data.response.route[0].shape.forEach(point => {
              let [lat, lng] = point.split(",");
              lineString.pushPoint({ lat: lat, lng: lng});
            });
            let polyline = new H.map.Polyline(
              lineString,
              {
                style: {
                  lineWidth: 15,
                  strokeColor: 'blue'
                }
              }
            );
            this.map.addObjects(polyline);
            this.map.getViewModel().setLookAtData({ bounds: polyline.getBoudingBox() })
          }

        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

<style scoped>
#map {
  width: 100%;
  text-align: center;
  margin: 5% auto;
  background-color: #ccc;
}
</style>