const API_PATH = 'http://127.0.0.1:8000/api';


generator.addEventListener('click', (e) => {
    // e.preventDefault()
    let xhr = new XMLHttpRequest();

    xhr.open('POST', API_PATH + '/openai');
    let data = {
        'collection': collection.value
    };

    // xhr.setRequestHeader('Access-Control-Allow-Origin', '*');

    xhr.send(JSON.stringify(data));

    let prompt = null;

    xhr.onload = () =>{
        if(xhr.status == 200){
            // console.log(xhr.response)
            prompt = xhr.response;
            get_images(prompt);
        }
    };
    // return false;
})

function get_images(prompt){
    let options = {
        method: 'POST',
        body: prompt
    }
    fetch(API_PATH + '/file_by_data', options).then((resp)=>{
        console.log(resp)

        sleep(50000);
        let b64 = btoa(resp);

        // let newEl = document.createElement('img');
        // newEl.src = 'data:image/png;base64,' + b64;

        // document.body.appendChild(newEl);

    });
    console.log('!!!!')
    console.log(prompt);
    // xhr1.send(JSON.stringify(prompt));

    // xhr1.onload = () => {
    //     if(xhr1.status == 200){
    //         let response = xhr1.response;
    //         console.log(response)

    //         let b64 = btoa(response);

    //         // let newEl = document.createElement('img');
    //         // newEl.src = 'data:image/png;base64,' + b64;

    //         // document.body.appendChild(newEl);
    //     }
    // }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}