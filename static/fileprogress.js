function _(el) {
  return document.getElementById(el);
}

function uploadFile(filename="file") {
  console.log(_(filename));
  var file = _(filename).files[0];
  // alert(file.name+" | "+file.size+" | "+file.type);
  var formdata = new FormData();
  formdata.append(filename, file);
  var ajax = new XMLHttpRequest();
  ajax.upload.addEventListener("progress", progressHandler, false);
  ajax.addEventListener("load", completeHandler, false);
  ajax.open("POST", "file_upload_parser.php"); // http://www.developphp.com/video/JavaScript/File-Upload-Progress-Bar-Meter-Tutorial-Ajax-PHP
  //use file_upload_parser.php from above url
  ajax.send(formdata);
}

function progressHandler(event) {
  var percent = (event.loaded / event.total) * 100;
  $("#progressBar").css('width', Math.round(percent)+'%');
}

function completeHandler(event) {
  $("#progressBar").css('width', '100%'); //wil clear progress bar after successful upload
}