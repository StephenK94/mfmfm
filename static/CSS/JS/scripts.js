/*used const to declare unchangable values*/
const jokeContainer = document.getElementById("jokes");
const btn = document.getElementById("btn");
const url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single";

/*Created a function to GET the random jokes from an API and to return it to the jokeContaainer*/
/*Also added a fade to the container for visual effects*/
let getJoke = () => {
    jokeContainer.classList.remove("fade");
    fetch(url)
    .then(data => data.json())
    .then(item =>{
        jokeContainer.textContent = `${item.joke}`;
        jokeContainer.classList.add("fade");
    });
}
/*added a button to fetch random joke from API each time its clciked*/
btn.addEventListener('click', getJoke);
getJoke();
