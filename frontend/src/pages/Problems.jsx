import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/axios";
import Navbar from "../components/Navbar";

function Problems() {

    const [problems, setProblems] = useState([]);

    const [search, setSearch] = useState("");

    const [difficulty, setDifficulty] = useState("");

    useEffect(() => {

        document.title = "Problems | Code Carnival";

        fetchProblems();

    }, [search, difficulty]);

    const fetchProblems = async () => {

        try {

            let url = "/problems/?";

            if (search)
                url += `search=${search}&`;

            if (difficulty)
                url += `difficulty=${difficulty}`;

            const response = await api.get(url);

            setProblems(response.data);

        } catch (error) {

            console.log(error);

        }

    };

    const badgeColor = (difficulty) => {

        if (difficulty === "Easy")
            return "bg-green-100 text-green-700";

        if (difficulty === "Medium")
            return "bg-yellow-100 text-yellow-700";

        return "bg-red-100 text-red-700";

    };

    return (

        <>
            <Navbar />

            <div className="bg-gray-100 min-h-screen p-8">

                <div className="max-w-7xl mx-auto">

                    <div className="flex justify-between items-center mb-8">

                        <div>

                            <h1 className="text-4xl font-bold">
                                💻 Problems
                            </h1>

                            <p className="text-gray-500 mt-2">
                                Practice coding problems.
                            </p>

                        </div>

                        <div className="bg-white rounded-xl shadow px-6 py-4">

                            <h3 className="text-gray-500">
                                Total Problems
                            </h3>

                            <h1 className="text-3xl font-bold text-blue-600">
                                {problems.length}
                            </h1>

                        </div>

                    </div>

                    {/* Search + Filter */}

                    <div className="flex gap-4 mb-8">

                        <input
                            type="text"
                            placeholder="Search problems..."
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            className="flex-1 border rounded-lg px-4 py-3"
                        />

                        <select
                            value={difficulty}
                            onChange={(e) => setDifficulty(e.target.value)}
                            className="border rounded-lg px-4 py-3"
                        >

                            <option value="">
                                All
                            </option>

                            <option value="Easy">
                                Easy
                            </option>

                            <option value="Medium">
                                Medium
                            </option>

                            <option value="Hard">
                                Hard
                            </option>

                        </select>

                    </div>

                    <div className="space-y-5">

                        {problems.map((problem) => (

                            <Link
                                key={problem.id}
                                to={`/problems/${problem.id}`}
                            >

                                <div className="bg-white rounded-xl shadow-lg hover:shadow-2xl transition p-6">

                                    <div className="flex justify-between items-center">

                                        <div>

                                            <h2 className="text-2xl font-bold">
                                                {problem.title}
                                            </h2>

                                            <p className="text-gray-500 mt-2">
                                                Click to solve this problem
                                            </p>

                                        </div>

                                        <span
                                            className={`px-4 py-2 rounded-full font-semibold ${badgeColor(problem.difficulty)}`}
                                        >
                                            {problem.difficulty}
                                        </span>

                                    </div>

                                </div>

                            </Link>

                        ))}

                    </div>

                </div>

            </div>

        </>

    );

}

export default Problems;