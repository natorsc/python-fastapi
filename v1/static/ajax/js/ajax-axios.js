const APIURL = '/v1/ajax/concatenate/names';

let paragraph = document.getElementById('result');

function sendDataByGet(button) {
    let firstName = document.getElementById('firstName');
    let lastName = document.getElementById('lastName');

    button.disabled = true;

    axios.get(APIURL, {
        params: {
            'first_name': firstName.value,
            'last_name': lastName.value,
        }
    }).then((response) => {
        paragraph.innerHTML = `Bem vindo
        <b>${response['data']['first_name']}</b> 
        <b>${response['data']['last_name']}</b>.`;
    }).finally(() => {
        button.disabled = false;
    });
}

function sendDataByPost(button) {
    let firstName = document.getElementById('firstName');
    let lastName = document.getElementById('lastName');

    button.disabled = true;

    // As requisições por padrão são json e utf-8.
    axios.post(APIURL, {
        'first_name': firstName.value,
        'last_name': lastName.value,
    }).then((response) => {
        paragraph.innerHTML = `Bem vindo
        <b>${response['data']['first_name']}</b>
        <b>${response['data']['last_name']}</b>.`;
    }).finally(() => {
        button.disabled = false;
    });
}