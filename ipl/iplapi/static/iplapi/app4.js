const chart4 = document.querySelector("#container4")
const data4 = JSON.parse(chart4.dataset.chart)
const datas = data4.matches_data["top_economical_bowler"]

Highcharts.chart('container4', {
    chart: {
      type: 'column'
    },
    title: {
      text: data4.title
    },
    xAxis: {
      categories: datas.map(el => el["bowler"]),
      title: {
        text: data4.bottom
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: data4.text
      }
    },
    tooltip: {
      pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b>',
      shared: true
    },
    series: [{
        name:"matches",
        data: datas.map(el => el["economy"])
    }]
  });
  
