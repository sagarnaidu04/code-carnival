import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/axios";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await api.post("/accounts/login/", {
                username,
                password,
            });

            localStorage.setItem("access", response.data.access);
            localStorage.setItem("refresh", response.data.refresh);

            navigate("/dashboard", {
                replace: true,
            });

        } catch (error) {

            if (error.response) {
                toast.error(JSON.stringify(error.response.data));
            } else {
                toast.error(error.message);
            }

        }

    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-gray-100">

            <div className="bg-white shadow-xl rounded-xl p-8 w-[400px]">

                <h1 className="text-4xl font-bold text-center mb-8">
                    Code Carnival
                </h1>

                <form
                    onSubmit={handleLogin}
                    className="space-y-5"
                >

                    <input
                        type="text"
                        placeholder="Username"
                        className="w-full border rounded-lg p-3"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        className="w-full border rounded-lg p-3"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />

                    <button
                        type="submit"
                        className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg p-3"
                    >
                        Login
                    </button>

                </form>

                <p className="mt-6 text-center">

                    Don't have an account?

                    <Link
                        to="/register"
                        className="text-blue-600 ml-2 font-semibold"
                    >
                        Register
                    </Link>

                </p>

            </div>

        </div>

    );

}

export default Login;