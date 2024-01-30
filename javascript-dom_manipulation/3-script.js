const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function onClick(event) {
	const header = document.querySelector('header');

	if (header.classList.contains('red')) {
	header.classList.replace("red", "green");
	}
	else if (header.classList.contains('green')) {
	header.classList.replace("green", "red");
	}
  });
