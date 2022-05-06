import React, { useState } from "react";
import { fireEvent, render } from "@testing-library/react";
import MadLib from "./MadLib";
// importing parent comp doesn't seem to help with func defs
import MadLibContainer from "./MadLibContainer";

const madlibValues = {
    adjective: 'scaly',
    color: 'pink',
    noun: 'fish',
    noun2: 'dog',
    story: 'True Love'
}

// const [displayLib, setDisplayLib] = useState(false);
// const [madlibValues, setMadlibValues] = useState(null);

it("renders without crashing", function () {
    render(<MadLib madlibValues={madlibValues} />);
});

it("matches snapshot", function () {
    const { asFragment } = render(<MadLib madlibValues={madlibValues} />);
    expect(asFragment()).toMatchSnapshot();
});

it("Should create correct MadLib", function () {
    const madlib = render(<MadLib madlibValues={madlibValues} />);

    expect(madlib.getByText('There was a pink fish who loved a scaly dog.')).toBeInTheDocument();
    expect(madlib.getByText('Story: True Love')).toBeInTheDocument();
    expect(madlib.getByText('Make Another Story')).toBeInTheDocument();
})

// should I be doing this testing from inside MadlibContainer?
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