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
      <b-img src="../assets/transport.png" alt="Transport image" v-b-toggle.collapse-1 class="m-1"></b-img>
      <b-collapse :visible="showItinerariesBloc" id="collapse-1">
        <template  v-if="Object.keys(this.itineraryResult).length != 0">

        </template>

        <div>
          <h1>Les itinéraires</h1>
          <b-tabs content-class="mt-3" align="center">
            <b-tab title="Train" active>
                <p>Temps de trajet : {{ itineraryResult.distance }} minutes</p>
                <div v-for="(itinerary, index) in itineraryResult.itineraries" :key="index">
                  <p>{{ itinerary }}</p>
                </div>
                <hr>
              <HereMap :center="center" ref="map" width="100" height="640px" :way="trainResult"/>
            </b-tab>

            <b-tab title="Voiture">
              <HereMap :center="center" ref="map" width="100" height="640px" :way="carResult"/>
            </b-tab>
          </b-tabs>
        </div>
      </b-collapse>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { sendText } from '../../api/resolver';
import HereMap from './HereMap.vue';

export default Vue.extend({
  name: 'HomePage',
  components: { HereMap },
  data() {
    return {
      isTextReceived: false,
      textSent: '',
      itineraryResult: {},
      carResult: {},
      showItinerariesBloc: true,
      center:{ 
        lat: 43.6124203, 
        lng: 1.4289301
      },
      trainResult: []
    }
  },
  methods: {
    speechEnd({transcriptions}) {
      let textRecorded = '';
      this.isTextReceived = false;
      textRecorded = transcriptions;
      if (textRecorded) {
        console.log('Texte enregistré', textRecorded)
        this.textSent = textRecorded;
        this.getResolver(textRecorded);
      }
    },
    async getResolver(text) {
      const result = await sendText(text);
      this.isTextReceived = true;
      this.itineraryResult = result.train;
      this.trainResult = result.train.itineraries;

      this.carResult = result.cities;
      this.showItinerariesBloc = true;
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
