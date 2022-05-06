import React from "react";
import stories from "./stories";

const StoryForm = ({ formik }) => {

    const storyValues = stories.map((story, idx) => {
        return (<option key={idx} value={`${story.title}`}>{story.title}</option>)
    })

    const labelStyle = {
        display: 'block',
        marginTop: '20px' 
     }

    return (
        <>
            <label style={labelStyle} htmlFor="story">Choose a Story</label>
            <select
                id="story"
                name='story'
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}>
                {storyValues}
            </select>
        </>
    );
}

export default StoryForm;