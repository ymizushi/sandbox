
function moveImg() {
  var img = document.createElement("img")
  img.src = "https://a248.e.akamai.net/assets.github.com/images/icons/emoji/u5408.png"; 
  img.name = "hoge";
  img.draggable = true;
  document.body.appendChild(img);
}

window.document.onclick = moveImg;
