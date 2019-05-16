
// -------------------------------------------------//
/*
函数(1):function submit()
    功能:绑定"培养计划"界面中的“提交”按钮，将用户更新的计划书结果存储到数据库中，并刷新计划书和进度条
 */
function submit(){
    alert("提交成功");
    var postData = {};
    var tree = myChart.getOption()['series'][0]['data'][0];
    var scores = course2score;
    var returnData = {'tree':tree, 'scores':scores};
    $.ajax({
        type:'POST',
        url:"submit_train_plan",
        data:JSON.stringify(returnData),  //转化字符串
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

// --------------------------------------------------//
/*
函数(3) function dfsScore()
    功能: 根据计划树和子类别，得到该类别所有课程以及其评分
    输入：Tree, idx（类别)
    返回: {"类别": ["课程一"，"课程而"], [评分1， 评分2]}
 */

var allSujCourse = [];
var allSujScore = [];
var course2score = {};

function dfsScore(Node){
    if(typeof Node.children == 'undefined'){
        allSujCourse.push(Node['name']);
        allSujScore.push(Node['score']);
        course2score[Node['name']] = Node['score'];
    }
    else{
        // console.log(Node["children"]);
        for (var sub = 0; sub < Node["children"].length; sub++)
            dfsScore(Node["children"][sub]);
    }
}
// -----------------------------------------------------//

// --------------------------------------------------- //
/*
函数(4)：function score()
    功能, 更具计划树初始化评分下拉框，只显示未选课程以及未评分课程
    下拉框1：domain
    下拉框2：course
    下拉框3：score
 */


setTimeout(function initScore(){
    console.log("111");
    var allScore = ['1', '2', "3", '4', '5'];
    var courseScore = [];
    var courseName = [];
    var allSubject = [];
    Tree = myChart.getOption()['series'][0]['data'][0];
    for(var idx=0; idx<Tree['children'].length; idx++) {
        var subName = Tree['children'][idx]['name'];
        allSubject.push(subName);
        allSujCourse = [];
        allSujScore = [];
        dfsScore(Tree['children'][idx]);
        /*
        {"体育":["体育一", "体育二"], [分数1, 分数2], ....}
         */
        courseScore.push(allSujScore);
        courseName.push(allSujCourse);
    }
    console.log(courseScore);
    console.log(courseName);
    console.log(course2score);

    // 初始化下拉框的值
    document.getElementById("domain").length=0;
    $("#domain").append($("<option></option>").val(0).html("课程类别"));
    for(var idx=0; idx<allSubject.length; idx++){
        $("#domain").append($("<option></option>").val(idx + 1).html(allSubject[idx]));
    }

    $("#domain").change(function(){
        document.getElementById("course").length=0;
        $("#course").append($("<option></option>").val(0).html("课程"));
        var index = $(this).val()-1;
        for(var i = 0; i < courseName[index].length; i++) {
            if(courseScore[index][i] == 0+""){
                $("#course").append($("<option></option>").val(i + 1).html(courseName[index][i]));
            }
              else{
                $("#course").append($("<option></option>").val(i + 1).html("√"+courseName[index][i]));
            }
        }
    })
    $("#course").change(function(){
        document.getElementById("score").length=0;
        var domainSelect = document.getElementById("domain");
        var domainIndex = domainSelect.selectedIndex-1;
        console.log(domainIndex)
        var courseIndex = $(this).val() - 1;
        console.log(courseIndex)
        if(courseScore[domainIndex][courseIndex] == 0+""){
            $("#score").append($("<option></option>").val(0).html("请评分:"));
            for(var s=1; s<=5; s++){
                $("#score").append($("<option></option>").val(s).html(s));
            }
            $("#btnScore").attr('disabled',false);
            $("#score").attr("disabled", false);
        }
        else{
            $("#score").append($("<option></option>").val(0).html("已评分:"+ courseScore[domainIndex][courseIndex]));
            $("#btnScore").attr('disabled',true);
            $("#score").attr("disabled",true);
        }
    })
}, 3000)

// -------------------------------------------------------------------//
// --------------------------------------------------- //
/*
函数(5)：function updataScore()
    更新courseScore
    发送json文件给后端: {"课程1":3."课程2":2, ...}
 */

function updataScore(){
    var domCourse = document.getElementById("course")
    var courseName = domCourse[domCourse.selectedIndex].text;
    var domScore =  document.getElementById("score");
    course2score[courseName] = parseInt(domScore[domScore.selectedIndex].text);
    alert("评分成功")
    domScore.length=0;
    $("#score").append($("<option></option>").val(0).html("已评分:"+ course2score[courseName]));
    $("#score").attr("disabled",true);
    $("#btnScore").attr('disabled',true);
}
