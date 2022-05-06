import React from "react";
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Home from '../Home';

it("matches the snapshot", function() {
    const {asFragment} = render(<Home />)
    expect(asFragment()).toMatchSnapshot();
})

it("should render", function(){
    render(<Home />);
})

it("should contain some HTML elements", function() {
    const {queryByText} = render(<Home />)
    expect(queryByText("Welcome to Silicon Valley's premier dive cafe!")).toBeInTheDocument()
})