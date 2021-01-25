const account_menu = document.getElementById("account-menu");
account_menu.style.display = "none";
const conpanyLink = document.getElementById("conpanylink")
document.getElementById("edit-user-info").onclick = function (){
    const account_menu_area = document.getElementById("account-menu-area");
    if(account_menu.style.display == "none"){
        conpanyLink.style.height = "38%";
        account_menu.style.display = "block";
        detail_area.style.display = "none";
        document.getElementById("edit-user-info").style.transform = "rotate(90deg)";
    }else{
        conpanyLink.style.height = "58%";
        account_menu.style.display = "none";
        document.getElementById("edit-user-info").style.transform = "rotate(0deg)";
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
    conpanyLink.style.height = "58%";
    document.getElementById("edit-user-info").style.transform = "rotate(0deg)";
    if(target.style.display == "none"){
        target.style.display = "block";
    }else{
        target.style.display = "none";
    }
}

// 自分史新規登録モーダル
const motivation_modal = document.getElementById("motivation-modal");
motivation_modal.style.display = "none";
const open_modal = document.getElementById("open-modal");
open_modal.onclick = function (){
    if(motivation_modal.style.display == "none"){
        motivation_modal.style.display = "block"
    }
}

const motivation_modal_close = document.getElementById("motivation-modal-close");
motivation_modal_close.onclick = function (){
    if(motivation_modal.style.display == "block"){
        motivation_modal.style.display = "none"
    }
}

// 自分史編集モーだる
const jibunshi_modal_close = document.getElementById("jibunshi-modal-close");
jibunshi_modal_close.onclick = function (){
    if(jibunshi_modal.style.display == "block"){
        jibunshi_modal.style.display = "none"
    }
}