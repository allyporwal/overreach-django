let avgRpe = document.getElementById('avgRpe');
let avgRpeChart = new Chart(avgRpe, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Average session RPE',
            data: JSON.parse(document.getElementById('rpe_chart_data').textContent),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 2
        }]
    },

    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

let totalReps = document.getElementById('totalReps');
let totalRepsChart = new Chart(totalReps, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Total Reps',
            data: JSON.parse(document.getElementById('total_reps_chart_data').textContent),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 2
        }]
    },

    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

let totalVolume = document.getElementById('totalVolume');
let totalVolumeChart = new Chart(totalVolume, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Total volume',
            data: JSON.parse(document.getElementById('total_volume_chart_data').textContent),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 2
        }]
    },

    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});