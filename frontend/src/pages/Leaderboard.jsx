import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import api from "../api/axios";
import { toast } from "react-toastify";

function Leaderboard() {
    const [leaders, setLeaders] = useState([]);

    useEffect(() => {
        document.title = "Dashboard | Code Carnival";
        fetchLeaderboard();
    }, []);

    const fetchLeaderboard = async () => {
        try {
            const response = await api.get("/accounts/leaderboard/");
            setLeaders(response.data);
        } catch (error) {
            console.log(error);
            toast.error("Failed to load leaderboard");
        }
    };

    const getMedal = (index) => {
        if (index === 0) return "🥇";
        if (index === 1) return "🥈";
        if (index === 2) return "🥉";
        return index + 1;
    };

    return (
        <>
            <Navbar />

            <div className="bg-gray-100 min-h-screen p-8">

                <div className="max-w-6xl mx-auto">

                    <h1 className="text-4xl font-bold mb-2">
                        🏆 Leaderboard
                    </h1>

                    <p className="text-gray-500 mb-8">
                        Top coders ranked by problems solved.
                    </p>

                    <div className="bg-white rounded-xl shadow-lg overflow-hidden">

                        <table className="w-full">

                            <thead className="bg-blue-600 text-white">

                                <tr>

                                    <th className="p-4 text-left">
                                        Rank
                                    </th>

                                    <th className="p-4 text-left">
                                        Username
                                    </th>

                                    <th className="p-4 text-center">
                                        Solved
                                    </th>

                                    <th className="p-4 text-center">
                                        Submissions
                                    </th>

                                    <th className="p-4 text-center">
                                        Accuracy
                                    </th>

                                </tr>

                            </thead>

                            <tbody>

                                {leaders.map((user, index) => (

                                    <tr
                                        key={index}
                                        className="border-b hover:bg-gray-50 transition"
                                    >

                                        <td className="p-4 font-bold text-xl">
                                            {getMedal(index)}
                                        </td>

                                        <td className="p-4 font-semibold">
                                            {user.username}
                                        </td>

                                        <td className="p-4 text-center font-bold text-green-600">
                                            {user.problems_solved}
                                        </td>

                                        <td className="p-4 text-center">
                                            {user.total_submissions}
                                        </td>

                                        <td className="p-4 text-center">

                                            <span
                                                className={
                                                    user.acceptance_rate >= 80
                                                        ? "text-green-600 font-bold"
                                                        : user.acceptance_rate >= 50
                                                        ? "text-yellow-600 font-bold"
                                                        : "text-red-600 font-bold"
                                                }
                                            >
                                                {user.acceptance_rate}%
                                            </span>

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

export default Leaderboard;