/*
 * appjs.
 */
 
/*操作返回状态接收和操作结果提示*/
function parse_result(data) {
    if (data) {
        toastr.success('Action Success');
        console.log(data)
    } else {
        toastr.error('Action Failed');
    }
}


/*控制左侧sidebar展开和标签选中状态*/
window.onload = function() { 
var url = document.location.toString();
var pathname = window.location.pathname;
var showItem =pathname.substring(1,pathname.length-1);
var checkItem = "#nav-"+showItem;

  $(checkItem).parents("ul").collapse();
  $(checkItem).css('background','#428bca');
  $(checkItem).css('color','#FFF8F1');
 
}
