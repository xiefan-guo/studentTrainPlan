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
        else{
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
                initialTreeDepth: 4,
                expandAndCollapse: true,

                label: {
                    normal: {
                        position: 'bottom',
                        rotate: -90,
                        verticalAlign: 'middle',
                        align: 'left',
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
var perExistScore;
var perAddScore;

function getScore(Node){
    if(typeof Node.children == 'undefined'){
        if(Node.itemStyle.borderColor == "yellow"){
            perAddScore += Node.value;
        }
        else if (Node.itemStyle.borderColor == "green"){
            perExistScore += Node.value;
        }
    }
    else{
        // console.log(Node["children"]);
        for (var sub = 0; sub < Node["children"].length; sub++)
            getScore(Node["children"][sub]);
    }
}
setInterval(function(){
    Tree = myChart.getOption()['series'][0]['data'][0];
    var subjects = ["思想政治理论", "外语", "文化素质教育必修", "体育", "军事", "健康教育", "数学", "物理", "计算机",
        "学科基础", "专业选修"];
    var subjects2TotalScore = {};  //所需总学分
    var subjects2ExistScore = {};  //已修学分(绿色)
    var subjects2AddScore = {};  //拟增加学分(黄色)
    // 初始化已选分数和总分数
    for(var i=0; i<subjects.length;i++){
        subjects2TotalScore[subjects[i]] = Tree['children'][i].value;
        subjects2ExistScore[subjects[i]] = 0;
        subjects2AddScore[subjects[i]] = 0;
    }
    // 求得所需学分和
    for(var sub =0; sub <subjects.length; sub++){
        perExistScore = 0;
        perAddScore = 0;

        getScore(Tree['children'][sub]);
        subjects2ExistScore[subjects[sub]] = perExistScore;
        subjects2AddScore[subjects[sub]] = perAddScore;
    }
    var TotalScore = 0;
    var TotalExistScore = 0;
    var TotalAddScore = 0;
    for(var i=0; i<subjects.length; i++){
        TotalScore += subjects2TotalScore[subjects[i]];
        TotalExistScore += subjects2ExistScore[subjects[i]];
        TotalAddScore += subjects2AddScore[subjects[i]];
    }


    // 生成进度条标签
    var processes = [];
    var pLabels = [];
    for(var i=2; i< subjects.length+2; i++){
        processes.push("process-parent"+i.toString());
        pLabels.push("on" + i.toString());
    }
    // 更新总进度条
    var greenWidth, yellowWidth;
    var doms = document.getElementsByClassName("process-parent1")[0].children;
    greenWidth = (TotalExistScore*100/TotalScore).toFixed(2);
    yellowWidth = (TotalAddScore*100/TotalScore).toFixed(2);
    doms[0].style.width = greenWidth + "%";
    doms[1].style.width = Math.min(100-greenWidth, yellowWidth) + "%";
    dom = document.getElementById("on1");
    dom.textContent = TotalExistScore + '/' + TotalScore;

    // 设置各个子进度条

    for(var idx=0; idx<processes.length; idx++){
        TotalScore = subjects2TotalScore[subjects[idx]];
        TotalExistScore = subjects2ExistScore[subjects[idx]];
        TotalAddScore = subjects2AddScore[subjects[idx]];
        var doms = document.getElementsByClassName(processes[idx])[0].children;
        greenWidth = (TotalExistScore*100/TotalScore).toFixed(2);
        yellowWidth = (TotalAddScore*100/TotalScore).toFixed(2);
        doms[0].style.width = greenWidth + "%";
        doms[1].style.width = Math.min(100-greenWidth, yellowWidth) + "%";
        dom = document.getElementById(pLabels[idx]);
        dom.textContent = TotalExistScore + '/' + TotalScore;
    }
}, 1)