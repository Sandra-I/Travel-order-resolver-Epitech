<template>
  <div>
    <div class="row justify-content-md-center">
      <div class="col-12"><p>Cliquez sur le micro pour indiquer votre trajet !</p></div>
      <div class="col-12">
        <SpeechRecognition lang="fr-FR" :white="false" @end="speechEnd" class="icon"/>
      </div>
    </div>
      
    <div class="row">
      <div class="col-12">
        <h1 v-if="isTextReceived">Text reçu => {{ textSent }}</h1>
        <h1 v-else>No text recording</h1>
      </div>
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
      textSent: ''
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
      console.log(text)
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
.icon {

  img {
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

</style>
