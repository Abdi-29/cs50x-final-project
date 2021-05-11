function deleteVideo(videoId) {
    fetch("/delete-video", {
      method: "POST",
      body: JSON.stringify({ videoId: videoId }),
    }).then((_res) => {
      window.location.href = "/video/edit";
    });
  }