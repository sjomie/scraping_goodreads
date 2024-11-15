def normalize_date(date_string: str) -> str :
    date_list = date_string.split()
    year = int(date_list[-1])
    date_list [-1] = f"{year:04d}"
    date_string = ' '.join(date_list)
    return date_string
