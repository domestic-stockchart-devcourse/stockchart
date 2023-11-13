// 함수 정의
function createChart(ctx, labels, data, backgroundColor, borderColor) {
  return new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Data",
          fill: true,
          backgroundColor: backgroundColor,
          borderColor: borderColor,
          borderWidth: 2,
          data: data,
        },
      ],
    },
    options: {
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
    },
  });
}
var chart1 = createChart(
  document.getElementById("chart1").getContext("2d"),
  [
    "start",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
  ], // 초기 라벨
  [70400, 70500, 70500, 70500, 70500, 70600], // 초기 데이터
  "rgba(72,72,176,0.2)",
  "#d048b6"
);
var chart2 = createChart(
  document.getElementById("chart2").getContext("2d"),
  [
    "start",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
  ], // 초기 라벨
  [414500, 414500, 414500, 414000, 414000, 415500], // 초기 데이터
  "rgba(72,72,176,0.2)",
  "#d048b6"
);
var chart4 = createChart(
  document.getElementById("chart4").getContext("2d"),
  [
    "start",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
    "2023-11-13",
  ], // 초기 라벨
  [131400, 131500, 131500, 131600, 131600, 131600], // 초기 데이터
  "rgba(72,72,176,0.2)",
  "#d048b6"
);

// 함수 정의
function createbarChart(ctx, labels, data, backgroundColor, borderColor) {
  return new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Data",
          fill: true,
          backgroundColor: backgroundColor,
          borderColor: borderColor,
          borderWidth: 2,
          data: data,
        },
      ],
    },
    options: {
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
    },
  });
}
var chart3 = createbarChart(
  document.getElementById("Top_six").getContext("2d"),
  [
    "200선물인버스2X",
    "코스닥150선물인버스",
    "코스닥150레버리지",
    "대유플러스",
    "경농",
    "2X WTI원유 선물",
  ], // 초기 라벨
  [100419925, 53936758, 32107786, 17146523, 16095592, 15950975], // 초기 데이터
  "rgba(72,72,176,0.2)",
  "#d048b6"
);

// mychart.js

function updateChartData() {
  fetch("api/stock-prices/?stock_name=삼성전자")
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // 데이터 콘솔에 출력
      // 나머지 데이터 업데이트 코드
      chart.data.labels = data.labels;
      chart.data.datasets[0].data = data.data;
      chart.update();
    })
    .catch((error) => console.error("데이터 업데이트 실패:", error));
}

// 초기 데이터 가져오기
updateChartData();

// 일정한 주기로 데이터 업데이트
setInterval(updateChartData, 6000); // 60초마다 업데이트 (원하는 주기로 변경 가능)
