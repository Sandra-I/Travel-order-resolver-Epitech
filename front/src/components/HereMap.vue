<template>
  <div class="here-map">
    <div ref="map" id="map" v-bind:style="{ width: width + '%', height: height }" style="float: left"></div>
    <ol>
      <h4>LA ROUTE EN DETAILS</h4>
      <li v-for="(direction, key) in directions" v-bind:key="key">
        <p v-html="direction.instruction"></p>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: "HereMap",
  data() {
    return {
      map: null,
      platform: {},
      router: {},
      geocoder: {},
      directions: [],
      apikey: "Qe4qjarfX-UGou2haKF8YC83z4tZFZANgiHpBEKAcgs"
    }
  },
  props: {
    width: String,
    height: String,
    center: Object,
    start: String,
    finish: String,
    way: Array
  },
  created() {
    this.platform = new window.H.service.Platform({
      apikey: this.apikey
    });
    this.router = this.platform.getRoutingService();
    this.geocoder = this.platform.getGeocodingService();
  },
  mounted() {
    console.log('this.way', this.way)
    this.initializeHereMap();
    this.route();
  },
  watch: {
    way() {
      this.route();
    }
  },
  methods: {
    initializeHereMap() {
      let maptypes = this.platform.createDefaultLayers();
      this.map = new window.H.Map(
        this.$refs.map,
        maptypes.vector.normal.map,
        {
          zoom: 10,
          center: this.center
        }
      ); 
      addEventListener("resize", () => this.map.getViewPort().resize());
      // add behavior control
      new window.H.mapevents.Behavior(new window.H.mapevents.MapEvents(this.map));
      // add UI
      window.H.ui.UI.createDefault(this.map, maptypes);
    }, 
    geocode(query) {
      return new Promise((resolve, reject) => {
        console.log('Promise geocode')
        this.geocoder.geocode({ searchText: query }, data => {
          if(data.Response.View[0].Result.length > 0) {
            data = data.Response.View[0].Result.map(location => {
              return {
                lat: location.Location.DisplayPosition.Latitude,
                lng: location.Location.DisplayPosition.Longitude
              };
            });
            resolve(data);
          } else {
            reject({ "message": "No data found" });
          }
        }, error => {
          reject(error);
        });
      });
    },
    route() {
      const H = window.H;
      let params = {
        "mode": "fastest;car",
        "representation": "display"
      }
      let waypoints = [];
      this.map.removeObjects(this.map.getObjects());
      
      this.directions = [];

      this.way.map(res => {
        console.log(res)
        // const goeRes = await this.geocode(res);
        waypoints.push(this.geocode(res));
      })

      // for (const res of this.way) {
      //   console.log('for')
      //   const test = this.geocode(res)
      //   waypoints.push(test);
      // }
      
      // waypoints = [this.geocode('Toulouse'), this.geocode('Gare de Brive-la-Gaillarde'), this.geocode('Gare de Bordeaux-St-Jean')];
      console.log(waypoints)
      Promise.all(waypoints).then(result => {
        console.log('Promise all')
        let markers = [];
        for(let i = 0; i < result.length; i++) {
          params["waypoint" + i] = result[i][0].lat + "," + result[i][0].lng;
          markers.push(new H.map.Marker(result[i][0]));
        }
        this.router.calculateRoute(params, data => {
          if(data.response) {
            for(let i = 0; i < data.response.route[0].leg.length; i++) {
              this.directions = this.directions.concat(data.response.route[0].leg[i].maneuver);
            }
            data = data.response.route[0];
            let lineString = new H.geo.LineString();
            data.shape.forEach(point => {
              let parts = point.split(",");
              lineString.pushLatLngAlt(parts[0], parts[1]);
            });
            let routeLine = new H.map.Polyline(lineString, {
              style: { strokeColor: "blue", lineWidth: 5 }
            });
            console.log(routeLine);
            this.map.addObjects([routeLine, ...markers]);
            // this.map.setViewBounds(routeLine.getBounds());
            // Set the map's viewport to make the whole route visible:
            this.map.getViewModel().setLookAtData({bounds: routeLine.getBoundingBox()});
          }
        }, error => {
          console.error(error);
        });
      });
    }
  }
}
</script>

<style scoped>
#map {
  width: 100%;
  text-align: center;
  margin: 5% auto;
  background-color: #ccc;
}
</style>