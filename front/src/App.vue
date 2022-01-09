<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-12">
        <h1>The Recorder</h1>
      </div>
    </div>
    <hr/>
    <HomePage />
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
