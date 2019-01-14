const chart5 = document.querySelector("#container5")
const data5 = JSON.parse(chart5.dataset.chart)
const datas = data5.matches_data["top_batting_average"]

Highcharts.chart('container5', {
    chart: {
      type: 'column'
    },
    title: {
      text: data5.title
    },
    xAxis: {
      categories: datas.map(element => element["batsman"]),
      title: {
        text: data5.bottom
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: data5.text
      }
    },
    tooltip: {
      pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b>',
      shared: true
    },
    series: [{
        name:"average",
        data: datas.map(element => element["average"])
    }]
  });