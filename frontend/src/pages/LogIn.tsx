import { GoogleLogin, useGoogleLogin } from "@react-oauth/google";

import React from "react";

export default function Login() {
  const login = useGoogleLogin({
    onError: (error) => console.log("Google Error:", error),
    scope:
      "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/gmail.readonly openid",
    flow: "auth-code",
    ux_mode: "redirect",
    redirect_uri: "http://localhost:8000/login",
    state:
      Math.random().toString(36).substring(2, 15) +
      Math.random().toString(36).substring(2, 15),
  });
  return (
    <div className="grid grid-cols-[1fr] grid-rows-[auto_1fr_auto] min-h-screen bg-gradient-to-b from-indigo-100 from-5% via-indigo-200 via-25% to-indigo-400 to-90%">
      <div className="navber">
        <a href="/" className="text-4xl font-[Kanit]">
          Jobbing
        </a>
      </div>
      <div className="w-full text-center text-gray-700 flex flex-col justify-center items-center ">
        <div className="border border-white  rounded-lg p-8 bg-white">
          <h1 className="text-2xl font-bold mb-4">Give us all your money</h1>
          <button onClick={login}>Sign in with Google 🚀</button>
        </div>
      </div>
    </div>
  );
}
