let textareaList = document.getElementsByClassName("info")[0].getElementsByClassName("textarea");
let editBtn = document.getElementsByClassName("edit")[0];
let postEditBtnList = document.getElementsByClassName("postedit");

editBtn.addEventListener("click", () => {
    editBtn.style.display = "none";
    Array.from(postEditBtnList).forEach(element => {
        element.style.display = "block";
    });
    Array.from(textareaList).forEach(element => {
        element.removeAttribute("readonly");
        element.style.backgroundColor = "white";
    })
});

let cancelBtn = postEditBtnList[0];

cancelBtn.addEventListener("click", () => {
    editBtn.style.display = "block";
    Array.from(postEditBtnList).forEach(element => {
        element.style.display = "none";
    });
    Array.from(textareaList).forEach(element => {
        element.setAttribute("readonly" ,"");
    })
    location.reload();
});

let textarea2 = document.getElementsByClassName("acc-container")[0].getElementsByClassName("editable")[0];
let editBtn2 = document.getElementsByClassName("edit2")[0];
let postEditBtnList2 = document.getElementsByClassName("postedit2");

editBtn2.addEventListener("click", () => {
    editBtn2.style.display = "none";
    Array.from(postEditBtnList2).forEach(element => {
        element.style.display = "block";
    });
    textarea2.removeAttribute("readonly");
    textarea2.style.backgroundColor = "white";
});

let cancelBtn2 = postEditBtnList2[0];

cancelBtn2.addEventListener("click", () => {
    editBtn2.style.display = "block";
    Array.from(postEditBtnList2).forEach(element => {
        element.style.display = "none";
    });
    textarea2.setAttribute("readonly" ,"");
    location.reload();
});


// Submitting Information

var data = [];

function sendReq(reqType) {
    if (reqType === "acc_edit"){
        let editable = document.getElementsByClassName("textarea2 editable")[0];
        data.push(editable.value);

    } else if (reqType === "user_edit") {
        let textareaList = document.getElementsByClassName("textarea");
        Array.from(textareaList).forEach(elmt => {
            data.push(elmt.value);
        });
    }

    $.ajax({
        type: "POST",
        url: "",
        data: JSON.stringify({"req": reqType, "info": data}),
        contentType: "application/json",
        success: function(){
            if(reqType === 'acc_edit'){
                top.location.href = "";
            } else if (reqType === 'user_edit'){
                top.location.href = "";
            }
        } 
    });
}

let acc = document.getElementById('acc');
let cus = document.getElementById('cus');
let his = document.getElementById('his');
let con1 = document.getElementsByClassName('container1')[0];
let con2 = document.getElementsByClassName('container2')[0];
let con3 = document.getElementsByClassName('container3')[0];

acc.addEventListener('click', function() {
    acc.style.color = "#B73E3E";
    con1.style.display = 'flex';
    con2.style.display = 'none';
    con3.style.display = 'none';
    cus.style.color = "grey";
    his.style.color = "grey";
});

cus.addEventListener('click', function() {
    cus.style.color = "#B73E3E";
    con1.style.display = 'none';
    con2.style.display = 'flex';
    con3.style.display = 'none';
    acc.style.color = "grey";
    his.style.color = "grey";
});

his.addEventListener('click', function() {
    his.style.color = "#B73E3E";
    con1.style.display = 'none';
    con2.style.display = 'none';
    con3.style.display = 'flex';
    cus.style.color = "grey";
    acc.style.color = "grey";
});
