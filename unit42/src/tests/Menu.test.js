import React from "react";
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';
import Menu from "../Menu";

let snacks = [
    {
      "id": "nachos",
      "name": "Nachos",
      "description": "An American classic!",
      "recipe": "Cover expensive, organic tortilla chips with Cheez Whiz.",
      "serve": "Serve in a hand-thrown ceramic bowl, garnished with canned black olives"
    },
    {
      "id": "hummus",
      "name": "Hummus",
      "description": "Sure to impress your vegan friends!",
      "recipe": "Purchase one container of hummus.",
      "serve": "Place unceremoniously on the table, along with pita bread."
    },
    {
      "id": "arugula-and-walnut-salad",
      "name": "Arugula and Walnut Salad",
      "description": "Tart and delicious.",
      "recipe": "Mix arugula, toasted walnuts, and thinly-sliced Parmesan cheese. Dress with lemon and olive oil.",
      "serve": "Place on tiny, precious little plates."
    }
  ];

it("matches the snapshot", function() {
    const {asFragment} = render(
    <MemoryRouter initialEntries={["/snacks"]}>   
        <Menu items={snacks} title="Snacks"/>
    </MemoryRouter>
    
    )
    expect(asFragment()).toMatchSnapshot();
})

it("should render", function(){
    render(
    <MemoryRouter initialEntries={["/snacks"]}>   
        <Menu items={snacks} title="Snacks"/>
    </MemoryRouter>    
    );
})

it("should contain some link elements", function() {
    const {getByText} = render(
    <MemoryRouter initialEntries={["/snacks"]}>   
        <Menu items={snacks} title="Snacks"/>
    </MemoryRouter>
    )
    let snacksLink = getByText('Snacks Menu');
    expect(snacksLink).toBeInTheDocument()
    let nachos = getByText('Nachos')
    expect(nachos).toBeInTheDocument()

    let hummus = getByText('Hummus')
    expect(hummus).toBeInTheDocument()

    let salad = getByText('Arugula and Walnut Salad')
    expect(salad).toBeInTheDocument()
})