var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
option = null;
myChart.on("click", clickFun);
function clickFun(param) {
    if (typeof param.seriesIndex == 'undefined') {
        return;
    }
    if (param.type == 'click' && typeof param.data.children == "undefined") {
        console.log(param.data.itemStyle.borderColor);
        if (param.data.itemStyle.borderColor == 'red') {
            param.data.itemStyle.borderColor = 'yellow';
            param.data.itemStyle.Color = 'yellow';
        }
        else if(param.data.itemStyle.borderColor == 'yellow') {
            param.data.itemStyle.borderColor = 'red';
            param.data.itemStyle.Color = 'red';
        }
        myChart.setOption({});
        console.log(param.data.itemStyle.borderColor);
    }
};
$.getJSON('/get_info', function(data)
{
    myChart.setOption(option = {
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        series:[
            {
                type: 'tree',

                data: [data],

                left: '2%',
                right: '2%',
                top: '8%',
                bottom: '20%',

                symbol: 'emptyCircle',
                symbolSize: 13,
                orient: 'vertical',
                initialTreeDepth: 2,
                expandAndCollapse: true,

                label: {
                    normal: {
                        position: 'top',
                        rotate: -90,
                        verticalAlign: 'middle',
                        align: 'right',
                        fontSize: 14
                    }
                },

                leaves: {
                    label: {
                        normal: {
                            position: 'bottom',
                            rotate: -90,
                            verticalAlign: 'middle',
                            align: 'left'
                        }
                    }
                },

                animationDurationUpdate: 750
            }
        ]
    });

});
