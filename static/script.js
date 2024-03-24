$(document).ready(function () {
  refreshMeme();

  $("#refresh-btn").click(function () {
    refreshMeme();
  });
});

function refreshMeme() {
  $.ajax({
    url: "/meme",
    type: "GET",
    success: function (data) {
      $("#meme-image").attr("src", data.meme_url);
    },
    error: function () {
      alert("An error occurred while fetching the meme.");
    },
  });
}
