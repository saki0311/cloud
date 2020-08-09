// クリップボードコピーを行う関数
function copyToClipboard(){
    // テキストエリアを生成するdivを取得
    const mypage_id = document.getElementById("mypage_id");
    // 中身が空の場合
    if(!mypage_id.hasChildNodes()){
      // テキストエリアオブジェクトを生成
      const input = document.createElement("textarea");
      // テキストエリアの内容をIDに
      input.textContent=JSON.parse(document.getElementById("test").textContent).con;
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