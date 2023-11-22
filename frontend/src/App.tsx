import React from "react";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Landing from "./pages/Landing";
import Navbar from "./components/Navbar";
import { GoogleOAuthProvider } from "@react-oauth/google";
import Login from "./pages/Login";

function App() {
  return (
    <GoogleOAuthProvider
      clientId={
        "224832934072-igamf2ggcd44jvsv274782h7jqecfjf7.apps.googleusercontent.com"
      }
    >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/jobbing/" element={<Navbar />}>
            <Route index element={<Main />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </GoogleOAuthProvider>
  );
}

export default App;
