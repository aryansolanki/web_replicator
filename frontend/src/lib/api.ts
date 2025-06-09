const BACKEND_URL = "http://localhost:8000/api/clone";

export async function cloneWebsite(url: string): Promise<{ html: string }> {
  const response = await fetch(BACKEND_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url }),
  });

  if (!response.ok) {
    throw new Error("Failed to fetch cloned website.");
  }

  return response.json();
}
