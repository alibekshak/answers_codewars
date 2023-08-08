def job_matching(candidate, job):
    if candidate["min_salary"] * 0.9 <= job["max_salary"]:
        return True
    else:
        return False 