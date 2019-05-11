function submit(){
    alert("hello");
    $.ajax({
        type:'POST',
        url:"submit_train_plan",

        data:JSON.stringify(myChart.getOption()['series'][0]['data'][0]),  //转化字符串
        dataType: "json",
        success: function(data){
            myChart.setOption({
                series:[{
                    name:"trianPlanTree",
                    data: [data]
                }]
            })
        }
    })
}
// setInterval(function(){
//     Tree = myChart.getOption()['series'][0]['data'][0]
//     var subjects = ["思想政治理论", "外语", "文化素质教育必修", "体育", "军事", "健康教育", "数学", "物理", "计算机",
//     "学科基础", "专业选修", "课程设计", "实习 ", "毕业设计", "研究与创新", "跨学科选修或PSIP-跨学科选修", "学生创新实践计划(PSIP)"];
//     var year = ["第一学年", "第二学年"];
//     var option = ["必修", "选修"];
//     var subjects2TotalScore = {};
//     var subjects2ExistScore = {};
//     var subjects2AddScore = {};
//     // 初始化已选分数和总分数
//     for(var i=0; i<subjects.length;i++){
//         subjects2TotalScore[subjects[i]] = 0;
//         subjects2ExistScore[subjects[i]] = 0;
//     }
//     // 求得所需学分和
//     for(var sub =0; sub <subjects.length; sub++){
//         var existScore = 0;
//         var addScore = 0;
//         for (var year = 0; year < year.length; year++){
//             for( var option=0; option < option.length; i++){
//                 courses = myChart.getOption()['series'][0]['data'][0]["children"][sub]["children"][year]["children"][option];
//                 for(var course=0; course < courses.length; course++ ) {
//                     if(course['borderColor'] == 'green')
//                         existScore = existScore + course['value'];
//                     else if(course['borderColor'] == 'yellow')
//                         addScore = addScore + course['value'];
//                 }
//             }
//         }
//         subjects2ExistScore[subjects[sub]] = existScore;
//         subjects2AddScore[subjects[sub]] = addScore;
//     }
//
// })