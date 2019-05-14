var domCourse = document.getElementById("course_box");
var domPerson = document.getElementById("person_box");
var chartCourse = echarts.init(domCourse);
var chartPerson = echarts.init(domPerson);

var app = {};
option = null;
var option = {
    dataset: {
        source: [
            [2.3, "计算机视觉"],
            [1.1, "自然语言处理"],
            [2.4, "高等数学"],
            [3.1, "线性代数"],
            [4.7, "计算机网络"],
            [5.1, "离散数学"]
        ]
    },
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
if (option && typeof option === "object") {
    chartCourse.setOption(option, true);
    chartPerson.setOption(option, true);
}