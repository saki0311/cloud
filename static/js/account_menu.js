const account_menu = document.getElementById("account-menu");
account_menu.style.display = "none";
document.getElementById("edit-user-info").onclick = function (){
    const conpanyLink = document.getElementById("conpanylink")
    const account_menu_area = document.getElementById("account-menu-area");
    if(account_menu.style.display == "none"){
        conpanyLink.style.height = "55%";
        // account_menu_area.style.display = "25%";
        account_menu.style.display = "block";
        detail_area.style.display = "none";
    }else{
        conpanyLink.style.height = "75%";
        // account_menu_area.style.display = "10%";
        account_menu.style.display = "none";
    }
}

const triple_dot = document.getElementsByClassName("triple_dot");
const detail_area = document.getElementById("detail-area");
detail_area.style.display = "none";
function detailDisplay(){
    if(detail_area.style.display == "none"){
        detail_area.style.display = "block";
    }else{
        detail_area.style.display = "none";
    }
}
document.getElementById("profile-edit-window").style.display = "none";
document.getElementById("exit-profile-window").onclick = function (){
    const target = document.getElementById("profile-edit-window");
    if(target.style.display == "none"){
        target.style.display = "block";
    }else{
        target.style.display = "none";
    }
}

function profileEditDisplay(){
    const target = document.getElementById("profile-edit-window");
    account_menu.style.display = "none";
    detail_area.style.display = "none";
    if(target.style.display == "none"){
        target.style.display = "block";
    }else{
        target.style.display = "none";
    }
}