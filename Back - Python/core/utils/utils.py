def handle_server_down():
    return {
        "status": "false",
        "message": "Database server status: Database server is down. Please try again later."
    }
    
def handle_server_up():
    return {
        "status": "true",
        "message": "Database server is up. :D"
    }
