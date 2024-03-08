document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('refreshButton').addEventListener('click', function() {
        fetch('http://127.0.0.1:8000/history/')
            .then(response => response.json())
            .then(data => {
                const historyList = document.getElementById('historyResult');
                historyList.innerHTML = '';
                data.forEach(call => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Date de l'appel : ${call.date}, Endpoint : ${call.endpoint}, Résultat : ${call.result}`;
                    historyList.appendChild(listItem);
                });
            })
            .catch(error => {
                document.getElementById('historyResult').innerText = 'Une erreur est survenue : ' + error.message;
            });
    });
});
