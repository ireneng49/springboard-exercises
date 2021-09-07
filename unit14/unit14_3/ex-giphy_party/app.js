const form = document.getElementById("giphypartyform");
const searchInput = document.getElementById("searchinput");
const searchBtn = document.getElementById("searchbtn");
const removeBtn = document.getElementById("removebtn");
const imgContainer = document.getElementById("images");

searchBtn.addEventListener("click", function (evt) {
    evt.preventDefault();
    if (searchInput.value) {
      getImg(searchInput.value);
    }
    searchInput.value = "";
  });


async function getImg(input) {
    const response = await axios.get('https://api.giphy.com/v1/gifs/search', {
        params: {
            api_key: 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym', 
            q: input
        }
    });
    getImg(response.data.data);

    const num = Math.floor(Math.random() * response.data.data.length);
    const imgURL = response.data.data[num].images.original.url;
    const newImg = document.createElement("img");
    const newImgContainer = document.createElement("div");
    newImgContainer.classList.add("giphy");
    newImgContainer.append(newImg);
    newImg.src = imgURL;
    imgContainer.append(newImgContainer);
};
  
  
  removeBtn.addEventListener("click", function () {
    imgDiv.innerHTML = "";
  });

