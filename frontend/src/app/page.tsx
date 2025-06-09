"use client";
import React, { useState } from "react";
import CloneForm from "../components/CloneForm";
import ClonePreview from "../components/ClonePreview";
import { SparklesIcon } from "@heroicons/react/24/solid";

const HomePage: React.FC = () => {
  const [clonedHtml, setClonedHtml] = useState("");

  return (
    <main className="flex flex-col items-center min-h-screen p-8 bg-gradient-to-b from-blue-100 via-white to-blue-50">
      <div className="text-center">
        <div className="flex items-center justify-center gap-2 mb-4">
          <SparklesIcon className="h-10 w-10 text-blue-600 animate-bounce" />
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">
            Website Cloner
          </h1>
        </div>
        <p className="text-gray-600 max-w-lg mx-auto">
          Enter a public website URL and let our AI clone its design for you!
        </p>
      </div>
      <div className="mt-8 w-full flex flex-col items-center">
        <CloneForm onResult={setClonedHtml} />
        <ClonePreview html={clonedHtml} />
      </div>
    </main>
  );
};

export default HomePage;
