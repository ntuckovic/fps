
function pieGraph(data, container){

    var containerFake = '#graph-container';

    var dataFake = [
            ['data1', 30],
            ['data2', 120],
        ];

    var data = (data) ? data : dataFake ;
    var container = (container)? container : containerFake;

    var chart = c3.generate({
    bindto: containerFake,
    data: {
        columns: data,
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
});



}

