var startTime;
var clickCount = 0;

window.onload = function() {
    startTime = new Date();

    // Add click event listener to the button
    document.getElementById("scrollToBottomButton").addEventListener("click", function() {
        clickCount++;
        scrollToBottom();
    });
};

window.onunload = function() {
    var endTime = new Date();
    var timeSpent = endTime - startTime;
    console.log("Time spent on the site: " + (timeSpent / 1000) + " seconds");
    console.log("Button clicks: " + clickCount);
    // You can send this timeSpent data to your server for further analysis or processing.
};

function scrollToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
}