// This will sanitize text of foreign JavaScript code and SQL commands


function sanitizeData(text) {
    var cleanText = text;
    // General syntax breaker
    cleanText = cleanText.replaceAll(";", "");
    do {
        // Start with removing JavaScript
        cleanText = cleanText.replaceAll("<script>", "");
        cleanText = cleanText.replaceAll("</script>", "");
        // Finish off with SQL commands
        cleanText = cleanText.replaceAll("SELECT", "");
        cleanText = cleanText.replaceAll("select", "");
        cleanText = cleanText.replaceAll("CREATE", "");
        cleanText = cleanText.replaceAll("create", "");
        cleanText = cleanText.replaceAll("UPDATE", "");
        cleanText = cleanText.replaceAll("update", "");
        cleanText = cleanText.replaceAll("DELETE", "");
        cleanText = cleanText.replaceAll("delete", "");
    } while (cleanText.includes("<script>") && cleanText.includes("</script>") &&
    	cleanText.toLowerCase().includes("select") && cleanText.toLowerCase().includes("create") &&
    	cleanText.toLowerCase().includes("update") && cleanText.toLowerCase().includes("delete"));
    alert(cleanText); // For testing purposes
    return cleanText;
}
