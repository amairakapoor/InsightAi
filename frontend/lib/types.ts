export interface AskResponse {
  question: string;
  sql: string;
  sql_engine: "gemini" | "rule_based";
  columns: string[];
  rows: Record<string, any>[];
  row_count: number;
  chart_type: string;
  chart_json: string | null;
  insight_text: string;
  insight_engine: "gemini" | "rule_based";
}

export interface HistoryItem {
  id: number;
  question: string;
  sql: string;
  row_count: number;
  created_at: string;
}

export interface DatasetInfo {
  table_name: string;
  filename: string;
  rows: number | null;
  columns: number | null;
}

export interface Kpis {
  total_revenue: number;
  total_profit: number;
  total_orders: number;
  total_customers: number;
}
