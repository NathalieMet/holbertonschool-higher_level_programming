const getElement = document.getElementById('update_header');

getElement.addEventListener('click', function onClick(event) {
	const header = document.body.querySelector("header");
	header.innerText = "New Header!!!";
  });
