function renderChart(data, labels) {
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'This week',
                data: data,
                lineTension:0.1,
                backgroundColor: 'rgba(255, 0, 10, 0.8)',

            }]
        },
    });
}

$("#renderBtn").click(
    function () {
        data = [310,583, 583 , 786, 830, 838,874];
        labels =  ["09.03","10.03","11.03 - no pred.","12.03","13.03","14.03","15.03"];
        renderChart(data, labels);
    }
);