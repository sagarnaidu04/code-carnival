import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import api from "../api/axios";

function SubmissionHistory() {

    const [history, setHistory] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        document.title = "Submission History | Code Carnival";

        fetchHistory();

    }, []);

    const fetchHistory = async () => {

        try {

            const response = await api.get("/submissions/");

            console.log(response.data);

            if (Array.isArray(response.data)) {
                setHistory(response.data);
            } else if (Array.isArray(response.data.results)) {
                setHistory(response.data.results);
            } else {
                setHistory([]);
            }

        } catch (error) {

            console.log(error);

            toast.error("Failed to load submission history");

        } finally {

            setLoading(false);

        }

    };

    if (loading) {

        return (
            <>
                <Navbar />

                <div className="min-h-screen flex items-center justify-center bg-gray-100">

                    <h1 className="text-3xl font-bold">
                        Loading...
                    </h1>

                </div>
            </>
        );

    }

    if (history.length === 0) {

        return (

            <>
                <Navbar />

                <div className="min-h-screen bg-gray-100 flex items-center justify-center">

                    <div className="bg-white rounded-xl shadow-lg p-10 text-center">

                        <h1 className="text-4xl font-bold">
                            📜 No Submissions Yet
                        </h1>

                        <p className="text-gray-500 mt-4">
                            Solve your first coding problem to see your history here.
                        </p>

                    </div>

                </div>

            </>

        );

    }

    return (

        <>
            <Navbar />

            <div className="bg-gray-100 min-h-screen p-8">

                <div className="max-w-7xl mx-auto">

                    <h1 className="text-4xl font-bold mb-2">

                        📜 Submission History

                    </h1>

                    <p className="text-gray-500 mb-8">

                        View all your previous submissions.

                    </p>

                    <div className="bg-white rounded-xl shadow-lg overflow-hidden">

                        <table className="w-full">

                            <thead className="bg-blue-600 text-white">

                                <tr>

                                    <th className="p-4 text-left">
                                        Problem
                                    </th>

                                    <th className="p-4 text-center">
                                        Language
                                    </th>

                                    <th className="p-4 text-center">
                                        Verdict
                                    </th>

                                    <th className="p-4 text-center">
                                        Runtime
                                    </th>

                                    <th className="p-4 text-center">
                                        Memory
                                    </th>

                                    <th className="p-4 text-center">
                                        Submitted
                                    </th>

                                </tr>

                            </thead>

                            <tbody>

                                {history.map((submission) => (

                                    <tr
                                        key={submission.id}
                                        className="border-b hover:bg-gray-50 transition"
                                    >

                                        <td className="p-4 font-semibold">

                                            {submission.problem_title ||
                                                submission.problem?.title ||
                                                submission.problem}

                                        </td>

                                        <td className="p-4 text-center">

                                            {submission.language}

                                        </td>

                                        <td className="p-4 text-center">

                                            <span
                                                className={
                                                    submission.verdict === "Accepted"
                                                        ? "text-green-600 font-bold"
                                                        : submission.verdict === "Wrong Answer"
                                                        ? "text-red-600 font-bold"
                                                        : "text-yellow-600 font-bold"
                                                }
                                            >

                                                {submission.verdict}

                                            </span>

                                        </td>

                                        <td className="p-4 text-center">

                                            {submission.runtime ?? "-"}

                                        </td>

                                        <td className="p-4 text-center">

                                            {submission.memory ?? "-"}

                                        </td>

                                        <td className="p-4 text-center">

                                            {submission.created_at
                                                ? new Date(
                                                      submission.created_at
                                                  ).toLocaleString()
                                                : "-"}

                                        </td>

                                    </tr>

                                ))}

                            </tbody>

                        </table>

                    </div>

                </div>

            </div>

        </>

    );

}

export default SubmissionHistory;