document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('yearForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const year = document.getElementById('yearInput').value;
        fetch('http://127.0.0.1:8000/is_leap_year/' + year + '/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = data.message;
            })
            .catch(error => {
                document.getElementById('result').innerText = 'Une erreur est survenue : ' + error.message;
            });
    });
});
