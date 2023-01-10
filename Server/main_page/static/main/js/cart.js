var modal = document.getElementsByClassName('modal')[0];
var title = document.getElementById("item-id");
var span = document.getElementsByClassName("close")[0];
var form = document.getElementsByTagName('form')[0];
var btn = document.getElementsByClassName('confirm-btn')[0];
var ids = [];
var item = null;


function openModal(element, str) {
    item = element.getElementsByClassName("id")[0].innerHTML;
    title.innerHTML = "Item ID: " + item;
    ids = str.split('-');
    modal.classList.add('visible');
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.classList.remove('visible');
        item = null;
        ids = [];
    }
}

span.onclick = function() {    
    modal.classList.remove('visible');
    item = null;
    ids = [];
}

window.addEventListener("load", (event) =>{
    modal.style.cssText = "transition: opacity 0.2s 0s ease-in-out,transform 0.2s 0s ease-in-out;";
})

function sendReq(reqType) {
    $.ajax({
        type: "POST",
        url: "",
        data: JSON.stringify({"req": reqType, "itemID": ids[0], "instID": ids[1]}),
        contentType: "application/json",
        success: function(){
            if(reqType === 'edit'){
                top.location.href = "redirect/custom/" + ids[0] + "/" + ids[1];
            } else if (reqType === 'remove'){
                location.reload();
            } else if (reqType === 'confirm'){
                top.location.href = "";
            }
          
        } 
      });
}

