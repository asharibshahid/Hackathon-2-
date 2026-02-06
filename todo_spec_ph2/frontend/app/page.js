"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

import { getToken } from "../lib/auth";

export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    const token = getToken();
    router.replace(token ? "/dashboard" : "/login");
  }, [router]);

  return (
    <div className="container">
      <div className="card auth-card">
        <h1>Loading...</h1>
        <p className="muted">Redirecting to your workspace.</p>
      </div>
    </div>
  );
}
