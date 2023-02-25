// do a get request to localhost at port 5000

// do repeatedly and time
// do a post request to localhost at port 5000

fetch("http://localhost:5000")
  .then((response) => response.json())
  .then((json) => console.log(json));
