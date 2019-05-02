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
function get_info(){
    alert("hello");
    $.ajax({
        type:'POST',
        url:"get_info",

        data:JSON.stringify({1:2}),  //转化字符串
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