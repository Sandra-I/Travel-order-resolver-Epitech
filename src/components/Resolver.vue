<template>
  <div class="row d-flex justify-content-center p-2 bd-highlight">
      <div class="col align-self-center">
        <button type="button" class="btn btn-outline-dark btn-lg" v-on:click="voiceRecorder()">Recorder</button>
      </div>
      <div class="col align-self-center">
        <!-- <VueSpeechToText /> -->
      </div>
      <div class="col align-self-center">
        <button id="stop" type="button" class="btn btn-outline-dark">Stop</button>
      </div>
      <div class="col align-self-center">
        <a id="download" class="btn btn-primary" href="#" role="button">Ici la voix</a>
      </div>
      <div class="col align-self-center">
        <audio id="player" controls>
          <source id="playerSource" :src="this.voice">
          <p>Listen</p>
        </audio>
      </div>
      <p>{{ text }}</p>
  </div> 
</template>

<script>

export default {
  name: 'Resolver',
  data() {
    return {
      test: 'toto',
      voice: null,
      text: '',
      runtimeTranscription: '',
      sentences: []
    }
  },
  methods: {
    voiceRecorder() {
      const downloadLink = document.getElementById('download');
      const stopButton = document.getElementById('stop');

      const handleSuccess = function(stream) {
        console.log('handleSuccess')
        const options = {mimeType: 'audio/webm'};
        const recordedChunks = [];
        const mediaRecorder = new MediaRecorder(stream, options);

        mediaRecorder.addEventListener('dataavailable', function(e) {
          console.log('dataavailable')
          if (e.data.size > 0) {
            recordedChunks.push(e.data);
            console.log('recordedChunks', recordedChunks)
          }
        });

        mediaRecorder.addEventListener('stop', function() {
          console.log('stop')
          downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
          downloadLink.download = 'acetest.wav';
          this.voice = 'acetest.wav';
        });

        stopButton.addEventListener('click', function() {
          console.log('click')
          mediaRecorder.stop();
          const text = Array.from(event.results).map(result => result[0]).map(result => result.transcript).join('')
          this.runtimeTranscription = text
        });

        mediaRecorder.start();
      };

      navigator.mediaDevices.getUserMedia({ audio: true, video: false })
        .then(handleSuccess);
    }
  }
}
</script>
