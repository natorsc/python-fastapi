const APIURL = '/v1/ajax/concatenate/names';

let paragraph = document.getElementById('result');

function sendDataByGet(button) {
    let firstName = document.getElementById('firstName');
    let lastName = document.getElementById('lastName');

    button.disabled = true;

    $.ajax({
        type: 'get',
        async: true,
        url: APIURL,
        data: {
            'first_name': firstName.value,
            'last_name': lastName.value,
        },
        success: (response) => {
            paragraph.innerHTML = `Bem vindo <b>${response['first_name']}</b>
            <b>${response['last_name']}</b>.`;
        },
        error: (error) => {
            paragraph.innerHTML = `Status: ${error.status}
            Erro: ${error.statusText}`;
        },
        complete: () => {
            button.disabled = false;
        }
    });
}

function sendDataByPost(button) {
    let firstName = document.getElementById('firstName');
    let lastName = document.getElementById('lastName');

    button.disabled = true;

    $.ajax({
        type: 'post',
        async: true,
        url: APIURL,
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({
            'first_name': firstName.value,
            'last_name': lastName.value,
        }),
        success: (response) => {
            paragraph.innerHTML = `Bem vindo <b>${response['first_name']}</b>
            <b>${response['last_name']}</b>.`;
        },
        error: (error) => {
            paragraph.innerHTML = `Status: ${error.status}
            Erro: ${error.statusText}`;
        },
        complete: () => {
            button.disabled = false;
        }
    });
}