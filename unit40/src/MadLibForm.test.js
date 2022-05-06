import React from "react";
import { render } from "@testing-library/react";
import MadLibForm from './MadLibForm'

it("renders without crashing", function () {
  render(<MadLibForm />);
});

it("matches snapshot", function () {
  const { asFragment } = render(<MadLibForm />);
  expect(asFragment()).toMatchSnapshot();
});