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
        <b-card>
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
        </b-card>
      </b-collapse>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';

export default Vue.extend({
  name: 'HomePage',
  data() {
    return {
      isTextReceived: false,
      textSent: '',
      // itineraries: {},
      // itinerariesSort: [['Paris', 'Annecy', 'Grenoble', 'Marseille'], 47],
      itineraryResult: {
        "distance": 283,
        "itineraries": ["Gare de Toulouse-Matabiau","Gare de Cahors","Gare de Brive-la-Gaillarde","Gare de Bordeaux-St-Jean"]
      },
      showItinerariesBloc: true
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
      this.sendText(textRecorded);
    },
    sendText(text: string) {
      axios
        .post('https://travel-resolver-100.herokuapp.com/vocal', {text})
        .then(response => {
          if(response.status == 200 && response.data.data) {
            console.log(response.data.data)
            this.isTextReceived = true;
            this.textSent = text;
            this.itineraryResult = response.data.data;
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
#recorderBloc {
  // background-color: rgb(255, 223, 223);

  .icon {
    img {
      margin-top: 20px;
      width: 64px;
      height: 64px;
      -ms-transition: width 5s, height 5s, transform 5s;
      -webkit-transition: width 5s, height 5s, transform 5s;
      transition: width 5s, height 5s, transform 5s;
    }

    :hover {
      cursor: pointer;
      width: 100px;
      height: 100px;
      // background-color: gold;
      -ms-transform: scale(1.5); /* IE 9 */
      -webkit-transform: scale(1.5); /* Safari 3-8 */
      transform: scale(1.5);
    }
  }
}


</style>
