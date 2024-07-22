class RateLimiter:
    def __init__(self, max_requests, period):
        self.max_requests = max_requests
        self.period = period
        self.requests = []
    
    def allow_request(self, timestamp):
        # Remove requests outside the current period
        self.requests = [r for r in self.requests if r > timestamp - self.period]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(timestamp)
            return True
        return False
