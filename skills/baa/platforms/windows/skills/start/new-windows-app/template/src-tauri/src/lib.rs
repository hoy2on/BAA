mod title;

#[tauri::command]
fn validate_title(title: String) -> Result<String, String> {
    title::validate(&title).map(str::to_owned)
}

pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![validate_title])
        .run(tauri::generate_context!())
        .expect("Application runtime failed");
}
