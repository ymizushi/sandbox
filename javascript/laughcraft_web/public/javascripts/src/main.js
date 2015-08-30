function main() {
  var scene = new THREE.Scene();
  var renderer = new THREE.WebGLRenderer();
  var container = createContainer();
  var camera = createCamera();
  var clock = new THREE.Clock();
  var score = new LAUGH.ScoreLoader().load(1);
  var lookatObject = new THREE.Vector3(0, 0, 0);

  // timer
  var timerCounter=0;
  var bpm = 60;
  var secondPerBeat = 60/bpm;
  var keyframeLoopCount = 0;

  // システム関連の処理
  init(container, camera, scene, renderer, score);

  var animate = function () {
    requestAnimationFrame(animate);

    var delta = clock.getDelta();
    timerCounter += delta;

    // キーフレームカウントアップ処理
    if (timerCounter >= secondPerBeat) {
      keyframeLoopCount += 1;
      timerCounter = 0;
    }

    setCameraDirection(camera, lookatObject, score, keyframeLoopCount, delta, secondPerBeat);

    renderer.render(scene, camera);
  }
  animate();
}

function createCamera() {
  var camera = new THREE.OrthographicCamera(window.innerWidth/-2, window.innerWidth/2, window.innerHeight/2, window.innerHeight/-2, -500, 1000);
  camera.position.x = -500;
  camera.position.y = 0;
  camera.position.z = 0;
  return camera;
}

function createContainer() {
  var container = document.createElement('div');
  document.body.appendChild(container);

  var info = document.createElement('div');
  info.style.position = 'absolute';
  info.style.top = '10px';
  info.style.width = '100%';
  info.style.textAlign = 'center';
  container.appendChild(info);
  return container;
}

function createLineFrame(pianorollSize, step) {
  var geometry = new THREE.Geometry();
    for (var x = 0; x <= pianorollSize["width"]; x += step ) {
      geometry.vertices.push(new THREE.Vector3(x, 0, 0));
      geometry.vertices.push(new THREE.Vector3(x, 0, pianorollSize["depth"]));
    }
    for (var z = 0; z <= pianorollSize["depth"]; z += step) {
      geometry.vertices.push(new THREE.Vector3(0, 0, z));
      geometry.vertices.push(new THREE.Vector3(pianorollSize["width"], 0, z));
    }

  var material = new THREE.LineBasicMaterial( { color: 0x000000, opacity: 0.8 } );

  var line = new THREE.Line(geometry, material);
  line.type = THREE.LinePieces;
  return line;
}

function addLight(scene) {
  var ambientLight = new THREE.AmbientLight( Math.random() * 0x10 );
  scene.add( ambientLight );

  var directionalLight = new THREE.DirectionalLight( Math.random() * 0xffffff );
  directionalLight.position.x = Math.random() - 0.5;
  directionalLight.position.y = Math.random() - 0.5;
  directionalLight.position.z = Math.random() - 0.5;
  directionalLight.position.normalize();
  scene.add( directionalLight );

  var directionalLight = new THREE.DirectionalLight( Math.random() * 0xffffff );
  directionalLight.position.x = Math.random() - 0.5;
  directionalLight.position.y = Math.random() - 0.5;
  directionalLight.position.z = Math.random() - 0.5;
  directionalLight.position.normalize();
  scene.add( directionalLight );
}

function onWindowResize(camera, renderer) {
  return function () {
    camera.left = window.innerWidth / - 2;
    camera.right = window.innerWidth / 2;
    camera.top = window.innerHeight / 2;
    camera.bottom = window.innerHeight / - 2;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
  };
}

function setDeltaPosition(targetPosition, position, frameNum, nextPosition, nextFrameNum, secondPerFrame, deltaTime) {
  var deltaFrame = nextFrameNum - frameNum;
  var totalSecond = deltaFrame * secondPerFrame;
  var divider = totalSecond/deltaTime;
  var deltaX = (nextPosition.x - position.x)/divider;
  var deltaY = (nextPosition.y - position.y)/divider;
  var deltaZ = (nextPosition.z - position.z)/divider;
  targetPosition.x = position.x+deltaX;
  targetPosition.y = position.y+deltaY;
  targetPosition.z = position.y+deltaZ;
}

