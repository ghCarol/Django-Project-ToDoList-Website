//设置右侧菜单hover可见
$('#list_items').on("mouseover", ".item", function () {
    $('.item').mouseover(function () {
        $(this).find('.menu').css("visibility", "visible");
    }).mouseleave(function () {
        let td_menu = $(this).find('.menu'),
            dropdown_menu = $(this).find('.dropdown-menu'),
            display_value = dropdown_menu.css("display");
        if (display_value == "none")
            $(this).find('.menu').css("visibility", "hidden");
        else
            td_menu.css("opacity", "1"); //使bootstrap下拉菜单仍然可见
    })
});

$('#list_items').on("click", ".new_text_placeholder", function () {
    $(this).hide();
    $(".new_text").focus();
});
$(".new_text").focus(function () {
    $('.new_text_placeholder').hide();
}).blur(function () {
    if ($(this).text() == "")
        $('.new_text_placeholder').show();
});
//添加任务
$('#details').find('.ist_btn').click(function () {
    let new_Info = $('.new_task_content .new_text'),
        new_text = new_Info.text();
    if (new_text == null || new_text == "") {
        $('.details').hide();
        return;
    }
    $.post("/toDoList/", {"new_content": new_text}, function (task) {
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
let build_list_item = function (task) {
    if (task) {
        let new_item_HTMLDoc = '<li class=\"item item_' + task.id + '\" id=\"item_' + task.id + '\">\n' +
            '                        <table cellpadding=\"0\" cellspacing=\"0\">\n' +
            '                            <tbody>\n' +
            '                            <tr>\n' +
            '                                <td class=\"item_checker\">\n' +
            '                                    <div class=\"ist_checkbox\"><input type=\"checkbox\" name=\"finished\" id=\"item_checked_' + task.id + '\"/></div>\n' +
            '                                </td>\n' +
            '                                <td class=\"item_content\">\n' +
            '                                    <span class=\"text\">' + task.content + '</span>\n' +
            '                                </td>\n' +
            '                                <td class="menu dropdown">\n' +
            '                                    <div class="">\n' +
            '                                    <span class="icon glyphicon glyphicon-option-vertical menu_icon" data-toggle="dropdown">\n' +
            '                                    </span>\n' +
            '                                    <ul class="dropdown-menu dropdown-menu-right">\n' +
            '                                        <li><a href="#" class="delete" id="item_delete_' + task.id + '">删除任务</a></li>\n' +
            '                                    </ul>\n' +
            '                                    </div>\n' +
            '                                </td>\n' +
            '                            </tr>\n' +
            '                            </tbody>\n' +
            '                        </table>\n' +
            '                    </li>';
        // var firstItem = $("#list_items").children(":first");
        // $(new_item_HTMLDoc).insertBefore(firstItem);
        let add_task = $("#details");
        $(new_item_HTMLDoc).insertBefore(add_task);
        //$('#list_items').append(new_item_HTMLDoc);
    }
}

$('#list_items').on("click", ".cancel", function () {
    $('.details').hide();
});

$('.controller_add').click(function () {
    let details = $('#details'),
        editor = $('.editor');
    editor.hide();
    $('.editor').next().show();
    details.show();
    details.find(".new_text").focus();
});

//已完成任务
$('#list_items').on("click", ".ist_checkbox", function () {
    let item_checked_id = $(this).find('input').attr("id"),
        len = item_checked_id.length,
        id = item_checked_id.substring(13, len),
        item_id = "item_" + id;

    $.post("/toDoList/", {"finished_id": id}, function () {
        $("#" + item_id).hide();
    });

});
//删除任务
$('#list_items').on("click", ".delete", function () {
    let item_delete_id = $(this).attr("id"),
        len = item_delete_id.length,
        id = item_delete_id.substring(12, len),
        item_id = "item_" + id;

    $.post("/toDoList/", {"delete_id": id}, function () {
        $("#" + item_id).remove();
    });

});

//修改内容
$('#list_items').on("click", ".item_content", function () {
    //让添加任务隐藏
    let details = $('#details');
    if (details.css("display") == "list-item")
        details.hide();
    //让原item隐藏
    let item_id = $(this).closest('li').attr("id"),
        len = item_id.length,
        id = item_id.substring(5, len),
        item = $("#" + item_id);
    item.hide();

    let editor = $('.editor');
    if (editor.css("display") == "list-item") {
        editor.next().show();
    }

    editor.insertBefore(item);

    //复制原有内容
    let orig_text_node = item.find('.item_content .text'),
        orig_text = orig_text_node.text(),
        modified_text_node = editor.find('.new_task_content .new_text');
    modified_text_node.text(orig_text);
    editor.show();
});
//取消修改
$('.editor').find('.cancel').click(function () {
    let editor = $('.editor');
    editor.hide();
    editor.next().show();

});
$('.editor').find('.ist_btn').click(function () { //点击保存
    let editor = $('.editor');
    let text = editor.find('.new_task_content .new_text').text();
    let item = editor.next(),
        item_id = item.attr("id"),
        len = item_id.length,
        id = item_id.substring(5, len);

    $.post("/toDoList/", {"modified_id": id, "modified_content": text}, function () {
        item.find('.item_content .text').text(text);
        editor.hide();
        item.show();
    });
});