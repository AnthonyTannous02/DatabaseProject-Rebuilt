let list = document.querySelectorAll(".list li");
let box = document.querySelectorAll(".box");

list.forEach((el)=>{
    el.addEventListener("click" , (e)=>{

        list.forEach((el1)=>{
            el1.style.color = "#000";
        })
        e.target.style.color = "#B73E3E"
        box.forEach((el2)=>{
            el2.style.display = "none";
        })
        document.querySelectorAll(e.target.dataset.color).forEach((el3)=>{
            el3.style.display = "flex";
        })
    })
})



let itemBoxList = document.querySelectorAll(".box");
itemBoxList.forEach((element) => {
element.addEventListener('click', function() {
    console.log();
    window.location.assign("/main/custom/" + element.getElementsByClassName("box-info")[0].getElementsByClassName("text")[0].getElementsByTagName("h3")[0].id);
})});

