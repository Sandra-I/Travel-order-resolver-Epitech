import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueSpeechToText from 'vue-speech-to-text'
// vue-audio-recorder-and-player 
// import vueAudioRecorderAndPlayer from 'vue-audio-recorder-and-player'

Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(VueSpeechToText)
// Vue.use(vueAudioRecorderAndPlayer)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
