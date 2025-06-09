"use client";
import React, { useState } from "react";
import { cloneWebsite } from "../lib/api";
import { SparklesIcon } from "@heroicons/react/24/solid"; // Tailwind HeroIcons

interface CloneFormProps {
  onResult: (html: string) => void;
}

const CloneForm: React.FC<CloneFormProps> = ({ onResult }) => {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  setLoading(true);
  setError("");
  try {
    const cleanedUrl = url.trim().replace(/\\+$/, "");
    if (!cleanedUrl) {
      setError("Please enter a valid URL.");
      setLoading(false);
      return;
    }
    const result = await cloneWebsite(cleanedUrl);
    onResult(result.html);
  } catch (err) {
    setError("Failed to clone website. Please try again.");
  } finally {
    setLoading(false);
  }
};


  return (
    <div className="bg-white/70 backdrop-blur-lg rounded-xl shadow-xl p-8 w-full max-w-2xl border border-gray-200">
      <form onSubmit={handleSubmit} className="flex flex-col gap-6">
        <div className="flex items-center gap-3">
          <SparklesIcon className="h-8 w-8 text-blue-600 animate-pulse" />
          <h2 className="text-2xl font-extrabold text-gray-800">Clone a Website</h2>
        </div>
        <input
          id="url"
          type="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
          className="border-2 border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
          placeholder="Enter a website URL (e.g., https://example.com)"
        />
        <button
          type="submit"
          className={`bg-gradient-to-r from-blue-500 to-indigo-600 text-white py-3 rounded-lg font-semibold shadow-md hover:shadow-lg transition-all duration-300 ${
            loading ? "opacity-60 cursor-not-allowed" : ""
          }`}
          disabled={loading}
        >
          {loading ? "Cloning..." : "Clone Website"}
        </button>
        {error && <p className="text-red-600 font-medium">{error}</p>}
      </form>
    </div>
  );
};

export default CloneForm;
