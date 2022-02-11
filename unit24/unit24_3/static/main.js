const BASE_URL = 'http://localhost:5000/api/cupcakes';

async function get_cupcakes(){
    const resp = await axios.get(BASE_URL);
    return resp.data.cupcakes;
}

async function display_cupcakes(){
    const cupcakes = await get_cupcakes();

    for (cupcake of cupcakes){
        addCupcakeToList(cupcake);
    }
}

function addCupcakeToList(cupcake){
    const $list = $('#cupcake-list');
    const newLi = $('<li>').text(cupcake.flavor);
    $list.append(newLi);
}

async function createCupcake(){
    const json = {
        'flavor': $('#flavor').val(),
        'size': $('#size').val(),
        'rating': $('#rating').val(),
        'image': $('#image').val(),
    };

    const resp = await axios.post(BASE_URL, json);
    return resp;
}

async function handleAddCupcakeClick(evt){
    evt.preventDefault();
    resp = await createCupcake();
    if(resp.status === 201){
        addCupcakeToList(resp.data.cupcake);
        $('#flavor').val('');
        $('#size').val('');
        $('#rating').val('');
        $('#image').val('');
    }
}

$('#add-cupcake-btn').on('click', handleAddCupcakeClick);

display_cupcakes();