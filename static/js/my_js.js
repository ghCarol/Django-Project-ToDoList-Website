//添加任务
$('#list_items').on("mouseover",".item",function(){
$('.item').mouseover(function(){
    $(this).find('.menu').css("visibility","visible");
}).mouseleave(function(){
    $(this).find('.menu').css("visibility","hidden");
})
});

$('.new_text_placeholder').click(function(){
    $(this).hide();
    $(".new_text").focus();
})
$(".new_text").focus(function () {
    $('.new_text_placeholder').hide();
});
$('.td_submit').find('.ist_btn').click(function () {
    let new_Info =  $('.new_task_content .new_text');
    let new_text =new_Info.text();
    if (new_text==null||new_text=="") {
        $('.details').hide();
        return;
    }
    $.post("/toDoList/",{"new_content":new_text}, function(task){
        build_list_item(task);
    });
    new_Info.html("");
    //$('.details').hide();
});
// 利用list.html的方法
// $('.td_submit').click(function () {
//     var new_text = $('.new_task_content .new_text').text();
//     if (new_text==null||new_text=="") {
//         return;
//     }
//     $.post("/toDoList/",{'new_content':new_text}, function(renderResult){
//         $("#list_items").html(renderResult);
//     });
// });


//
let build_list_item = function(task){
    if (task){
        let new_item_HTMLDoc = '<li class=\"item item_'+ task.id +'\" id=\"item_'+ task.id +'\">\n' +
            '                        <table cellpadding=\"0\" cellspacing=\"0\">\n' +
            '                            <tbody>\n' +
            '                            <tr>\n' +
            '                                <td class=\"item_checker\">\n' +
            '                                    <div class=\"ist_checkbox\"><input type=\"checkbox\" name=\"finished\" id=\"item_checked_'+ task.id +'\"/></div>\n' +
            '                                </td>\n' +
            '                                <td class=\"item_content\">\n' +
            '                                    <span class=\"text\">'+ task.content +'</span>\n' +
            '                                </td>\n' +
            '                                <td class=\"menu\"><span class=\"icon glyphicon glyphicon-option-vertical\"></span></td>\n' +
            '                            </tr>\n' +
            '                            </tbody>\n' +
            '                        </table>\n' +
            '                    </li>' ;
        // var firstItem = $("#list_items").children(":first");
        // $(new_item_HTMLDoc).insertBefore(firstItem);
        //$('#list_items').append(new_item_HTMLDoc);
         let add_task = $(".details");
        $(new_item_HTMLDoc).insertBefore(add_task);
    }
}

$('.td_submit').find('.cancel').click(function () {
    $('.details').hide();
});

$('.controller_add').click(function () {
    let details = $('.details');
    details.show();
    details.find(".new_text").focus();
});

//已完成任务
$('#list_items').on("click",".item_checker",function () {
let item_checked_id = $(this).find('input').attr("id");
   let len = item_checked_id.length;
   let id = item_checked_id.substring(13,len);
   let item_id = "item_" + id;

   $.post("/toDoList/",{"finished_id":id}, function(){
        $("#"+item_id).hide();
    });

});

