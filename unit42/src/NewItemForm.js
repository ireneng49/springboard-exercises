import React, { useState } from 'react';
import { Form, FormGroup, Label, Input, Button } from 'reactstrap';
import SnackOrBoozeApi from "./Api";

function NewItemForm () {

    const initialState = {
        item: "",
        name: "",
        description: "",
        recipe: "",
        serve: ""
      }
      const [formData, setFormData] = useState(initialState)
      const handleChange = e => {
        const { name, value } = e.target;
        setFormData(data => ({
          ...data,
          [name]: value
        }))
      }
    
      const handleSubmit = (e) => {
        e.preventDefault();
        const { item, name, description, recipe, serve } = formData;

        if (item.toLowerCase() === "snack"){
            console.log(item)
            SnackOrBoozeApi.addSnack({
              "name": name,
              "description": description,
              "recipe": recipe,
              "serve": serve
            })
        }
        if (item.toLowerCase() === "drink"){
            console.log(item)
            SnackOrBoozeApi.addDrink({
              "name": name,
              "description": description,
              "recipe": recipe,
              "serve": serve
            })
        }
        console.log("finished")
        setFormData(initialState)
      }


    return (
        <Form onSubmit={handleSubmit}>
         <FormGroup>
            <Label for="item">Select Drink or item</Label>
            <Input type="text" name="item" id="item" placeholder="Snack or Drink?" value={formData.item} onChange={handleChange}/>

            <Label for="name">Name</Label>
            <Input type="text" name="name" id="name" placeholder="name" value={formData.name} onChange={handleChange}/>

            <Label for="description">Description</Label>
            <Input type="text" name="description" id="description" placeholder="description" value={formData.description} onChange={handleChange}/>

            <Label for="recipe">Recipe</Label>
            <Input type="text" name="recipe" id="recipe" placeholder="recipe" value={formData.recipe} onChange={handleChange}/>

            <Label for="serve">Serve</Label>
            <Input type="text" name="serve" id="serve" placeholder="serve" value={formData.serve} onChange={handleChange}/>

            <Button>Submit</Button>
          </FormGroup>
        </Form>
      );
}

export default NewItemForm;