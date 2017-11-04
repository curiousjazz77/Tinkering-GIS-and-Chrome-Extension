

function click(e) {
	chrome.tabs.executeScript(null, 
		{code:"document.body.style.backgroundImage='url(" + images[e.target.id]
			+ "'"});
	window.close();
}

document.addEventListener('DOMContentLoaded', function() {
	var divs = document.querySelectorAll('div');
	for (var i = 0; i < divs.length; i++) {
		divs[i].addEventListener('click', click);
	}
});

var images = {
	chatting: 'https://i.pinimg.com/originals/1b/0b/10/1b0b10eccf85153fe0e6f7af53633a3f.jpg',
	laughing: 'https://pbs.twimg.com/media/BaYQtwXIIAAo6FF.jpg',
	rattling: 'https://i.pinimg.com/736x/e9/ef/3c/e9ef3cfd8ff0f93d6f56ceca33383301--pusheen-love-kawaii-pusheen.jpg'
}