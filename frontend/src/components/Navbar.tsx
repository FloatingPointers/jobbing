import React from "react";
import { Outlet } from "react-router-dom";

export default function Navbar() {
  return (
    <div className="grid grid-cols-[1fr] grid-rows-[auto_1fr]">
      <div>Nabbar</div>
      <Outlet />
    </div>
  );
}
