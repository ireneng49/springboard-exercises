import React, { useState } from "react";
import stories from "./stories";


const MadLib = ({ madlibValues, setDisplayLib }) => {

    const handleReset = () => {
        setDisplayLib(false);
    }

    const { noun, noun2, color, adjective } = madlibValues
    let { story } = madlibValues
    if (story === '') story = 'Once Upon a Time'

    const selectStory = () => {
        for (let i = 0; i < stories.length; i++) {
            if (stories[i].title === story) {
                return createStory(stories[i].text)
            }
        }
    }

    const createStory = (foundStory) => {
        let modifiedStory;
        modifiedStory = foundStory.replace('noun1', noun)
        modifiedStory = modifiedStory.replace('noun2', noun2)
        modifiedStory = modifiedStory.replace('color', color)
        modifiedStory = modifiedStory.replace('adj', adjective)
        return modifiedStory
    }

    const buttonStyle = {
        backgroundColor: 'lightgreen',
        borderRadius: '5px',
        padding: '5px 10px',
        fontWeight: '700',
        border: '2px solid black'
    }

    return (
        <div className="MadLib">
            <h3>{`Story: ${story}`}</h3>
            <h3>{selectStory()}</h3>
            <button style={buttonStyle} onClick={handleReset}>Make Another Story</button>
        </div>
    );
}

export default MadLib;