var endpoint = '/api/res/petrol-profit'
var defaultData = []
var labels = []
$.ajax({
    methos:"GET",
    url:endpoint,
    success:function(data){
        labels = data.labels
        defaultData = data.defaultDatas
        setChart()
    },
    error:function(error){
        console.log("error")
        console.log(error)
    }
});
function setChart(){
    var ctx = document.getElementById('myChart1').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels ,
                datasets: [{
                    label: 'Sale Per Day For Petrol in Rupees',
                    data: defaultData,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
}

// var endPoint = 'api/res/diesel-profit'
// var totalAmount = []
// var labels = []
// $.ajax({
//     methos:"GET",
//     url:endPoint,
//     success:function(data){
//         labels = data.date
//         defaultData = data.totalAmount
//         setChart()
//     },
//     error:function(error){
//         console.log("error")
//         console.log(error)
//     }
// });
// function setChart(){
//     var ctx = document.getElementById('myChart').getContext('2d');
//         var myChart = new Chart(ctx, {
//             type: 'bar',
//             data: {
//                 labels: labels ,
//                 datasets: [{
//                     label: 'Sale Per Day For Diesel in Rupees',
//                     data: defaultData,
//                     backgroundColor: [
//                         'rgba(255, 99, 132, 0.2)',
//                         'rgba(54, 162, 235, 0.2)',
//                         'rgba(255, 206, 86, 0.2)',
//                         'rgba(75, 192, 192, 0.2)',
//                         'rgba(153, 102, 255, 0.2)',
//                         'rgba(255, 159, 64, 0.2)'
//                     ],
//                     borderColor: [
//                         'rgba(255, 99, 132, 1)',
//                         'rgba(54, 162, 235, 1)',
//                         'rgba(255, 206, 86, 1)',
//                         'rgba(75, 192, 192, 1)',
//                         'rgba(153, 102, 255, 1)',
//                         'rgba(255, 159, 64, 1)'
//                     ],
//                     borderWidth: 1
//                 }]
//             },
//             options: {
//                 scales: {
//                     yAxes: [{
//                         ticks: {
//                             beginAtZero: true
//                         }
//                     }]
//                 }
//             }
//         });
// }