const chart3 = document.querySelector("#container3")
const data3 = JSON.parse(chart3.dataset.chart)
const datas = data3.matches_data["extra_runs_2016"]

Highcharts.chart('container3', {
    chart: {
      type: 'column'
    },
    title: {
      text: data3.title
    },
    xAxis: {
      categories: datas.map(el => el["bowling_team"]),
      title: {
        text: data3.bottom
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: data3.text
      }
    },
    tooltip: {
      pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b>',
      shared: true
    },
    series: [{
        name:"matches",
        data: datas.map(el => el["extra_runs"])
    }]
  });
  
