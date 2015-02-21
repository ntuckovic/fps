//glavni graf

var chart = c3.generate({
	bindto: '#graph-container',
    data: {
    	x: "x",
        columns: [
        	["x", "SDP", "HDZ", "HNS", "HSLS", "HSP", "HSS"],
            ['data1', 30, 200, 100, 400, 150, 250],
            // ['data2', 130, 100, 140, 200, 150, 50]
        ],
        type: 'bar'
    },
    axis: {
        x: {
            type: 'category',
            tick: {
                rotate: 75,
                multiline: false
            },
            height: 130
        }
    }
});