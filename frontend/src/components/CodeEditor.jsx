import Editor from "@monaco-editor/react";
import { useState } from "react";
import api from "../api/axios";

function CodeEditor() {

    const [code, setCode] = useState(
`def solve():
    pass`
    );

    const [output, setOutput] = useState("");

    const runCode = async () => {

        try {

            const response = await api.post("/submissions/run/", {
                source_code: code,
                language: "python"
            });

            setOutput(response.data.output);

        } catch(error) {

            console.log(error);

            if(error.response){
                setOutput(JSON.stringify(error.response.data));
            }
            else{
                setOutput("Server error");
            }

        }
    };


    return (
        <div>

            <h2>Code Editor</h2>

            <Editor
                height="400px"
                language="python"
                theme="vs-dark"
                value={code}
                onChange={(value)=>setCode(value)}
            />


            <button onClick={runCode}>
                Run
            </button>


            <h3>Output</h3>

            <pre>
                {output}
            </pre>


        </div>
    );
}

export default CodeEditor;