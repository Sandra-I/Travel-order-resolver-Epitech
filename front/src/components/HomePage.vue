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
      <b-button v-b-toggle.collapse-1 class="m-1">Toggle Collapse</b-button>
      <b-collapse :visible="showItinerariesBloc" id="collapse-1">
        <b-card>
          <h1>Les itinéraires</h1>
          <div v-for="(itinerary, index) in itinerariesSort" :key="index">
            <p>{{ itinerary.cities }}</p>
            <p>Temps de trajet : {{ itinerary.distance }} minutes</p>
            <!-- <p v-for="it in itinerary" :key="it">{{ it }}</p> -->
            <hr>
          </div>
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
      // itineraries: [['Paris', 'Annecy', 'Grenoble', 'Marseille'], 47],
      itineraries: [
        { cities: ['Paris', 'Annecy', 'Grenoble', 'Marseille'], distance: 47 },
        { cities: ['Paris', 'Grenoble', 'Marseille'], distance: 40 },
        { cities: ['Paris', 'Marseille'], distance: 30 }
      ],
      showItinerariesBloc: true
    }
  },
  computed: {
    itinerariesSort() {
      return [...this.itineraries].sort(function (a: { distance: number; }, b: { distance: number; }) {
        return a.distance - b.distance;
      });
    }
  },
  methods: {
    speechEnd({transcriptions}) {
      let textRecorded = '';
      this.isTextReceived = false;
      textRecorded = transcriptions;
      this.sendText(textRecorded);
    },
    sendText(text: string) {
      axios
        .post('http://127.0.0.1:5000/vocal', {text})
        .then(response => {
          if(response.status == 200 && response.data.receivedText) {
            this.textSent = response.data.receivedText;
            this.isTextReceived = true;
          }
        })
        .catch(error => {
          console.error(error);
          this.isTextReceived = false;
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
