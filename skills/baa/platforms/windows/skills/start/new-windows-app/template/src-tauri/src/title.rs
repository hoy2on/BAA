pub fn validate(value: &str) -> Result<&str, String> {
    let title = value.trim();
    if title.is_empty() {
        return Err("Enter a title.".into());
    }
    if title.chars().count() > 120 {
        return Err("Use at most 120 characters.".into());
    }
    Ok(title)
}

#[cfg(test)]
mod tests {
    use super::validate;
    #[test]
    fn trims_and_preserves_unicode() {
        assert_eq!(validate("  Hello 🌍  ").unwrap(), "Hello 🌍");
    }
    #[test]
    fn rejects_empty_and_overlong_input() {
        assert!(validate(" ").is_err());
        assert!(validate(&"a".repeat(121)).is_err());
        assert!(validate(&"🌍".repeat(120)).is_ok());
    }
}
