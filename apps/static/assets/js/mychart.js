// 메인 시총 1위 차트
var ctx = document.getElementById("chartBig1").getContext("2d");
var data = {
  labels: [], // 서버에서 가져온 날짜 데이터로 업데이트
  datasets: [
    {
      label: "Stock Price",
      fill: true,
      backgroundColor: "rgba(72,72,176,0.2)",
      borderColor: "#d048b6",
      borderWidth: 2,
      data: [], // 서버에서 가져온 주식 가격 데이터로 업데이트
    },
  ],
};

var options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        display: false,
      },
    },
  },
};

var chart = new Chart(ctx, {
  type: "line",
  data: data,
  options: options,
});

// 데이터 가져오기 및 그래프 업데이트
function updateChart() {
  $.get("/get_stock_prices/", function (data) {
    chart.data.labels = data.labels;
    chart.data.datasets[0].data = data.data;
    chart.update();
  });
}

// 초기 그래프 업데이트
updateChart();

// 주기적으로 그래프 업데이트
setInterval(updateChart, 6000); // 예: 60초마다 업데이트

// 시총 2위 차트
var ctx = document.getElementById("chartLinePurple").getContext("2d");

var data = {
  labels: ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
  datasets: [
    {
      label: "Data",
      fill: true,
      backgroundColor: "rgba(72,72,176,0.2)",
      borderColor: "#d048b6",
      borderWidth: 2,
      data: [800, 100, 70, 80, 120, 80],
    },
  ],
};

var options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        display: false,
      },
    },
  },
};

var chart = new Chart(ctx, {
  type: "line",
  data: data,
  options: options,
});

// 거래량 TOP 6 차트
var ctx = document.getElementById("Top_six").getContext("2d");

var data = {
  labels: ["주식1", "주식2", "주식3", "주식4", "주식5", "주식6"],
  datasets: [
    {
      label: "Data",
      fill: true,
      backgroundColor: "rgba(72,72,176,0.2)",
      borderColor: "#1f8ef1",
      borderWidth: 2,
      borderDash: [],
      borderDashOffset: 0.0,
      data: [800, 100, 60, 70, 2, 9],
    },
  ],
};

var options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        display: false,
      },
    },
  },
};

var chart = new Chart(ctx, {
  type: "bar",
  data: data,
  options: options,
});

// 시총 3위 차트
var ctxGreen = document.getElementById("chartLineGreen").getContext("2d");

var data = {
  labels: ["JUL", "AUG", "SEP", "OCT", "NOV"],
  datasets: [
    {
      fill: true,
      backgroundColor: "rgba(66,134,121,0.15)",
      borderColor: "#00d6b4",
      borderWidth: 2,
      borderDash: [],
      borderDashOffset: 0.0,
      pointBackgroundColor: "#00d6b4",
      pointBorderColor: "rgba(255,255,255,0)",
      pointHoverBackgroundColor: "#00d6b4",
      pointBorderWidth: 20,
      pointHoverRadius: 4,
      pointHoverBorderWidth: 15,
      pointRadius: 4,
      data: [90, 27, 60, 12, 80],
    },
  ],
};
var options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        display: false,
      },
    },
  },
};
var myChart = new Chart(ctxGreen, {
  type: "line",
  data: data,
  options: options,
});
