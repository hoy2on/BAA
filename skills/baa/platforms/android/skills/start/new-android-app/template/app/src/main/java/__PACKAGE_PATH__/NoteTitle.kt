package __APPLICATION_ID__

fun noteTitle(body: String): String = body.lineSequence().first().trim().ifEmpty { "Untitled" }
