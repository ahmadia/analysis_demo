def read(websites_file):
    sites = {}
    with open(websites_file) as websites:
        for website in websites.readlines():
            name, url = website.split()
            sites[name] = url
    return sites
