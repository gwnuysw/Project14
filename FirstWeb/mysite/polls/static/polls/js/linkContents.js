jQuery(document).ready(function(){
  var coll = document.getElementsByTagName("button");
  var i;
  console.log("js is running");
  console.log(coll.length);
  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      console.log("clicked");
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      console.log(content);
      console.log(content.style.maxHeight);
      if (content.style.maxHeight){
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }
 });
