document.addEventListener('DOMContentLoaded', function () {

	fetch('https://swapi-api.hbtn.io/api/films/?format=json')
	.then(response => {
		if (!response.ok) {
			throw new Error(`HTTP error! Status: ${response.status}`);
		}
		return response.json();
	})
	.then(data => {
		showTitles(data.results);
		})
	.catch(error => {
		console.error('Error fetching data:', error.message);
		});

		function showTitles(titles) {
			const titleElement = document.getElementById('list_movies');
				titles.forEach(title => {
				  const newElement = document.createElement("li");
				  newElement.appendChild(document.createTextNode(title.title));
				  titleElement.appendChild(newElement);
				});
			}
		});
