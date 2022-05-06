import React from "react";
import { useFormik } from "formik";
import validate from "./validate";
import StoryForm from "./StoryForm";

const MadLibForm = ({ setDisplayLib, setMadlibValues }) => {
    const formik = useFormik({
        initialValues: {
            noun: '',
            noun2: '',
            adjective: '',
            color: '',
            story: ''
        },
        validate,
        onSubmit: values => passValuesToMadLib(values),
    });

    // uses values from forms to create MadLibs and changes state to display them
    const passValuesToMadLib = (values) => {
        setMadlibValues(values);
        setDisplayLib(true);
    }

    const labelStyle = {
       display: 'block',
       marginTop: '5px' 
    }

    const buttonStyle = {
        backgroundColor: 'lightgreen',
        borderRadius: '5px',
        padding: '5px 10px',
        fontWeight: '700',
        border: '2px solid black',
        display: 'block',
        marginTop: '10px',
        marginLeft: '40px'
    }

    const formStyle = {
        textAlign: 'center'
    }

    return (
        <form style={formStyle} onSubmit={formik.handleSubmit}>
            <label style={labelStyle} htmlFor="noun">Noun</label>
            <input
                id="noun"
                name="noun"
                type="text"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.noun}
                placeholder="noun"
            />
            {formik.touched.noun && formik.errors.noun && (
                <div>{formik.errors.noun}</div>
            )}

            <label style={labelStyle} htmlFor="noun2">Noun 2</label>
            <input
                id="noun2"
                name="noun2"
                type="text"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.noun2}
                placeholder="noun 2"
            />
            {formik.touched.noun2 && formik.errors.noun2 ? (
                <div>{formik.errors.noun2}</div>
            ) : null}

            <label style={labelStyle} htmlFor="adjective">Adjective</label>
            <input
                id="adjective"
                name="adjective"
                type="text"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.adjective}
                placeholder="adjective"
            />
            {formik.touched.adjective && formik.errors.adjective ? (
                <div>{formik.errors.adjective}</div>
            ) : null}

            <label style={labelStyle} htmlFor="color">Color</label>
            <input
                id="color"
                name="color"
                type="text"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.color}
                placeholder="color"
            />
            {formik.touched.color && formik.errors.color ? (
                <div>{formik.errors.color}</div>
            ) : null}

            <StoryForm formik={formik} />

            <button style={buttonStyle} type="submit">Create Story</button>


        </form>

    );
}

export default MadLibForm;