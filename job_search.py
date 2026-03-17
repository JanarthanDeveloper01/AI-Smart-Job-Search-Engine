def search_jobs(role):

    role_query = role.replace(" ", "%20")

    jobs = [
        {
            "title": role,
            "company": "LinkedIn Jobs",
            "location": "India",
            "link": f"https://www.linkedin.com/jobs/search/?keywords={role_query}&location=India"
        },
        {
            "title": role,
            "company": "Indeed",
            "location": "India",
            "link": f"https://www.indeed.com/jobs?q={role_query}&l=India"
        },
        {
            "title": role,
            "company": "Naukri",
            "location": "India",
            "link": f"https://www.naukri.com/{role_query}-jobs"
        }
    ]

    return jobs