function heightChange() {
  heightNumberButton = document.getElementById("height_button");
  heightNumberButton.value
  heightNumber = heightNumberButton.value;
}

function createBaseImg(x, y) {
  var img = document.createElement("img");
  img.src = "https://a248.e.akamai.net/assets.github.com/images/icons/emoji/arrow_up.png"; 
  img.id= x + "_" + y + "_" + "emoji";
  img.alt=":arrow_up:";
  img.class = "emoji"; 
  img.draggable="true";
  img.height="20";
  img.width="20";
  img.align="absmiddle";
  img.setAttribute("ondragstart", "f_dragstart(event)");
  return img;
}

function createImg(x, y) {
  var img = document.createElement("img");
  img.src = "https://a248.e.akamai.net/assets.github.com/images/icons/emoji/arrow_down.png"; 
  img.id= x + "_" + y + "_" + "emoji";
  img.alt=":arrow_down:";
  img.class = "emoji"; 
  img.draggable="true";
  img.height="20";
  img.width="20";
  img.align="absmiddle";
  img.setAttribute("ondragstart", "f_dragstart(event)");
  return img;
}

function createDropboxDiv(id) {
  var div = document.createElement("span");
  div.id = id;
  div.setAttribute("ondragover", "f_dragover(event)");
  div.setAttribute("ondrop", "f_drop(event)");
  return div
}

function generate() {
  width = document.getElementById("width_button").value;
  height = document.getElementById("height_button").value;
  pElement = document.getElementById("p_element");

  for (y=0;y<height;y++) {
    for (x=0;x<width;x++) {
      var div = createDropboxDiv(x+"_"+y+"_"+"dropbox")
      var img = createBaseImg(x, y);
      div.appendChild(img);
      pElement.appendChild(div);
    }
    var br = document.createElement("br")
    pElement.appendChild(br);
  }

  dropbox = document.getElementById("dropbox");
  for (y=0;y<height;y++) {
    for (x=0;x<width;x++) {
      var img = createImg(x, y);
      dropbox.appendChild(img);
    }
    var br = document.createElement("br")
    dropbox.appendChild(br);
  }

}


function f_dragstart(event){
  event.dataTransfer.setData("text", event.target.id);
}

function f_dragover(event){
  event.preventDefault();
}

function f_drop(event){
  var id_name = event.dataTransfer.getData("text");
  console.log(id_name);
  var drag_elm =document.getElementById(id_name);
  event.currentTarget.appendChild(drag_elm);
  event.preventDefault();
}
