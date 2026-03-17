def detect_domain_roles(text):

    text = text.lower()

    if "network" in text:
        return ["Network Engineer", "Network Administrator", "System Engineer"]

    elif "java" in text:
        return ["Java Developer", "Backend Developer", "Software Engineer"]

    elif "python" in text and "machine learning" in text:
        return ["Machine Learning Engineer", "Data Scientist", "AI Engineer"]

    elif "data" in text:
        return ["Data Analyst", "Data Scientist"]

    else:
        return ["Software Engineer"]