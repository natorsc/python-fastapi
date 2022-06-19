function convertText(button, path) {
    let textarea = document.getElementById('textarea');
    let alertError = document.getElementById('alertError');
    let pError = document.getElementById('pError');

    if (textarea.value.length === 0) {
        pError.innerHTML = 'Área de texto não pode estar vazia.';
        alertError.classList.add("show");
        return;
    }

    button.disabled = true;

    const params = { 'data': textarea.value };
    let baseUrl = `${window.location.href}`;
    let url = baseUrl.substring(0, baseUrl.lastIndexOf('/')) + '/' + path;

    axios.get(url, {
        params: params,
    }).then((response) => {
        textarea.value = response.data['detail'];
    }).catch(function (error) {
        if (error.response) {
            pError.innerHTML = error.response.data['detail'];
            alertError.classList.add("show");
        } else if (error.request) {
            // console.log(error.request);
        } else {
            // console.log('Error', error.message);
        }
        // console.log(error.config);
    }).finally(() => {
        button.disabled = false;
    });
}