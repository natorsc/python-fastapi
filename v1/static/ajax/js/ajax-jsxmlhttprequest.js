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

    let ajax = new XMLHttpRequest();
    ajax.open('get', url, true);
    ajax.send();
    ajax.onreadystatechange = () => {
        // Caso o state seja 4 e o http.status for 200. Requisição OK.
        if (ajax.readyState == 4 && ajax.status == 200) {
            let json = JSON.parse(ajax.responseText);
            paragraph.innerHTML = `Bem vindo <b>${json['first_name']}</b>
            <b>${json['last_name']}</b>.`;
        } else {
            paragraph.innerHTML = ajax.statusText;
        }
        button.disabled = false;
    }
}

function sendDataByPost(button) {
    let firstName = document.getElementById('firstName');
    let lastName = document.getElementById('lastName');
    let paragraph = document.getElementById('result');

    button.disabled = true;

    var ajax = new XMLHttpRequest();
    ajax.open('post', APIURL, true);
    ajax.setRequestHeader('Accept', 'application/json');
    ajax.setRequestHeader('Content-Type', 'application/json');
    ajax.send(JSON.stringify(
        {
            'first_name': firstName.value,
            'last_name': lastName.value,
        }),
    );
    ajax.onreadystatechange = () => {
        // Caso o state seja 4 e o http.status for 200. Requisição OK.
        if (ajax.readyState == 4 && ajax.status == 200) {
            let json = JSON.parse(ajax.responseText);
            paragraph.innerHTML = `Bem vindo <b>${json['first_name']}</b>
            <b>${json['last_name']}</b>.`;
        } else {
            paragraph.innerHTML = ajax.statusText;
        }
        button.disabled = false;
    }
}