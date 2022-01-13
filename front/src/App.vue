<template>
  <div id="app" class="container">
    <b-card>
      <h1 class="card-title">The Recorder</h1>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
