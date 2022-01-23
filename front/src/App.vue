<template>
  <div id="app" class="container">
    <b-card class="theBloc">
      <h1 class="card-title mt-4">The Recorder</h1>
      <HomePage />
    </b-card>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import HomePage from './components/HomePage.vue';

export default Vue.extend({
  name: 'App',
  components: {
    HomePage
  }
});
</script>

<style lang="scss">

body {
  .theBloc {
    border-radius: 50px;
    background-color: #FFFFFF;
    box-shadow: 0px 0px 35px 4px #DDDDDD;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
}
</style>