function setCameraDirection(camera, lookatObject, score, keyframeLoopCount, delta, secondPerBeat) {
  var keyframeList = score.getKeyframeList();
  var keyframeLength = keyframeList.length;
  var keyframeCamera = keyframeList[keyframeLoopCount % keyframeLength]["camera"];
  var frameNum = keyframeCamera["frameNum"];
  var executedLoopNum = secondPerBeat/delta
  var position = keyframeCamera["position"];
  var lookat   = keyframeCamera["lookat"];

  lookatObject.x += lookat[0]/frameNum/executedLoopNum;
  lookatObject.y += lookat[1]/frameNum/executedLoopNum;
  lookatObject.z += lookat[2]/frameNum/executedLoopNum;
  
  camera.lookAt(lookatObject);
  camera.position.x += position[0] /frameNum/executedLoopNum;
  camera.position.y += position[1] /frameNum/executedLoopNum;
  camera.position.z += position[2] /frameNum/executedLoopNum;
}

function createScore() {
  // 今は使っていないけど、将来必要になる関数群
  score.play(); // 音楽を再生するときはここをコメントイン
}

function createCubeList(score) {
  var geometry = new THREE.BoxGeometry(50, 50, 50);
  var material = new THREE.MeshLambertMaterial({color:0xffffff, shading:THREE.FlatShading, overdraw:0.5});
  var objectList = score.getObjectList();

  var cubeList = [];
  for (var i=0; i<objectList.length; i++) {
    var cube = new THREE.Mesh(geometry, material);
    cube.position.x = objectList[i]["point"][0] * 50+25;
    cube.position.y = objectList[i]["point"][1] * 50+25;
    cube.position.z = objectList[i]["point"][2] * 50+25;
    cubeList.push(cube);
  }
  return cubeList
}

function createMarker() {
  var geometry = new THREE.PlaneGeometry(50, 600, 72, 12);
  var material = new THREE.MeshLambertMaterial( { color: 0xffffff, shading: THREE.FlatShading, overdraw: 0.5 } );

  var cube = new THREE.Mesh(geometry, material );
  cube.rotateZ(Math.PI/2);
  cube.rotateY(Math.PI/2);
  cube.rotateZ(Math.PI/2);

  cube.position.x = -75;
  cube.position.y = -50;
  cube.position.z = 200;
  return cube
}

function createRoop() {
  var geometry = new THREE.SphereGeometry(10, 10, 10);
  var material = new THREE.MeshLambertMaterial( { color: 0xffffff, shading: THREE.FlatShading, overdraw: 0.5 } );

  var roop = new THREE.Mesh(geometry, material );
  roop.scale.x = 5;
  roop.scale.y = 5;
  roop.scale.z = 5;
  roop.position.x = -75;
  roop.position.y = -50;
  roop.position.z = 200;
  return roop
}

function addObjects(scene, score) {
 // マーカを作成して、scenenに追加
  scene.add(createMarker());
  addLight(scene);

  // ノートキューブを追加
  var cubeList = createCubeList(score);
  for ( var i = 0; i < cubeList.length; i++ ) {
    scene.add(cubeList[i]);
  }

  // グリッドラインを追加
  var cubeSize = 50;
  var pianorollSize = {"width": 3600, "depth": 600};
  var line = createLineFrame(pianorollSize, cubeSize);
  scene.add(line);
}

// 全体の初期化を行う
function init(container, camera, scene, renderer, score) {
  addObjects(scene, score);

  // レンダラー初期化
  renderer.setClearColor(0xf0f0f0);
  renderer.setSize(window.innerWidth, window.innerHeight);

  container.appendChild(renderer.domElement);

  // ベンチマーカー初期化
  var stats = new Stats();
  stats.domElement.style.position = 'absolute';
  stats.domElement.style.top = '0px';
  container.appendChild(stats.domElement);

  window.addEventListener('resize', onWindowResize(camera, renderer), false );
}

main();
