"use client";

import { useEffect, useState } from "react";

const KEY = "insightai_active_table";

export function useActiveTable(): [string, (t: string) => void] {
  const [table, setTable] = useState("sales");

  useEffect(() => {
    const stored = window.localStorage.getItem(KEY);
    if (stored) setTable(stored);
  }, []);

  function update(t: string) {
    setTable(t);
    window.localStorage.setItem(KEY, t);
  }

  return [table, update];
}
