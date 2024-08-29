document.addEventListener("DOMContentLoaded", function() {
    var video = document.getElementById('video');
    
    if (Hls.isSupported()) {
        var hls = new Hls();
        hls.loadSource('/stream/output.m3u8');
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function() {
            document.addEventListener('click', function() {
                video.play();
            }, { once: true }); // Escuta apenas uma vez a interação
        });
    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = '/stream/output.m3u8';
        video.addEventListener('canplay', function() {
            document.addEventListener('click', function() {
                video.play();
            }, { once: true });
        });
    }
});
