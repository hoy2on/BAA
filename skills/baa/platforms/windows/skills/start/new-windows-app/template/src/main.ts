import { invoke } from "@tauri-apps/api/core";
import "./style.css";

const form = document.querySelector<HTMLFormElement>("#title-form")!;
const input = document.querySelector<HTMLInputElement>("#title")!;
const button = document.querySelector<HTMLButtonElement>("#submit")!;
const result = document.querySelector<HTMLParagraphElement>("#result")!;
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (button.disabled) return;
  button.disabled = true;
  result.textContent = "Checking…";
  try {
    const title = await invoke<string>("validate_title", { title: input.value });
    result.textContent = `Ready: ${title}`;
  } catch (error) {
    result.textContent = typeof error === "string" ? error : "Could not check the title. Try again.";
  } finally {
    button.disabled = false;
  }
});
