console.log("From js")
function petrolAPI() {
    let petrolEndpoint = '/api/res/petrol-profit';
    let petrolDefaultData = [];
    let labels = [];
    $.ajax({
        methods: "GET",
        url: petrolEndpoint,
        success: function (data) {
            labels = data.labels;
            petrolDefaultData = data.defaultDatas;
            let ctx = document.getElementById('myChart1').getContext('2d');
            let myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Sale Per Day For Petrol in Rupees',
                        data: petrolDefaultData,
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
        },
        error: function (error) {
            console.log("error");
            console.log(error)
        }
    });
}
petrolAPI();
function dieselApi() {
    let dieselEndPoint = 'api/res/diesel-profit';
    let totalAmount = [];
    let dieselLabels = [];
    $.ajax({
        methods: "GET",
        url: dieselEndPoint,
        success: function (data) {
            labels = data.date;
            defaultData = data.amount;
            let ctx = document.getElementById('myChart').getContext('2d');
            let myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: dieselLabels,
                    datasets: [{
                        label: 'Sale Per Day For Diesel in Rupees',
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
        },
        error: function (error) {
            console.log("error");
            console.log(error)
        }
    });
}
dieselApi();
function mothAPi() {
    let endpoint = '/api/res/petrol-month-sale';
    let defaultData = [];
    let months = [];
$.ajax({
    methos: "GET",
    url: endpoint,
    success: function (data) {
        months = data.month;
        defaultData = data.totalSale;
        let ctx = document.getElementById('lineChart').getContext("2d");
        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: months,
                datasets: [{
                    label: "Monthly Petrol Sale in liters",
                    borderColor: "#80b6f4",
                    pointBorderColor: "#80b6f4",
                    pointBackgroundColor: "#80b6f4",
                    pointHoverBackgroundColor: "#80b6f4",
                    pointHoverBorderColor: "#80b6f4",
                    pointBorderWidth: 10,
                    pointHoverRadius: 10,
                    pointHoverBorderWidth: 1,
                    pointRadius: 3,
                    fill: false,
                    borderWidth: 4,
                    data: defaultData
                }]
            },
            options: {
                legend: {
                    position: "bottom"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            fontColor: "rgba(0,0,0,0.5)",
                            fontStyle: "bold",
                            beginAtZero: true,
                            maxTicksLimit: 5,
                            padding: 20
                        },
                        gridLines: {
                            drawTicks: false,
                            display: false
                        }

                    }],
                    xAxes: [{
                        gridLines: {
                            zeroLineColor: "transparent"
                        },
                        ticks: {
                            padding: 20,
                            fontColor: "rgba(0,0,0,0.5)",
                            fontStyle: "bold"
                        }
                    }]
                }
            }
        });
    }
});
}
mothAPi();