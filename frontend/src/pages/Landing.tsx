import React from "react";

export default function Landing() {
  return (
    <div className="grid grid-cols-[1fr] grid-rows-[auto_1fr_auto] min-h-screen bg-gradient-to-b from-indigo-100 from-5% via-indigo-200 via-25% to-indigo-400 to-90%">
      <div className="navber">
        <h1 className="text-4xl">Jobbing</h1>
        <ul>
          <li>Log In</li>
        </ul>
      </div>
      <div className="w-full text-center text-2xl text-gray-700 flex flex-col justify-center items-center">
        <h1 className="text-6xl font-bold mb-4 t">
          Jobbing made <u>easier</u>.
        </h1>
        <h2 className="text--6xl">
          Instant job application updates with Gmail integration
        </h2>
        <button
          type="button"
          className="bg-indigo-600 text-3xl border-indigo-500 border-1 rounded-xl font-bold text-gray-200 px-8 py-4 mt-12 hover:bg-indigo-500 active:bg-indigo-700 transition-colors"
        >
          Get Started
        </button>
      </div>
      <div className="h-28"></div>
    </div>
  );
}
