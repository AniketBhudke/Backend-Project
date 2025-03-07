const mainDiv = document.getElementById("main");

// Fetch data from the API and display it
async function getData() {
    try {
        const response = await fetch("http://localhost:4000/movies");
        const data = await response.json();
        console.log("Fetched Data:", data);
        displayData(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

getData();

// Input fields
const inputTitle = document.getElementById('title');
const inputDirector = document.getElementById('directorName');

// Create button event
document.getElementById("create").addEventListener('click', addData);{
    addData()
    backapi()

}

function backapi(){
    fetch('http://127.0.0.1:8000/items/', {
        method: 'POST',
        body: JSON.stringify({ name:inputTitle.value, description: inputDirector.value }),
        headers: {
          'Content-Type': 'application/json'
        }
    });
}

// Function to add a new movie
async function addData() {
    try {
        const res = await fetch("http://localhost:4000/movies", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                Name: inputTitle.value,
                Class: inputDirector.value,
            })
        });
        const newMovie = await res.json();
        console.log("Added Movie:", newMovie);

        // Clear input fields after adding a movie
        inputTitle.value = '';
        inputDirector.value = '';

        // Clear existing movies and fetch updated data
        mainDiv.innerHTML = "";
        getData();
    } catch (error) {
        console.error("Error adding movie:", error);
    }
}

// Display movies on the page
function displayData(data) {
    data.forEach((ele) => {
        const movie = document.createElement("div");
        movie.classList.add("movie");

        const movieTitle = document.createElement("h2");
        movieTitle.textContent = ele.title;

        const movieDirector = document.createElement("h3");
        movieDirector.textContent = `Director: ${ele.director}`;

        // Delete button
        const deleteButton = document.createElement('button');
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener('click', () => {
            fetch(`http://localhost:4000/movies/${ele.id}`, {
                method: 'DELETE'
            })
            .then(res => {
                console.log("Deleted Movie:", res);
                mainDiv.innerHTML = "";  // Clear display after delete
                getData();  // Fetch updated data
            });
        });

        // Update button
        const updateButton = document.createElement("button");
        updateButton.textContent = "Update";
        updateButton.addEventListener('click', () => {
            // Populate the form with movie data
            inputTitle.value = ele.title;
            inputDirector.value = ele.director;

            document.getElementById('create').style.display = "none";
            document.getElementById('update').style.display = 'block';

            // Clear previous click event on the update button to avoid multiple listeners
            const updateBtn = document.getElementById('update');
            updateBtn.replaceWith(updateBtn.cloneNode(true));

            document.getElementById('update').addEventListener('click', () => {
                fetch(`http://localhost:4000/movies/${ele.id}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        title: inputTitle.value,
                        director: inputDirector.value,
                    })
                })
                .then(() => {
                    // Clear input fields after update
                    inputTitle.value = '';
                    inputDirector.value = '';

                    // Clear display and fetch updated data
                    mainDiv.innerHTML = "";  
                    getData();

                    // Show create button again and hide the update button
                    document.getElementById('create').style.display = "block";
                    document.getElementById('update').style.display = 'none';
                });
            });
        });
        fetch('http://localhost:4000/items', {
            method: 'POST',
            body: JSON.stringify({ name: 'example', description: 'desc' }),
            headers: {
              'Content-Type': 'application/json'
            }
        });
        
        
        
        // Append all elements to the movie div
        movie.append(movieTitle, movieDirector, deleteButton, updateButton);
        mainDiv.append(movie);
    });
}
