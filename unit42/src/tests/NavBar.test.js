import React from "react";
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';
import NavBar from "../NavBar";

it("matches the snapshot", function() {
    const {asFragment} = render(
    <MemoryRouter initialEntries={["/"]}>   
        <NavBar />
    </MemoryRouter>
    
    )
    expect(asFragment()).toMatchSnapshot();
})

it("should render", function(){
    render(
    <MemoryRouter initialEntries={["/"]}>   
        <NavBar />
    </MemoryRouter>    
    );
})

it("should contain some link elements", function() {
    const {getByText} = render(
    <MemoryRouter initialEntries={["/"]}>   
        <NavBar />
    </MemoryRouter>
    )
    let snacksLink = getByText('Snacks');
    expect(snacksLink).toBeInTheDocument()
    let title = getByText('Snack or Booze')
    expect(title).toBeInTheDocument()
})