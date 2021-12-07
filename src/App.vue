<template>
  <div class="container">
    <Resolver />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Resolver from './components/Resolver.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    Resolver
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
