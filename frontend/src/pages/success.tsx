import React, { useEffect } from "react";

export default function Success() {
  useEffect(() => {
    fetch("http://localhost:8000/session")
      .then((res) => res.json())
      .then((data) => console.log(data));
  }, []);
  return (
    <div>
      <h1>Success</h1>
    </div>
  );
}
