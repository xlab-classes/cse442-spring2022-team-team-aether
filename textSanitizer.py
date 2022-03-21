# This will sanitize text of foreign JavaScript code and SQL commands


def sanitizeData(text):
    cleanText = text
    # General syntax breaker
    cleanText = cleanText.replace(";", "")
    # Replace HTML characters
    cleanText = cleanText.replace("&", "&amp")
    cleanText = cleanText.replace("<", "&lt")
    cleanText = cleanText.replace(">", "&gt")
    while (cleanText.lower().find("select")!=-1 or cleanText.lower().find("create")!=-1 or
        cleanText.lower().find("update")!=-1 or cleanText.lower().find("delete")!=-1):
        # Finish off with SQL commands
        cleanText = cleanText.replace("SELECT", "")
        cleanText = cleanText.replace("select", "")
        cleanText = cleanText.replace("CREATE", "")
        cleanText = cleanText.replace("create", "")
        cleanText = cleanText.replace("UPDATE", "")
        cleanText = cleanText.replace("update", "")
        cleanText = cleanText.replace("DELETE", "")
        cleanText = cleanText.replace("delete", "")
    # Stripping of additional spaces
    for i in range(len(cleanText)-1, 0, -1):
        if cleanText[i]==" " and cleanText[i-1]==" ":
            cleanText = cleanText[:i-1] + cleanText[i:]
    return cleanText
