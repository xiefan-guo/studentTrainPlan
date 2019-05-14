
// -------------------------------------------------//
/*
函数(1):function submit()
    功能:绑定"培养计划"界面中的“提交”按钮，将用户更新的计划书结果存储到数据库中，并刷新计划书和进度条
 */
function submit(){
    alert("提交成功");
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
            originTrainPlain = data;
        }
    })
}
//----------------------------------------------------//
/*
函数(2)function rebuild()
    功能：重置计划树和进度条为初始状态(最近一次数据库中状态)
 */
function rebuild(){
    myChart.setOption({
        series:[{
            name:"trianPlanTree",
            data: [originTrainPlain]
        }]
    })
}
// ---------------------------------------------------//