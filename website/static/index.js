
function showFlashMessage(element) {
  var event = new CustomEvent('showFlashMessage');
  element.dispatchEvent(event);
};

var flashMessages = document.getElementsByClassName('js-flash-message');
//show first flash message avilable in your page
showFlashMessage(flashMessages[0]);

function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
