import React from "react";
import { render } from "@testing-library/react";
import MadLibContainer from './MadLibContainer'

it("renders without crashing", function () {
  render(<MadLibContainer />);
});

it("matches snapshot", function () {
  const { asFragment } = render(<MadLibContainer />);
  expect(asFragment()).toMatchSnapshot();
});

// it("Should return to creation form upon clicking reset button", function () {
//     const madlib = render(<MadLib madlibValues={madlibValues}
//         setMadlibValues={setMadlibValues}
//         setDisplayLib={setDisplayLib} />);

//     expect(madlib.getByText('There was a pink fish who loved a scaly dog.')).toBeInTheDocument();

//     const resetButton = madlib.getByText('Make Another Story')
//     expect(resetButton).toBeInTheDocument()
//     fireEvent.click(resetButton)
//     // expect(madlib.queryByText('There was a pink fish who loved a scaly dog.')).not.toBeVisible();
// })