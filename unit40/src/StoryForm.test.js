import React from "react";
import { render } from "@testing-library/react";
import StoryForm from './StoryForm'
import { useFormik } from "formik";
import validate from "./validate";



it("renders without crashing", function () {
  render(<StoryForm />);
});

it("matches snapshot", function () {
  const { asFragment } = render(<StoryForm />);
  expect(asFragment()).toMatchSnapshot();
});