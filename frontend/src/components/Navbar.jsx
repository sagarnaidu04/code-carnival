import { Link, useLocation, useNavigate } from "react-router-dom";

function Navbar() {

    const navigate = useNavigate();
    const location = useLocation();

    const logout = () => {

        localStorage.removeItem("access");
        localStorage.removeItem("refresh");

        navigate("/login", { replace: true });

    };

    const active = (path) =>
        location.pathname === path
            ? "text-blue-400 font-bold"
            : "text-white hover:text-blue-300";

    return (

        <nav className="bg-gray-900 shadow-lg sticky top-0 z-50">

            <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">

                <Link
                    to="/dashboard"
                    className="text-3xl font-bold text-white"
                >
                    🎯 Code Carnival
                </Link>

                <div className="flex items-center gap-8">

                    <Link
                        to="/dashboard"
                        className={active("/dashboard")}
                    >
                        Dashboard
                    </Link>

                    <Link
                        to="/problems"
                        className={active("/problems")}
                    >
                        Problems
                    </Link>

                    <Link
                        to="/history"
                        className={active("/history")}
                    >
                        History
                    </Link>

                    <Link
                        to="/leaderboard"
                        className={active("/leaderboard")}
                    >
                        Leaderboard
                    </Link>

                    <button
                        onClick={logout}
                        className="bg-red-600 hover:bg-red-700 text-white px-5 py-2 rounded-lg transition"
                    >
                        Logout
                    </button>

                </div>

            </div>

        </nav>

    );

}

export default Navbar;