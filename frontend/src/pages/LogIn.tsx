import { GoogleLogin, useGoogleLogin } from "@react-oauth/google";

import React from "react";
import axios from "axios";

export default function Login() {
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
          {/* <button
            className="border border-black p-2 rounded-lg bg-slate-200 text-black "
            onClick={googleLogin}
          >
            Login with Google
          </button> */}
          <script src="https://accounts.google.com/gsi/client" async></script>
          <div
            id="g_id_onload"
            data-client_id="224832934072-igamf2ggcd44jvsv274782h7jqecfjf7.apps.googleusercontent.com"
            data-login_uri="http://localhost:8000/login"
            data-auto_prompt="false"
            data-auto_select="true"
          ></div>

          <div
            className="g_id_signin"
            data-type="standard"
            data-size="large"
            data-theme="outline"
            data-text="sign_in_with"
            data-shape="rectangular"
            data-logo_alignment="left"
          ></div>
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
