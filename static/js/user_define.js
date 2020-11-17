// クリップボードコピーを行う関数
function copyToClipboard(){
    // テキストエリアを生成するdivを取得
    const mypage_id = document.getElementById("mypage_id");
    // 中身が空の場合
    if(!mypage_id.hasChildNodes()){
      // テキストエリアオブジェクトを生成
      const input = document.createElement("textarea");
      // テキストエリアの内容をIDに
      input.textContent=JSON.parse(document.getElementById("copy_text").textContent).con;
      // テキストエリアにidを付与
      input.id = "copyTarget";
      // テキストエリアを指定したdivに生成（子ノードとして）
      mypage_id.appendChild(input);
        
      // テキストエリアの内容を読み取る
      var textarea = document.getElementsByTagName("textarea")[0];
      // テキストエリアの文字を選択状態に
      textarea.select();
      // コピーを実行
      document.execCommand("copy");
      
      // 生成したテキストエリアを削除
      input.remove();
    }
  }

// モーダルウィンドウの処理（新規企業登録）
  (function(){
      'use strict';
      //[POINT]idを取得する
      var open = document.getElementById('open');
      var close = document.getElementById('close');
      var mask = document.getElementById('mask');
      var modal = document.getElementById('modal');
      //[POINT]クリックイベントを定義
      open.addEventListener('click',function(){
        //openではマスクとモーダル画面が表示できるようにする
        //[POINT]クラス名を変えてCSSを当て込まないようにする
        mask.className = '';
        modal.className = '';
        });
        close.addEventListener('click',function(){
         //closeではマスクとモーダル画面を非表示にする
         //[POINT]クラス名を再定義し、CSSを当て込む
          mask.className = 'hidden';
           modal.className = 'hidden';
        });
           //モーダル画面外をクリックしてもモーダル画面が閉じるようにする
        mask.addEventListener('click',function(){
        //closeと同じなので、closeのクリックイベントを呼び出せば良い
        close.click(); 
        //このように書くことができる
        });
    })();

// モーダルウィンドウの処理（予定追加）
(function(){
    'use strict';
    //[POINT]idを取得する
    var open = document.getElementById('open_event');
    var close = document.getElementById('close_event');
    var mask = document.getElementById('mask_event');
    var modal = document.getElementById('modal_event');
    //[POINT]クリックイベントを定義
    open.addEventListener('click',function(){
      //openではマスクとモーダル画面が表示できるようにする
      //[POINT]クラス名を変えてCSSを当て込まないようにする
      mask.className = '';
      modal.className = '';
      });
      close.addEventListener('click',function(){
       //closeではマスクとモーダル画面を非表示にする
       //[POINT]クラス名を再定義し、CSSを当て込む
        mask.className = 'hidden_event';
         modal.className = 'hidden_event';
      });
         //モーダル画面外をクリックしてもモーダル画面が閉じるようにする
      mask.addEventListener('click',function(){
      //closeと同じなので、closeのクリックイベントを呼び出せば良い
      close.click(); 
      //このように書くことができる
      });
  })();

  /******************************************************/
  /* SignIn SignOut SignUp                              */
  /******************************************************/
//   $('#signup').click(function() {
//     $('.movebox').css('transform', 'translateX(90%)');
//     $('.signin').addClass('nodisplay');
//     $('.signup').removeClass('nodisplay');
// });

