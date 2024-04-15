document.addEventListener("DOMContentLoaded", function () {
  var quoteElement = document.querySelector("p");
  var quoteText = quoteElement.innerText;
  var maxLength = 3000;
  var breakLength = 50; // 50자마다 줄바꿈 (예시)
  if (quoteText.length > maxLength) {
    quoteText = quoteText.substring(0, maxLength);
  }
  var newText = "";
  for (var i = 0; i < quoteText.length; i += breakLength) {
    newText += quoteText.substring(i, i + breakLength) + "\n" + "\n";
  }
  quoteElement.innerText = newText;
});
