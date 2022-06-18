const APIURL = '/v1/ajax/concatenate/names';

let paragraph = document.getElementById('result');

function sendDataByGet(button) {
  let firstName = document.getElementById('firstName');
  let lastName = document.getElementById('lastName');

  button.disabled = true;

  const params = {
    'first_name': firstName.value,
    'last_name': lastName.value,
  };


  let url = APIURL + '?' + (new URLSearchParams(params)).toString();

  fetch(url, {
    method: 'get',
  }).then((response) => {
    if (response.ok) {
      return response.json();
    }
    return Promise.reject(response);
  }).then((json) => {
    paragraph.innerHTML = `Bem vindo <b>${json['first_name']}</b>
        <b>${json['last_name']}</b>`;
  }).catch((error) => {
    paragraph.innerHTML = error.statusText;
  }).finally(() => {
    button.disabled = false;
  });
}

function sendDataByPost(button) {
  let firstName = document.getElementById('firstName');
  let lastName = document.getElementById('lastName');

  button.disabled = true;

  fetch(APIURL, {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'first_name': firstName.value,
      'last_name': lastName.value,
    })
  }).then((response) => {
    if (response.ok) {
      return response.json();
    }
    return Promise.reject(response);
  }).then((json) => {
    paragraph.innerHTML = `Bem vindo <b>${json['first_name']}</b>
      <b>${json['last_name']}</b>`;
  }).catch((error) => {
    paragraph.innerHTML = error.statusText;
  }).finally(() => {
    button.disabled = false;
  });
}