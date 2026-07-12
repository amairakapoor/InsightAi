/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // The Next.js app calls the FastAPI backend via NEXT_PUBLIC_API_URL
  // (set in Vercel project env vars, e.g. https://insightai-api.vercel.app/api)
};

module.exports = nextConfig;
