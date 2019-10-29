console.log('je test si ca marche');

function ajaxPost(url, data, callback) {
    var req = new XMLHttpRequest ();
    req.open("POST", url);
    req.addEventListener('load', function() {
        if (req.status === 200) {
            callback(req.responseText)
        } else {
            console.error('Error')
        }
    });
    req.send(data);
}



// searchButton = document.getElementById('searchButton');
// searchButton.addEventListener('click', function (e) {

//     ajaxPost('/research/', searchButton, function(reponse){
//         answerFromApi = reponse;
//         dictAnswer = JSON.parse(answerFromApi);
//     });

// });

