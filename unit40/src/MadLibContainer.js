import React, { useState } from "react";
import MadLibForm from "./MadLibForm";
import MadLib from "./MadLib";
import './Container.css'

const MadLibContainer = () => {
    const [displayLib, setDisplayLib] = useState(false);
    const [madlibValues, setMadlibValues] = useState(null);

    return (
        <div className="Container">
            <h1>Mad Libs!</h1>
            {displayLib ? <MadLib
                madlibValues={madlibValues}
                setMadlibValues={setMadlibValues}
                setDisplayLib={setDisplayLib}/>
                : <MadLibForm
                    setDisplayLib={setDisplayLib}
                    setMadlibValues={setMadlibValues}/>}


        </div>
    );
}

export default MadLibContainer;