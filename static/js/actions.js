function submit(){
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
    alert("提交成功");
}
