import React from "react";
import { Outlet } from "react-router-dom";

export default function Navbar() {
  return (
    <div className="grid grid-cols-[1fr] grid-rows-[auto_1fr] min-h-screen bg-gradient-to-b from-indigo-100 from-5% via-indigo-200 via-25% to-indigo-400 to-90%">
      <div className="navber">
        <a href="/" className="text-4xl font-[Kanit]">
          Jobbing
        </a>
      </div>
      <Outlet />
    </div>
  );
}
