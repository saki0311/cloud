var ctx = document.getElementById("motivation-graph")
//const motivate_data = JSON.parse('{{ json_data|safe }}');
//console.log(motivate_data);
var myLineChart = new Chart(ctx,{
  type: 'line',
  data:{
    labels: ['15歳', '16歳', '17歳', '18歳', '19歳', '20歳', '21歳'],
    datasets: [
      {
        label: 'モチベーション(%）',
        data: [40, 50, 75, 10, 34, 50, 80, 25],
        borderColor: "rgba(255,0,0,1)",
        backgroundColor: "rgba(0,0,0,0)"
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: '人生のモチベーショングラフ'
    },
    scales: {
      yAxes: [{
        ticks: {
          suggestedMax: 100,
          suggestedMin: 0,
          stepSize: 10,
          callback: function(value, index, values){
            return  value +  '%'
          }
        }
      }]
    },
  }
});