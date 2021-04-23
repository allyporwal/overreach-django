const optionsRepsRpe = {
  responsive: true,
  interaction: {
    mode: "index",
    intersect: false,
  },
  stacked: false,
  scales: {
    y: {
      type: "linear",
      display: true,
      position: "left",
      beginAtZero: true,
    },
    y1: {
      ticks: {
        stepSize: 1,
        precision: 1,
      },
      type: "linear",
      display: true,
      position: "right",
      max: "10",
      beginAtZero: true,
      grid: {
        drawOnChartArea: false,
      },
    },
    x: {
      ticks: {
        maxRotation: 0,
      },
    },
  },
};

const optionsVolumeRpe = {
  responsive: true,
  interaction: {
    mode: "index",
    intersect: false,
  },
  stacked: false,
  scales: {
    y: {
      type: "linear",
      display: true,
      position: "left",
      beginAtZero: true,
    },
    y1: {
      ticks: {
        stepSize: 1,
        precision: 1,
      },
      type: "linear",
      display: true,
      position: "right",
      max: "10",
      beginAtZero: true,
      grid: {
        drawOnChartArea: false,
      },
    },
    x: {
      ticks: {
        maxRotation: 0,
      },
    },
  },
};

// Reps chart
let totalReps = document.getElementById("totalReps");
let totalRepsChart = new Chart(totalReps, {
  type: "line",
  data: {
    datasets: [
      {
        label: "Total Reps",
        lineTension: 0.2,
        data: JSON.parse(
          document.getElementById("total_reps_chart_data").textContent
        ),
        backgroundColor: ["rgba(0, 178, 131, 0.3)"],
        borderColor: ["rgba(0, 178, 131, 0.3)"],
        borderWidth: 1,
        yAxisID: "y",
        fill: true,
      },
      {
        label: "Average RPE",
        lineTension: 0.2,
        data: JSON.parse(document.getElementById("rpe_chart_data").textContent),
        backgroundColor: ["rgba(178, 33, 0, 0.6)"],
        borderColor: ["rgba(178, 33, 0, 0.6)"],
        borderWidth: 1,
        yAxisID: "y1",
      },
    ],
  },
  options: optionsRepsRpe,
});

// Volume chart
let totalVolume = document.getElementById("totalVolume");
let totalVolumeChart = new Chart(totalVolume, {
  type: "line",
  data: {
    datasets: [
      {
        label: "Total volume",
        lineTension: 0.4,
        data: JSON.parse(
          document.getElementById("total_volume_chart_data").textContent
        ),
        backgroundColor: ["rgba(0, 178, 131, 0.3)"],
        borderColor: ["rgba(0, 178, 131, 0.3)"],
        borderWidth: 1,
        yAxisID: "y",
        fill: true,
      },
      {
        label: "Average RPE",
        lineTension: 0.2,
        data: JSON.parse(document.getElementById("rpe_chart_data").textContent),
        backgroundColor: ["rgba(178, 33, 0, 0.6)"],
        borderColor: ["rgba(178, 33, 0, 0.6)"],
        borderWidth: 1,
        yAxisID: "y1",
      },
    ],
  },
  options: optionsVolumeRpe,
});

// autoscroll snippet for cards
$('.scroll-icon').click(function() {
  $(this).parent().animate({ scrollTop: $(document).height() }, 1000);
})

$('.scroll-icon-up').click(function() {
  $(this).parent().animate({ scrollTop: -$(document).height() }, 1000);
})