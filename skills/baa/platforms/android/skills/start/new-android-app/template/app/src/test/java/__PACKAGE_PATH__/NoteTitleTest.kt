package __APPLICATION_ID__

import org.junit.Assert.assertEquals
import org.junit.Test

class NoteTitleTest {
    @Test fun usesTrimmedFirstLine() {
        assertEquals("Meeting", noteTitle("  Meeting  \nDetails"))
        assertEquals("Untitled", noteTitle("\nDetails"))
        assertEquals("Untitled", noteTitle(""))
    }
}
