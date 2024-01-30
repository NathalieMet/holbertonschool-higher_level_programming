const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', function onClick(event) {

	const header = document.body.querySelector("header");
	header.classList.add("red");
  });
