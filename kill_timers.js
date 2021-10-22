function timerKiller(){
  var lastCleanedBorder = 0;
  
  return function () {
      var id = window.setTimeout(function() {}, 0);
      for(var i = lastCleanedBorder; i <= id; i++) {
        window.clearTimeout(i);
      }
      lastCleanedBorder = id + 1;
      console.log(lastCleanedBorder);
  }
}
