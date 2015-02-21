
function pieGraph(data){

    var dataFake = [
            ['data1', 30],
            ['data2', 120],
        ]

    var data = (data) ? data : dataFake ;

    var chart = c3.generate({
    bindto: '#graph-container',
    data: {
        columns: data,
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
});



}

