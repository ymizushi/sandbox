function moveImg() {
  pelement = document.getElementById("p_element");

  // document.body.p.appendChild(img);
}

function widthChange() {
  widthNumberButton = document.getElementById("width_button");
  widthNumber = widthNumberButton.value;
}

function heightChange() {
  heightNumberButton = document.getElementById("height_button");
  heightNumberButton.value
  heightNumber = heightNumberButton.value;
}

function createImg() {
  var img = document.createElement("img")
  img.src = "https://a248.e.akamai.net/assets.github.com/images/icons/emoji/arrow_up.png"; 
  img.class = "emoji"; 
  img.title = ":arrow_up:"; 
  img.alt=":arrow_up:";
  img.height="20";
  img.width="20";
  img.align="absmiddle";
  return img;
}

function generate() {
  width = document.getElementById("width_button").value;
  height = document.getElementById("height_button").value;
  pElement = document.getElementById("p_element");
  console.log(pElement);

  img = createImg();

  for (y=0;y<height;y++) {
    for(x=0;x<width;x++) {
      var img = createImg();
      pElement.appendChild(img);
    }
    var br = document.createElement("br")
    pElement.appendChild(br);
  }
}

window.document.onclick = moveImg;
