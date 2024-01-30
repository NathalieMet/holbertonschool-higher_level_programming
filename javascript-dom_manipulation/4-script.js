const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function onClick(event) {
	const ul = document.querySelector(".my_list");
	const li = document.createElement("li");
	li.appendChild(document.createTextNode("Item"));
	ul.appendChild(li);
  });
