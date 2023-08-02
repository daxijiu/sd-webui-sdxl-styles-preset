onUiLoaded(() => {
	document.addEventListener("DOMContentLoaded", document.getElementById('txt2img_sampling').before(document.getElementById('txt2img_sdxl_style_preset')));
	document.addEventListener("DOMContentLoaded", document.getElementById('img2img_sampling').before(document.getElementById('img2img_sdxl_style_preset')));
});

