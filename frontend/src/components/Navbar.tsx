import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { BasicUserInfo } from "./types";

export default function Navbar() {
  const [basicUserInfo, setBasicUserInfo] = useState<BasicUserInfo | null>(
    null
  );

  useEffect(() => {
    async function fetchUserInfo() {
      try {
        const response = await fetch("http://localhost:8000/me", {
          credentials: "include",
        });
        const data = await response.json();
        setBasicUserInfo({ picture: data.picture, firstName: data.given_name });
      } catch (err) {
        console.log(err);
      }
    }
    fetchUserInfo();
  }, []);

  return (
    <div className="grid grid-cols-[1fr] grid-rows-[auto_1fr] min-h-screen bg-gradient-to-b from-indigo-100 from-5% via-indigo-200 via-25% to-indigo-400 to-90%">
      <div className="navber">
        <a href="/" className="text-4xl font-[Kanit]">
          Jobbing
        </a>
        {basicUserInfo && (
          <div className="flex justify-center items-center gap-5">
            <p>{basicUserInfo.firstName}</p>
            <img
              src={basicUserInfo.picture}
              alt="profile"
              className="h-16 w-16 rounded-full border-2 border-gray-400"
            />
          </div>
        )}
      </div>
      <Outlet />
    </div>
  );
}
