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
});

closeBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

window.addEventListener('click', function(e) {
    if (e.target == modal) {
      modal.style.display = 'none';
    }
});

// 打ち消し線を出すところ
test.forEach(function(target) {
  target.addEventListener('click', () => {
  　target.classList.toggle('event_1_box_class_checked');
  　});
});

function moveEvent(e){
  // console.log(e.currentTarget);
  event_box.appendChild(e.currentTarget);
}