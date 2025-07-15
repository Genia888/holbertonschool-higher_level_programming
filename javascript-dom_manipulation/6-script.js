async function getData() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    document.querySelector('#character').textContent = data.name;
  } catch (error) {
    console.error(error.message);
  }
}
getData();
