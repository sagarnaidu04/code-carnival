import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Editor from "@monaco-editor/react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

function ProblemDetail() {

    const { id } = useParams();

    const [problem, setProblem] = useState(null);

    const [language, setLanguage] = useState("Python");

    const [code, setCode] = useState(`def solve():
    pass

if __name__ == "__main__":
    solve()
`);

    const [inputData, setInputData] = useState("");

    const [output, setOutput] = useState("");

    const [loading, setLoading] = useState(false);

    const [submissionResult, setSubmissionResult] = useState(null);

    const templates = {
    Python: `def solve():
    pass

if __name__ == "__main__":
    solve()
`,

    Java: `import java.util.*;

public class Main {

    public static void solve() {

    }

    public static void main(String[] args) {
        solve();
    }
}
`,

    Cpp: `#include <bits/stdc++.h>
using namespace std;

void solve() {

}

int main() {
    solve();
    return 0;
}
`
};


    const changeLanguage = (lang) => {

        if (
            code !== templates[language] &&
            !window.confirm(
                "Changing language will discard your current code. Continue?"
            )
        ) {
            return;
        }

        setLanguage(lang);
        setCode(templates[lang]);
    };

    useEffect(() => {
        document.title = "Dashboard | Code Carnival";
        fetchProblem();
    }, []);

    const fetchProblem = async () => {

        try {

            const response = await api.get(`/problems/${id}/`);

            setProblem(response.data);

        } catch (error) {

            console.log(error);

            toast.error("Failed to load problem");

        }

    };

    const runCode = async () => {

        try {

            setLoading(true);

            setOutput("Running...");

            const response = await api.post("/submissions/run/", {

                code,

                language,

                input_data: inputData,

            });

            setOutput(

                response.data.stdout ||

                response.data.stderr ||

                response.data.compile_output ||

                "No Output"

            );

        } catch (error) {

            console.log(error);

            setOutput(

                JSON.stringify(

                    error.response?.data || error.message,

                    null,

                    2

                )

            );

        } finally {

            setLoading(false);

        }

    };

    const submitCode = async () => {

        try {

            const response = await api.post("/submissions/", {

                problem: Number(id),

                language,

                code,

            });

            setSubmissionResult(response.data);

        } catch (error) {

            console.log(error);

            toast.error(

                JSON.stringify(

                    error.response?.data || error.message

                )

            );

        }

    };

    if (!problem) {

        return (

            <h2 className="text-center p-10 text-2xl">

                <div className="min-h-screen flex items-center justify-center">
                <h1 className="text-3xl font-bold">
                    Loading...
                </h1>
            </div>

            </h2>

        );

    }

    return (

        <>

            <Navbar />

            <div className="bg-gray-100 h-[calc(100vh-72px)] p-4">

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 h-full">

                    {/* LEFT PANEL */}

                    <div className="bg-white rounded-xl shadow-lg p-6 overflow-y-auto h-full">
            <h1 className="text-4xl font-bold">
    {problem.title}
</h1>

<div className="mt-4 mb-6">

    <span
        className={
            problem.difficulty === "Easy"
                ? "bg-green-100 text-green-700 px-4 py-2 rounded-full font-semibold"
                : problem.difficulty === "Medium"
                ? "bg-yellow-100 text-yellow-700 px-4 py-2 rounded-full font-semibold"
                : "bg-red-100 text-red-700 px-4 py-2 rounded-full font-semibold"
        }
    >
        {problem.difficulty}
    </span>

</div>

<hr className="mb-6" />

<h2 className="text-2xl font-bold mb-3">
    Description
</h2>

<p className="whitespace-pre-wrap mb-6">
    {problem.description}
</p>

<h2 className="text-2xl font-bold mb-3">
    Input Format
</h2>

<pre className="bg-gray-100 rounded-lg p-4 whitespace-pre-wrap mb-6">
    {problem.input_format}
</pre>

<h2 className="text-2xl font-bold mb-3">
    Output Format
</h2>

<pre className="bg-gray-100 rounded-lg p-4 whitespace-pre-wrap mb-6">
    {problem.output_format}
</pre>

<h2 className="text-2xl font-bold mb-3">
    Constraints
</h2>

<pre className="bg-gray-100 rounded-lg p-4 whitespace-pre-wrap mb-6">
    {problem.constraints}
</pre>

<h2 className="text-2xl font-bold mb-3">
    Examples
</h2>

<pre className="bg-gray-100 rounded-lg p-4 whitespace-pre-wrap">
    {problem.examples}
</pre>

</div>

{/* RIGHT PANEL */}

<div className="bg-white rounded-xl shadow-lg p-6 flex flex-col h-full">

    <div className="flex justify-between items-center mb-5">

        <h2 className="text-2xl font-bold">
            Code Editor
        </h2>

        <select
            value={language}
            onChange={(e) => changeLanguage(e.target.value)}
            className="border rounded-lg px-4 py-2"
        >
            <option value="Python">Python</option>
            <option value="Java">Java</option>
            <option value="Cpp">C++</option>
        </select>

    </div>

    <Editor
        height="55vh"
        theme="vs-dark"
        language={
            language === "Python"
                ? "python"
                : language === "Java"
                ? "java"
                : "cpp"
        }
        value={code}
        onChange={(value) => setCode(value || "")}
    />

    <h3 className="text-xl font-bold mt-5 mb-3">
        Custom Input
    </h3>

    <textarea
        rows="5"
        value={inputData}
        onChange={(e) => setInputData(e.target.value)}
        placeholder="Enter custom input..."
        className="border rounded-lg p-3 w-full"
    />

    <div className="flex gap-4 mt-5">

        <button
            onClick={runCode}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold transition"
        >
            {loading ? "Running..." : "Run Code"}
        </button>

        <button
            onClick={submitCode}
            className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg font-semibold transition"
        >
            Submit
        </button>

    </div>
    <h3 className="text-xl font-bold mt-6">
    Output
</h3>

<pre
    className="
        bg-gray-900
        text-green-400
        rounded-xl
        p-5
        mt-3
        min-h-[180px]
        overflow-auto
        text-sm
    "
>
    {output}
</pre>

{submissionResult && (

    <div className="mt-6 border rounded-xl p-5 bg-gray-50">

        <h2 className="text-2xl font-bold mb-4">
            Submission Result
        </h2>

        <div className="space-y-3">

            <p>

                <strong>Verdict : </strong>

                <span
                    className={
                        submissionResult.verdict === "Accepted"
                            ? "text-green-600 font-bold"
                            : "text-red-600 font-bold"
                    }
                >
                    {submissionResult.verdict}
                </span>

            </p>

            <p>

                <strong>Runtime :</strong>{" "}

                {submissionResult.runtime} sec

            </p>

            <p>

                <strong>Memory :</strong>{" "}

                {submissionResult.memory} KB

            </p>

        </div>

    </div>

)}

</div>

</div>

</div>

</>

);

}

export default ProblemDetail;