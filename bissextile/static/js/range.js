document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('rangeForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const startYear = document.getElementById('startYearInput').value;
        const endYear = document.getElementById('endYearInput').value;
        fetch(`http://127.0.0.1:8000/leap_years_in_range/${startYear}/${endYear}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('rangeResult').innerText = JSON.stringify(data.years);
            })
            .catch(error => {
                document.getElementById('rangeResult').innerText = 'Une erreur est survenue : ' + error.message;
            });
    });
});
