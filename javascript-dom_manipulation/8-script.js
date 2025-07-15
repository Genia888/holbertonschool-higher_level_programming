async function getHello() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  try {
    const response = await fetch(url);
    const data = await response.json();
    document.querySelector('#hello').textContent = data.hello;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
getHello();
