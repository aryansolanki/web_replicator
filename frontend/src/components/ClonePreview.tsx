import React from "react";

interface ClonePreviewProps {
  html: string;
}

const ClonePreview: React.FC<ClonePreviewProps> = ({ html }) => {
  if (!html) {
    return (
      <div className="text-gray-500 italic mt-8">
        The cloned website preview will appear here.
      </div>
    );
  }

  return (
    <div className="mt-10 w-full max-w-5xl border-4 border-dashed border-blue-300 rounded-xl overflow-hidden shadow-lg">
      <iframe
        srcDoc={html}
        title="Cloned Website Preview"
        className="w-full h-[700px] bg-white"
        sandbox=""
      />
    </div>
  );
};

export default ClonePreview;
