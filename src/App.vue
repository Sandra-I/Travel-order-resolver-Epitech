<template>
  <div id="app">
    <h1>The Recorder</h1>
    <b-button><SpeechRecognition lang="fr-FR" :white="false" @end="speechEnd" class="icon"/></b-button>
    <hr>
    <h1 v-if="isTextReceived">Text reçu => {{ textSent }}</h1>
    <h1 v-else>No text recording</h1>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import SpeechRecognition from 'vue-webapi-speech-recognition'
import axios from 'axios'

export default Vue.extend({
  name: 'App',
  components: {
    SpeechRecognition
  },
  data() {
    return {
      textRecorded: '',
      isTextReceived: false,
      textSent: ''
    }
  },
  methods: {
    speechEnd({transcriptions}) {
      this.isTextReceived = false;
      this.textRecorded = transcriptions;
      this.sendText(this.textRecorded);
    },
    sendText(text: string) {
      console.log(text)
      axios
        .post('http://127.0.0.1:5000/', {text})
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
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.icon {
  width: 64px;
  height: 64px;
}
</style>
