const options = {
                 scales: {
                     y: {
                         beginAtZero: true
                        },
                     x: {
                         ticks: {
                             maxRotation: 0,
                            },
                        },
                    }
                }

// RPE chart
let avgRpe = document.getElementById('avgRpe');
let avgRpeChart = new Chart(avgRpe, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Average session RPE',
            lineTension: 0.4,
            data: JSON.parse(document.getElementById('rpe_chart_data').textContent),
            backgroundColor: [
                'rgb(100, 99, 132)',
            ],
            borderColor: [
                'rgb(100, 99, 132)',
            ],
            borderWidth: 2,
        }]
    },

    options: options,
});

// Total reps chart
let totalReps = document.getElementById('totalReps');
let totalRepsChart = new Chart(totalReps, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Total Reps',
            lineTension: 0.4,
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

    options: options,
});

// Total volume chart
let totalVolume = document.getElementById('totalVolume');
let totalVolumeChart = new Chart(totalVolume, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Total volume',
            lineTension: 0.4,
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

    options: options,
});