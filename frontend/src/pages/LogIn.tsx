import { GoogleLogin, useGoogleLogin } from "@react-oauth/google";
import React from "react";
import { jwtDecode } from "jwt-decode";
import axios from "axios";

export default function Login() {
  const googleLogin = useGoogleLogin({
    flow: "auth-code",
    onSuccess: async (codeResponse) => {
      console.log(codeResponse);
      const tokens = await axios.post("http://localhost:3001/auth/google", {
        code: codeResponse.code,
      });

      console.log(tokens);
    },
    onError: (errorResponse) => console.log(errorResponse),
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
          <h1 className="text-2xl font-bold mb-4">
            We require advanced access
          </h1>
          <button
            className="border border-black p-2 rounded-lg bg-slate-200 text-black "
            onClick={googleLogin}
          >
            Login with Google
          </button>
          {/* <GoogleLogin
            flow="authCode"
            onSuccess={(credentialResponse) => {
              console.log(credentialResponse);
              if (typeof credentialResponse.credential === "string") {
                const decoded = jwtDecode(credentialResponse.credential);
                console.log(decoded);
              }
            }}
            onError={() => {
              console.log("Login Failed");
            }}
          /> */}
        </div>
      </div>
    </div>
  );
}
