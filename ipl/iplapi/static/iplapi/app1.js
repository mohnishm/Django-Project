const chart1 = document.querySelector("#container1")
const data1 = JSON.parse(chart1.dataset.chart)

Highcharts.chart('container1', {
    chart: {
      type: 'column'
    },
    title: {
      text: data1.title
    },
    xAxis: {
      categories: Object.keys(data1.matches_data.matches_per_season),
      title: {
        text: data1.bottom
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: data1.text
      }
    },
    tooltip: {
      pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b>',
      shared: true
    },
    series: [{
        name:"matches",
      data: Object.values(data1.matches_data.matches_per_season)
    }]
  });
  
