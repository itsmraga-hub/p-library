const greet = () => {
  eel.greet_from_python()(
    function(greeting) {
      document.getElementById("greeting").innerText = greeting;
    }
  );
}


document.getElementById('get_books').onclick = () => {
  eel.get_books()(function(books) {
    const ul = document.querySelector('.books')
    for (let i = 0; i < books.length; i++) {
      console.log(books[0]);
      const li = document.createElement('li');
      li.innerText = books[0]['name'];
      ul.appendChild(li);
    }
  })
}


document.getElementById("random_number").onclick = function () {
  // Call python's random_python function
  eel.random_python()(function(number) {
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerHTML = number;
  });
  greet();
}


document.getElementById("login").onclick = function () {
  // Call python's random_python function
  window.location.href = 'login.html'
}


