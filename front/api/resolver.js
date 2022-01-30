import axios from 'axios';

const URL_API = 'https://travel-resolver-100.herokuapp.com';
// const URL_API = 'http://127.0.0.1:5000';

function sendText(text) {
  return new Promise((resolve, reject) => {
    axios
      .post(`${URL_API}/vocal`, {text})
      .then(response => {
        let data = {};
        if(response.status == 200 && response.data) {
          data = response.data;
          resolve(data);
        }
        reject(data);
      })
      .catch(error => {
        console.error(error);
        if (error.response) {
          reject({message: 'Something went wrong!'})
        }
        reject(error);
      })
  })
}

function welcome() {
  return axios
    .get(URL_API)
    .then(response => {
      if(response.status == 200) {
        console.log(response.data);
      }
    })
}

export { sendText, welcome };
