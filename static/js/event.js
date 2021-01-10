// $(function () {
//   $('#open').click(function(){
//       $('#modalArea').fadeIn();
//   });
//   $('#close , #e_mask').click(function(){
//     $('#modalArea').fadeOut();
//   });
// });

var btn = document.getElementById('open_btn');
var modal = document.getElementById('modalArea');
var closeBtn = document.getElementById('close_modal');

const test = document.querySelectorAll(".event_ogata_box");
const owari = document.querySelectorAll(".event_1_box_class_checked");


btn.addEventListener('click', function() {
  modal.style.display = 'block';
  document.getElementById("action_type").value = 'add_event';
});

closeBtn.addEventListener('click', function() {
  modal.style.display = 'none';
  document.getElementById("action_type").value = 'update-company-data';
});

window.addEventListener('click', function(e) {
    if (e.target == modal) {
      modal.style.display = 'none';
      document.getElementById("action_type").value = 'update-company-data';
    }
});

const event_box = document.getElementById('event_box');

// 打ち消し線を出すところ
test.forEach(function(target) {
  target.addEventListener('click', () => {
  　target.classList.toggle('event_1_box_class_checked');
  　});
});

// function eventTitleClick(e) {
  // document.div.insertBefore(test, owari);
  // console.log(e.target)
  // console.log(event_box.childNodes[1]);
  // event_box.appendChild(event_box.childNodes[1])
  // event_box.appendChild(e.target);
  
// }

function eventTitleClick(e) {
  event_box.appendChild(e.target.parentNode.parentNode);
}

// ▼削除
flow_box = document.getElementById('flow_box');
remove_triangle = flow_box.lastElementChild.lastElementChild;
remove_triangle.remove();


/*イベント編集に関して**/
const menus = document.getElementsByClassName("edit_menu")
for(var i = 0; i < menus.length; i++) {
  menus[i].style.display = "none";
}
function eventEditMode(e){
  // console.log(e.currentTarget);
  const currentTarget = e.currentTarget;
  // console.log(currentTarget.nextElementSibling);
  const editMenu = currentTarget.nextElementSibling
  if(editMenu.style.display == "none"){
    editMenu.style.display = "block";
  }else{
    editMenu.style.display = "none";
  }
}
/*イベント削除*/
const askDeleteArea = document.getElementsByClassName("askDeleteWindow")
for(var i = 0; i < askDeleteArea.length; i++) {
  askDeleteArea[i].style.display = "none";
}
function openDeleteEventWindow(e){
  console.log(e.target.parentNode.parentNode.parentNode);
  const eventBox = e.target.parentNode.parentNode.parentNode;
  /*以下のコメントの要素が対応するイベント削除モーダルの要素*/
  // console.log(eventBox.previousElementSibling);
  if(eventBox.previousElementSibling.style.display == "none"){
    eventBox.previousElementSibling.style.display = "block";
    e.target.parentNode.style.display = "none"; //プロフィール編集と削除のウィンドウを消す
  }else{
    eventBox.previousElementSibling.style.display = "none";
    e.target.parentNode.style.display = "none"; //プロフィール編集と削除のウィンドウを消す
  }
}

/*イベント削除ウィンドウ内の戻るボタンに関する内容**/
function exitAskDeleteWindow(e){
  const window = e.target.parentNode.parentNode
  console.log(window);
  if(window.style.display == "none"){
    window.style.display = "block";
  }else{
    window.style.display = "none";
  }
}

/*イベント削除ウィンドウ内の削除ボタンに関する内容**/
function deleteEvent(e){
  const window = e.target.parentNode.parentNode
  document.getElementById('event_delete_form').submit();
  // document.delete_form.submit();
  console.log(window);
  if(window.style.display == "none"){
    window.style.display = "block";
  }else{
    window.style.display = "none";
  }
}
