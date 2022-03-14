// This will sanitize text of foreign JavaScript code and SQL commands


function sanitizeData(text) {
    var cleanText = text;
    // General syntax breaker
    cleanText = cleanText.replaceAll(";", "");
    // Replace HTML characters
    cleanText = cleanText.replaceAll("&", "&amp");
    cleanText = cleanText.replaceAll("<", "&lt");
    cleanText = cleanText.replaceAll(">", "&gt");
    do {
        // Finish off with SQL commands
        cleanText = cleanText.replaceAll("SELECT", "");
        cleanText = cleanText.replaceAll("select", "");
        cleanText = cleanText.replaceAll("CREATE", "");
        cleanText = cleanText.replaceAll("create", "");
        cleanText = cleanText.replaceAll("UPDATE", "");
        cleanText = cleanText.replaceAll("update", "");
        cleanText = cleanText.replaceAll("DELETE", "");
        cleanText = cleanText.replaceAll("delete", "");
    } while (cleanText.toLowerCase().includes("select") && cleanText.toLowerCase().includes("create") &&
    	cleanText.toLowerCase().includes("update") && cleanText.toLowerCase().includes("delete"));
    alert(cleanText); // For testing purposes
    return cleanText;
}
