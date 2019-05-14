var domCourse = document.getElementById("course_box");
var domPerson = document.getElementById("person_box");
var chartCourse = echarts.init(domCourse);
var chartPerson = echarts.init(domPerson);
var app = {};
optionCourse = null;
optionPerson = null;
$.getJSON('/getRecommedData', function(coursePersonJson)
var optionCourse = {
    dataset: coursePersonJson['course'],
    grid: {containLabel: true},
    xAxis: {name: 'amount'},
    yAxis: {type: 'category'},
    visualMap: {
        orient: 'horizontal',
        left: 'center',
        min: 1,
        max: 5,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: ['#D7DA8B', '#E15457']
        }
    },
    series: [
        {
            type: 'bar',
            encode: {
                // Map the "amount" column to X axis.
                x: 'amount',
                // Map the "product" column to Y axis
                y: 'product'
            }
        }
    ]
};
var optionPerson = {
    dataset: coursePersonJson['person'],
    grid: {containLabel: true},
    xAxis: {name: 'amount'},
    yAxis: {type: 'category'},
    visualMap: {
        orient: 'horizontal',
        left: 'center',
        min: 1,
        max: 5,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: ['#D7DA8B', '#E15457']
        }
    },
    series: [
        {
            type: 'bar',
            encode: {
                // Map the "amount" column to X axis.
                x: 'amount',
                // Map the "product" column to Y axis
                y: 'product'
            }
        }
    ]
};
if (optionCourse && typeof optionCourse === "object") {
    chartCourse.setOption(optionCourse, true);
}
if (optionPerson && typeof optionPerson === "object") {
    optionPerson.setOption(optionPerson, true);
}