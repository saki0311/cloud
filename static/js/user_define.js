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