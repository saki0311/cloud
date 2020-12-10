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

const test = document.querySelectorAll(".event_1_box");
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

function eventTitleClick(e) {
  // document.div.insertBefore(test, owari);
  // console.log(e.target)
  // console.log(event_box.childNodes[1]);
  // event_box.appendChild(event_box.childNodes[1])
  // event_box.appendChild(e.target);
  
}

function moveEvent(e){
  // console.log(e.currentTarget);
  event_box.appendChild(e.currentTarget);
}

// ▼削除
flow_box = document.getElementById('flow_box');
remove_triangle = flow_box.lastElementChild.lastElementChild;
remove_triangle.remove();
