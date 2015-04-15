code_show=true;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}

$([IPython.events]).on("app_initialized.NotebookApp", function () {
  $("#view_menu").append("<li id=\"toggle_toolbar\" title=\"Show/Hide code cells\"><a href=\"javascript:code_toggle()\">Toggle Code Cells</a></li>");
});