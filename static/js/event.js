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
