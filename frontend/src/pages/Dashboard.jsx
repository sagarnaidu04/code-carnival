import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/axios";
import Navbar from "../components/Navbar";
import { toast } from "react-toastify";

function Dashboard() {
    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {
        document.title = "Dashboard | Code Carnival";
        fetchDashboard();
    }, []);

    const fetchDashboard = async () => {
        try {
            const response = await api.get("/accounts/dashboard/");
            console.log(response.data);
            setDashboard(response.data);
        } catch (error) {
            console.log(error);
            toast.error("Failed to load dashboard");
        }
    };

    if (!dashboard) {
        return (
            <>
                <Navbar />
                <div className="min-h-screen flex items-center justify-center bg-gray-100">
                    <h1 className="text-3xl font-bold"><div className="min-h-screen flex items-center justify-center">
                    <h1 className="text-3xl font-bold">
                        Loading...
                    </h1>
                </div></h1>
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
                        👋 Welcome Back,
                        <span className="text-blue-600">
                            {" "}{dashboard.username}
                        </span>
                    </h1>

                    <p className="text-gray-500 mb-10">
                        Ready to solve today's coding challenge?
                    </p>

                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                        <div className="bg-white rounded-xl shadow-lg border-t-4 border-green-500 p-6">
                            <h3 className="text-gray-500">
                                📘 Problems Solved
                            </h3>

                            <h1 className="text-5xl font-bold mt-4 text-green-600">
                                {dashboard.accepted}
                            </h1>
                        </div>

                        <div className="bg-white rounded-xl shadow-lg border-t-4 border-blue-500 p-6">
                            <h3 className="text-gray-500">
                                📤 Submissions
                            </h3>

                            <h1 className="text-5xl font-bold mt-4 text-blue-600">
                                {dashboard.total_submissions}
                            </h1>
                        </div>

                        <div className="bg-white rounded-xl shadow-lg border-t-4 border-yellow-500 p-6">
                            <h3 className="text-gray-500">
                                🎯 Accuracy
                            </h3>

                            <h1 className="text-5xl font-bold mt-4 text-yellow-500">
                                {dashboard.acceptance_rate}%
                            </h1>
                        </div>

                        <div className="bg-white rounded-xl shadow-lg border-t-4 border-purple-500 p-6">
                            <h3 className="text-gray-500">
                                🟢 Status
                            </h3>

                            <h1 className="text-3xl font-bold mt-6 text-green-600">
                                Active
                            </h1>
                        </div>

                    </div>

                    <div className="mt-12">

                        <h2 className="text-3xl font-bold mb-6">
                            🚀 Quick Actions
                        </h2>

                        <div className="grid md:grid-cols-3 gap-6">

                            <Link
                                to="/problems"
                                className="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition"
                            >
                                <h2 className="text-2xl font-bold">
                                    💻 Solve Problems
                                </h2>

                                <p className="text-gray-500 mt-3">
                                    Practice coding challenges and improve your skills.
                                </p>
                            </Link>

                            <Link
                                to="/history"
                                className="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition"
                            >
                                <h2 className="text-2xl font-bold">
                                    📜 Submission History
                                </h2>

                                <p className="text-gray-500 mt-3">
                                    Review all your previous submissions.
                                </p>
                            </Link>

                            <Link
                                to="/leaderboard"
                                className="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition"
                            >
                                <h2 className="text-2xl font-bold">
                                    🏆 Leaderboard
                                </h2>

                                <p className="text-gray-500 mt-3">
                                    Check your ranking among all users.
                                </p>
                            </Link>

                        </div>

                    </div>

                    <div className="mt-12 bg-white rounded-xl shadow-lg p-8">

                        <h2 className="text-3xl font-bold mb-6">
                            📊 Statistics
                        </h2>

                        <div className="grid md:grid-cols-3 gap-6">

                            <div className="text-center">
                                <h1 className="text-5xl font-bold text-green-600">
                                    {dashboard.accepted}
                                </h1>

                                <p className="text-gray-500 mt-2">
                                    Accepted
                                </p>
                            </div>

                            <div className="text-center">
                                <h1 className="text-5xl font-bold text-red-600">
                                    {dashboard.wrong_answer}
                                </h1>

                                <p className="text-gray-500 mt-2">
                                    Wrong Answers
                                </p>
                            </div>

                            <div className="text-center">
                                <h1 className="text-5xl font-bold text-orange-500">
                                    {dashboard.runtime_error}
                                </h1>

                                <p className="text-gray-500 mt-2">
                                    Runtime Errors
                                </p>
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </>
    );
}

export default Dashboard;