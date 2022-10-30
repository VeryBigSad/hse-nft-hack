const API_PATH = 'localhost:8000/api';


generator.addEventListener('click', (e) => {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', 'http://127.0.0.1:8000/api/openai');
    let data = {
        'collection': collection.value
    };

    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');

    xhr.send(JSON.stringify(data));

    xhr.onload = () =>{
        if(xhr.status == 200){
            console.log(xhr.response);
        }
    }
})