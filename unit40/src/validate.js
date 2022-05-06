const validate = values => {
    const errors = {};

    if (!values.noun) {
        errors.noun = 'Required';
    } else if (values.noun.length > 20) {
        errors.noun = 'Must be 20 characters or less';
    }

    if (!values.noun2) {
        errors.noun2 = 'Required';
    } else if (values.noun2.length > 20) {
        errors.noun2 = 'Must be 20 characters or less';
    }

    if (!values.adjective) {
        errors.adjective = 'Required';
    } else if (values.adjective.length > 20) {
        errors.adjective = 'Must be 20 characters or less';
    }

    if (!values.color) {
        errors.color = 'Required';
    } else if (values.color.length > 20) {
        errors.color = 'Must be 20 characters or less';
    }

    return errors;
};

export default validate;