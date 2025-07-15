async function getMovies() {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  try {
    const response = await fetch(url);
    const data = await response.json();
    
    const movieList = document.querySelector('#list_movies');
    
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  } catch (error) {
    console.error('Error fetching movie data:', error);
  }
}
getMovies();