// $('#signin').click(function() {
//     $('.movebox').css('transform', 'translateX(-5%)');
//     $('.signup').addClass('nodisplay');
//     $('.signin').removeClass('nodisplay');
// });
  /******************************************************/
  /* メニュー詳細表示操作                                */
  /******************************************************/

  const es_content = document.getElementById("ES").style.display;
  const flow_content = document.getElementById("flow").style.display;
  const event_content = document.getElementById("event").style.display;
  const memo_content = document.getElementById("memo").style.display;
  const edit_content = document.getElementById("editor").style.display;

  var page_param = JSON.parse(document.getElementById("copy_text").textContent).page;
  if (page_param){
    if (page_param == "event"){
      document.getElementById("ES").style.display = "none"; // ESメニューも隠す
      document.getElementById("flow").style.display = "none"; // ESメニューも隠す
      document.getElementById("memo").style.display = "none"; // ESメニューも隠す
      document.getElementById("editor").style.display = "none"; // ESメニューも隠す
    } else {
      document.getElementById("ES").style.display = "none"; // ESメニューも隠す
      document.getElementById("flow").style.display = "none"; // ESメニューも隠す
      document.getElementById("event").style.display = "none"; // イベントメニューは隠す
      document.getElementById("memo").style.display = "none"; // ESメニューも隠す
      document.getElementById("editor").style.display = "none"; // ESメニューも隠す
    }
  } else {
    document.getElementById("ES").style.display = "none"; // ESメニューも隠す
    document.getElementById("flow").style.display = "none"; // ESメニューも隠す
    document.getElementById("event").style.display = "none"; // イベントメニューは隠す
    document.getElementById("memo").style.display = "none"; // ESメニューも隠す
    document.getElementById("editor").style.display = "none"; // ESメニューも隠す
  }

  function click_es(){
    const elem = document.getElementById("ES");
    if(elem.style.display==es_content){
      elem.style.display = "none";
    } else {
      elem.style.display = es_content;
      document.getElementById("flow").style.display = "none";
      document.getElementById("event").style.display = "none";
      document.getElementById("memo").style.display = "none";
      document.getElementById("editor").style.display = "none";
    }
  }

  function click_flow(){
    const elem = document.getElementById("flow");
    if(elem.style.display==flow_content){
      elem.style.display = "none";
    } else {
      elem.style.display = flow_content;
      document.getElementById("ES").style.display = "none";
      document.getElementById("event").style.display = "none";
      document.getElementById("memo").style.display = "none";
      document.getElementById("editor").style.display = "none";
    }
  }

  function click_event(){
    const elem = document.getElementById("event");
    if(elem.style.display==event_content){
      elem.style.display = "none";
    } else {
      elem.style.display = event_content;
      document.getElementById("ES").style.display = "none";
      document.getElementById("flow").style.display = "none";
      document.getElementById("memo").style.display = "none";
      document.getElementById("editor").style.display = "none";
    }
  }

  function click_memo(){
    const elem = document.getElementById("memo");
    if(elem.style.display==memo_content){
      elem.style.display = "none";
    } else {
      elem.style.display = memo_content;
      document.getElementById("ES").style.display = "none";
      document.getElementById("flow").style.display = "none";
      document.getElementById("event").style.display = "none";
      document.getElementById("editor").style.display = "none";
    }
  }

  function click_edit(){
    const elem = document.getElementById("editor");
    if(elem.style.display==edit_content){
      elem.style.display = "none";
    } else {
      elem.style.display = edit_content;
      document.getElementById("ES").style.display = "none";
      document.getElementById("flow").style.display = "none";
      document.getElementById("event").style.display = "none";
      document.getElementById("memo").style.display = "none";
    }
  }

  /******************************************************/
  /* GoogleCalendar追加関数                              */
  /******************************************************/
  // 開始時間がなければ24時間前に初期設定
  function addToGoogleCalendar(){
    var text = document.getElementById('event_name').textContent;
    var company_time = document.getElementById('company_time').textContent.split('-');
    var start_date = Date.parse(company_time[0]);
    var end_date = Date.parse(company_time[1]);
    var description = document.getElementById('company_description').textContent;

    var zero = function(n) { return ('0' + n).slice(-2); };
    var formatdate = function(datestr) {
        var date = new Date(datestr + '+09:00');
        return date.getUTCFullYear() + zero(date.getUTCMonth()+1) + zero(date.getUTCDate()) + 'T' + 
                zero(date.getUTCHours()) + zero(date.getUTCMinutes()) + zero(date.getUTCSeconds()) + 'Z';
        };  
    var url = 'http://www.google.com/calendar/event?action=TEMPLATE' +
              '&text=' + encodeURIComponent(text) +
              '&dates=' + formatdate(company_time[0]) + '/' + formatdate(company_time[1]) + 
              '&details=' + description;

    window.open(url);
}
