import type { AskResponse, HistoryItem, DatasetInfo, Kpis } from "./types";

// Set NEXT_PUBLIC_API_URL in Vercel project settings to your deployed
// FastAPI function, e.g. https://insightai-api.vercel.app/api
// Falls back to localhost for local `npm run dev` against a local backend.
const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000/api";

async function handle<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `Request failed (${res.status})`);
  }
  return res.json();
}

export async function askQuestion(question: string, tableName = "sales"): Promise<AskResponse> {
  const res = await fetch(`${API_URL}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, table_name: tableName }),
  });
  return handle<AskResponse>(res);
}

export async function getHistory(limit = 20): Promise<HistoryItem[]> {
  const res = await fetch(`${API_URL}/history?limit=${limit}`, { cache: "no-store" });
  return handle<HistoryItem[]>(res);
}

export async function getDatasets(): Promise<DatasetInfo[]> {
  const res = await fetch(`${API_URL}/datasets`, { cache: "no-store" });
  return handle<DatasetInfo[]>(res);
}

export async function getKpis(tableName = "sales"): Promise<Kpis> {
  const res = await fetch(`${API_URL}/kpis?table_name=${tableName}`, { cache: "no-store" });
  return handle<Kpis>(res);
}

export async function uploadDataset(file: File): Promise<{ table_name: string; n_rows: number; n_columns: number; columns: string[]; preview: Record<string, any>[] }> {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${API_URL}/upload`, { method: "POST", body: formData });
  return handle(res);
}

export async function checkHealth(): Promise<boolean> {
  try {
    const res = await fetch(`${API_URL}/health`, { cache: "no-store" });
    return res.ok;
  } catch {
    return false;
  }
}

export async function downloadReport(
  question: string,
  sql: string,
  rows: Record<string, any>[],
  insightText: string,
  format: "pdf" | "csv"
): Promise<Blob> {
  const res = await fetch(`${API_URL}/report`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, sql, rows, insight_text: insightText, format }),
  });
  if (!res.ok) throw new Error("Report export failed");
  return res.blob();
}

export { API_URL };
