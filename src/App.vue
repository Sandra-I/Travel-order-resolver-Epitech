<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
    <Resolver />
    <hr>
    <SpeechRecognition lang="fr-FR" :white="false" @end="speechEnd" class="icon"/>
    <hr>
    <button v-on:click="testGet()">Test</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
// import HelloWorld from './components/HelloWorld.vue';
import Resolver from './components/Resolver.vue';
import SpeechRecognition from 'vue-webapi-speech-recognition'
import axios from 'axios'

export default Vue.extend({
  name: 'App',
  components: {
    // HelloWorld,
    Resolver,
    SpeechRecognition
  },
  data() {
    return {
      text: ''
    }
  },
  methods: {
    speechEnd({transcriptions}) {
      console.log(transcriptions);
      this.text = transcriptions
      this.sendText(this.text)
    },
    sendText(text: string){
      console.log(text, typeof(text));
      axios
        .post('http://127.0.0.1:5000/', {text})
        .then(response => console.log('response', response))
        .catch(error => {
          console.log(error)
          // this.errored = true
        })
        .finally(() => console.log('finally quoi'))
    },
    testGet() {
      axios
      // .post('http://127.0.0.1:5000/')
      .post('http://127.0.0.1:5000/', {text: 'hello'})
      .then(response => console.log('response', response))
      .catch(error => {
        console.log(error)
        // this.errored = true
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
