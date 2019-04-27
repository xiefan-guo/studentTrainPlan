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
        if (param.data.itemStyle.borderColor == 'red')
            param.data.itemStyle.borderColor = 'yellow';
        else
            param.data.itemStyle.borderColor = 'red';
        myChart.setOption({});
    }
};
var data2 = {
    "name": "flare",
    "children": [
        {
            "name": "flex",
            "children": [
                {"name": "FlareVis", "value": 4116, "itemStyle": {borderColor: "red",}}
            ]
        },
        {
            "name": "scale",
            "children": [

                {"name": "TimeScale", "value": 5833, "categories":1, "itemStyle": {borderColor: "red",}}
            ]
        },
        {
            "name": "display",
            "children": [
                {"name": "DirtySprite", "value": 8833, "itemStyle": {borderColor: "red",}}
            ]
        }
    ]
};

myChart.setOption(option = {
    tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove'
    },
    series:[
        {
            type: 'tree',

            data: [data2],

            left: '2%',
            right: '2%',
            top: '8%',
            bottom: '20%',

            symbol: 'emptyCircle',

            orient: 'vertical',

            expandAndCollapse: true,

            label: {
                normal: {
                    position: 'top',
                    rotate: -90,
                    verticalAlign: 'middle',
                    align: 'right',
                    fontSize: 9
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
