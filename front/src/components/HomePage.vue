<template>
  <div class="row justify-content-md-center">
    <div class="col col-12 my-5" id="recorderBloc">
      <h1>Où souhaitez-vous aller ?</h1>
      <p>Cliquez sur le micro pour indiquer votre trajet !</p>
      <SpeechRecognition lang="fr-FR" :white="false" @end="speechEnd" class="icon"/>
    </div>
      
    <div class="col col-12 my-5">
      <h1>Votre trajet</h1>
      <p v-if="isTextReceived">{{ textSent }}</p>
      <p v-else>Pas de trajet demandé</p>
    </div>

    <div class="col col-12 my-5">
      <!-- <b-button v-b-toggle.collapse-1 class="m-1"></b-button> -->
      <b-img src="../assets/transport.png" alt="Transport image" v-b-toggle.collapse-1 class="m-1"></b-img>
      <b-collapse :visible="showItinerariesBloc" id="collapse-1">
        <b-card id="itiBloc" v-if="Object.keys(this.itineraryResult).length != 0">
          <h1>Les itinéraires</h1>
          <hr>
          <!-- <div>{{ itineraryResult }}</div> -->
          <p>Temps de trajet : {{ itineraryResult.distance }} minutes</p>
          <div v-for="(itinerary, index) in itineraryResult.itineraries" :key="index">
            <!-- <p v-for="it in itinerary.itineraries" :key="it">{{ it }}</p> -->
            <p>{{ itinerary }}</p>
            <!-- <hr> -->
          </div>
          <hr>
          <HereMap  :center="center" />
        </b-card>
      </b-collapse>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import HereMap from './HereMap.vue';

export default Vue.extend({
  name: 'HomePage',
  components: { HereMap },
  data() {
    return {
      isTextReceived: false,
      textSent: '',
      itineraryResult: {},
      // itineraryResult: {
      //   "distance": 283,
      //   "itineraries": ["Gare de Toulouse-Matabiau","Gare de Cahors","Gare de Brive-la-Gaillarde","Gare de Bordeaux-St-Jean"]
      // },
      showItinerariesBloc: false,
      center:{ 
        lat: 43.6124203, 
        lng: 1.4289301
      }
    }
  },
  // computed: {
  //   itinerariesSort() {
  //     return [this.itineraries].sort(function (a: { distance: number; }, b: { distance: number; }) {
  //       return a.distance - b.distance;
  //     });
  //   }
  // },
  mounted() {
    // this.welcome();
  },
  methods: {
    speechEnd({transcriptions}) {
      let textRecorded = '';
      this.isTextReceived = false;
      textRecorded = transcriptions;
      console.log('textRecorded', textRecorded)
      if (textRecorded) {
        this.textSent = textRecorded;
        this.sendText(textRecorded);
      }
    },
    sendText(text: string) {
      axios
        .post('https://travel-resolver-100.herokuapp.com/vocal', {text})
        .then(response => {
          if(response.status == 200 && response.data) {
            console.log(response.data)
            this.isTextReceived = true;
            this.itineraryResult = response.data.train;
            this.showItinerariesBloc = true;
            console.log(this.itineraryResult)
          }
        })
        .catch(error => {
          console.error(error);
          this.isTextReceived = false;
        })
    },
    welcome() {
      axios
        .get('https://travel-resolver-100.herokuapp.com')
        .then(response => {
          if(response.status == 200) {
            console.log(response.data);
          }
        })
    }
  }
})
</script>

<style lang="scss">
#itiBloc {
  border: none;
}
#recorderBloc {
  .icon {
    img {
      cursor: pointer;
      margin-top: 20px;
      width: 64px;
      height: 64px;
    }
  }
}


</style>
